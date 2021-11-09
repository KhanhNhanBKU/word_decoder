from math import log
import numpy as np

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



data = [[0.1, 0.2, 0.3, 0.4, 0.5],
		    [0.5, 0.4, 0.3, 0.2, 0.1],
		    [0.1, 0.2, 0.3, 0.4, 0.5],
		    [0.5, 0.4, 0.3, 0.2, 0.1],
		    [0.1, 0.2, 0.3, 0.4, 0.5],
		    [0.5, 0.4, 0.3, 0.2, 0.1],
		    [0.1, 0.2, 0.3, 0.4, 0.5],
		    [0.5, 0.4, 0.3, 0.2, 0.1],
		    [0.1, 0.2, 0.3, 0.4, 0.5],
		    [0.5, 0.4, 0.3, 0.2, 0.1]]

data = np.array(data)

result = beam_search_decoder(data, 3)
# print(result)
# for seq in result:
  # with open('output.txt') as f:
  #   f.write(str(seq))
  # print(seq)
# print(result)

queue = [
      { 
        "PATTERN": ("_","A"),
        "LOCATION": ("_","MOUTH"),
        "DIRECTION": ("_","_") 
      },
      { 
        "PATTERN": ("_","A"),
        "LOCATION": ("_","CHEST"),
        "DIRECTION": ("_","UP") 
      },
      { 
        "PATTERN": ("_","B"),
        "LOCATION": ("_","CHEST"),
        "DIRECTION": ("_","FORWARD") 
      },
      { 
        "PATTERN": ("_","_"),
        "LOCATION": ("_","CHEST"),
        "DIRECTION": ("_","_") 
      },
      { 
        "PATTERN": ("_","_"),
        "LOCATION": ("_","_"),
        "DIRECTION": ("_","_") 
      },
]

data = []
THRESHOLD = 0.4
for i in queue:
  p = Punish()
  score_array = p.punish(i).tolist()
  # for j in range(len(score_array)):
  #   if score_array[j] < THRESHOLD:
  #     score_array[j] = 0
  data.append(score_array)
  # data.append(p.punish(i))

# for i in data:
#   print(i)

result = beam_search_decoder(data, 3)
print(result[0][0])



