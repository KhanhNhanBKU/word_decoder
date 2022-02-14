# from math import log
from collections import defaultdict
from dataclasses import InitVar, dataclass
from typing import Optional, List, Tuple

import numpy as np
from database import Database

from punish import Punish


def beam_search_decoder(data, k):
  sequences = [[[], 0.0]]

  for row in data:
    all_candidates = []

    for i in range(len(sequences)):
      seq, score = sequences[i]
      for j in range(len(row)):
        candidate = [seq + [j], score - log(row[j])]
        all_candidates.append(candidate)
    ordered = sorted(all_candidates, key= lambda tup:tup[1])
    # print(ordered) # ?????
    sequences = ordered[:k]

  return sequences



# data = [[0.1, 0.2, 0.3, 0.4, 0.5],
# 		    [0.5, 0.4, 0.3, 0.2, 0.1],
# 		    [0.1, 0.2, 0.3, 0.4, 0.5],
# 		    [0.5, 0.4, 0.3, 0.2, 0.1],
# 		    [0.1, 0.2, 0.3, 0.4, 0.5],
# 		    [0.5, 0.4, 0.3, 0.2, 0.1],
# 		    [0.1, 0.2, 0.3, 0.4, 0.5],
# 		    [0.5, 0.4, 0.3, 0.2, 0.1],
# 		    [0.1, 0.2, 0.3, 0.4, 0.5],
# 		    [0.5, 0.4, 0.3, 0.2, 0.1]]

# data = np.array(data)

# result = beam_search_decoder(data, 3)
# print(result)
# for seq in result:
  # with open('output.txt') as f:
  #   f.write(str(seq))
  # print(seq)
# print(result)




def log(x: float) -> float:
    with np.errstate(divide='ignore'):
        return np.log(x)





database = {
  "tôi": [
    {
      "PATTERN": [
        "_",
        "F"
      ],
      "LOCATION": [
        "_",
        "CHEST"
      ],
      "DIRECTION": [
        "_",
        "INWARD"
      ]
    }
  ],
  "bạn": [
    {
      "PATTERN": [
        "_",
        "F"
      ],
      "LOCATION": [
        "_",
        "CHEST"
      ],
      "DIRECTION": [
        "_",
        "FORWARD"
      ]
    }
  ]
}


@dataclass
class BeamEntry:
  pr_total: float = log(0)
  pr_non_blank: float = log(0)
  pr_blank: float = log(0)
  pr_text: float = log(1)
  lm_applied: bool = False  # flag if LM was already applied to this beam
  labeling: tuple = ()  # beam-labeling





class BeamList:
  def __init__(self) -> None:
      self.entries = defaultdict(BeamEntry)

  def normalize(self) -> None:
    """Length-normalise LM score."""
    for k in self.entries.keys():
      labeling_len = len(self.entries[k].labeling)
      self.entries[k].pr_text = (1.0 / (labeling_len if labeling_len else 1.0)) * self.entries[k].pr_text
  
  def sort_labelings(self) -> List[Tuple[int]]:
    """Return beam-labelings, sorted by probability."""
    beams = self.entries.values()
    sorted_beams = sorted(beams, reverse=True, key=lambda x: x.pr_total + x.pr_text)
    return [x.labeling for x in sorted_beams]


def beam_search(mat: np.ndarray, chars: str = "ABCD", beam_width: int = 2 ):
    """Beam search decoder.

    See the paper of Hwang et al. and the paper of Graves et al.

    Args:
        mat: Output of neural network of shape TxC.
        chars: The set of characters the neural network can recognize, excluding the CTC-blank.
        beam_width: Number of beams kept per iteration.
        lm: Character level language model if specified.

    Returns:
        The decoded text.
    """

    blank_idx = len(chars)
    max_T, max_C = mat.shape

    # initialise beam state
    last = BeamList()
    labeling = ()
    last.entries[labeling] = BeamEntry()
    last.entries[labeling].pr_blank = log(1)
    last.entries[labeling].pr_total = log(1)

    # go over all time-steps
    for t in range(max_T):
        curr = BeamList()

        # get beam-labelings of best beams
        best_labelings = last.sort_labelings()[:beam_width]

        # go over best beams
        for labeling in best_labelings:

            # probability of paths ending with a non-blank
            pr_non_blank = log(0)
            # in case of non-empty beam
            if labeling:
                # probability of paths with repeated last char at the end
                pr_non_blank = last.entries[labeling].pr_non_blank + log(mat[t, labeling[-1]])

            # probability of paths ending with a blank
            pr_blank = last.entries[labeling].pr_total + log(mat[t, blank_idx])

            # fill in data for current beam
            curr.entries[labeling].labeling = labeling
            curr.entries[labeling].pr_non_blank = np.logaddexp(curr.entries[labeling].pr_non_blank, pr_non_blank)
            curr.entries[labeling].pr_blank = np.logaddexp(curr.entries[labeling].pr_blank, pr_blank)
            curr.entries[labeling].pr_total = np.logaddexp(curr.entries[labeling].pr_total,
                                                           np.logaddexp(pr_blank, pr_non_blank))
            curr.entries[labeling].pr_text = last.entries[labeling].pr_text
            curr.entries[labeling].lm_applied = True  # LM already applied at previous time-step for this beam-labeling

            # extend current beam-labeling
            for c in range(max_C - 1):
                # add new char to current beam-labeling
                new_labeling = labeling + (c,)

                # if new labeling contains duplicate char at the end, only consider paths ending with a blank
                if labeling and labeling[-1] == c:
                    pr_non_blank = last.entries[labeling].pr_blank + log(mat[t, c])
                else:
                    pr_non_blank = last.entries[labeling].pr_total + log(mat[t, c])

                # fill in data
                curr.entries[new_labeling].labeling = new_labeling
                curr.entries[new_labeling].pr_non_blank = np.logaddexp(curr.entries[new_labeling].pr_non_blank,
                                                                       pr_non_blank)
                curr.entries[new_labeling].pr_total = np.logaddexp(curr.entries[new_labeling].pr_total, pr_non_blank)


        # set new beam state
        last = curr

    # normalise LM scores according to beam-labeling-length
    last.normalize()

    # sort by probability
    best_labeling = last.sort_labelings()[0]  # get most probable labeling

    # map label string to char string
    # res = ''.join([chars[label] for label in best_labeling])
    return best_labeling


