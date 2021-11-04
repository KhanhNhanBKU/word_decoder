from math import log
from numpy import array

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

data = array(data)

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

for i in queue:
  result = []
  p = Punish()
  result.append(p.punish(i))
  print(result)