def find_word(input: Tuple[int] , database: dict):
  input = np.array(list(input))
  for _ in database.keys():
    word = np.array(database.get(_))
    if (input == word).all():
      return _
  return ""




# queue = [
#       { 
#         "PATTERN": ("_","D"),
#         "LOCATION": ("_","MOUTH"),
#         "DIRECTION": ("_","_") 
#       },
#       { 
#         "PATTERN": ("_","D"),
#         "LOCATION": ("_","MOUTH"),
#         "DIRECTION": ("_","_") 
#       },
#       { 
#         "PATTERN": ("_","B"),
#         "LOCATION": ("_","SHOULDER"),
#         "DIRECTION": ("_","_") 
#       },
#       { 
#         "PATTERN": ("_","G"),
#         "LOCATION": ("_","SHOULDER"),
#         "DIRECTION": ("_","_") 
#       },
#       { 
#         "PATTERN": ("_","_"),
#         "LOCATION": ("_","_"),
#         "DIRECTION": ("_","_") 
#       },
# ]



queue = [
  {
    "PATTERN": ["_","F"],
    "LOCATION": ["_","CHEST"],
    "DIRECTION": ["_","INWARD"]
  },
  {
    "PATTERN": ["_","F"],
    "LOCATION": ["_","CHEST"],
    "DIRECTION": ["_","INWARD"]
  },
  {
    "PATTERN": ["_","F"],
    "LOCATION": ["_","CHEST"],
    "DIRECTION": ["_","INWARD"]
  },
  {
    "PATTERN": ["_","D"],
    "LOCATION": ["_","MOUTH"],
    "DIRECTION": ["_","_"]
  },
  {
    "PATTERN": ["_", '_'],
    "LOCATION": ["_","_"],
    "DIRECTION": ["_","_"],
  }

]


def check_similar_hand_state(first: dict, second: dict) -> bool :
  if first["PATTERN"][0] == second["PATTERN"][0] and first["PATTERN"][1] == second["PATTERN"][1]:
    if first["LOCATION"][0] == second["LOCATION"][0] and first["LOCATION"][1] == second["LOCATION"][1]:
      if first["DIRECTION"][0] == second["DIRECTION"][0] and first["DIRECTION"][1] == second["DIRECTION"][1]:
        return True
  return False


def max_index(param: List[int]):
  max_value = -1
  index = -1
  for i in range(len(param)):
    if param[i] > max_value:
      max_value = param[i]
      index = i
  return max_value, index
  



def most_character(queue: List[dict], database: List[dict], word_database: dict):
  frequency = []
  for i in range(len(database)):
    count = 0;
    for _ in queue:
      if check_similar_hand_state(database[i], _):
        count += 1
    frequency.append(count)
  freq, index = max_index(frequency)


  return find_word(tuple([index]), word_database)




db = Database().get_database()
database = Database().get_word_database()

first_predict = most_character(queue, db, database)



data = []
# THRESHOLD = 0.4
for i in queue:
  p = Punish()
  score_array = p.punish(i).tolist()
  data.append(score_array)

mat = np.array(data)

result = beam_search(mat,"ABCD")
word = find_word(result, database)
print(word)













"""
      CheckList:
        [] Function compare 2 hand state
        [] Preparing database. Choose word needed
        [] Connect pin
        [] Standardize word
        [] Return word
        [] Preparing  
"""
