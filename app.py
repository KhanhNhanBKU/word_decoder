from flask import Flask
from flask.globals import request
from numpy.core.fromnumeric import resize
from database import Database


from collections import defaultdict
from dataclasses import InitVar, dataclass
from typing import Optional, List, Tuple


from punish import Punish
from math import log
import numpy as np
import json
app = Flask(__name__)




def find_word(input: Tuple[int] , database: dict):
  input = np.array(list(input))
  for _ in database.keys():
    word = np.array(database.get(_))
    if (input == word).all():
      return _
  return "_"


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



@app.route("/word_decode", methods=["POST"])
def word_decode():
  queue = json.loads(request.get_json()["data"])
  print(queue)
  for item in queue:
    if item["PATTERN"][1] == "tro":
      item["PATTERN"][1] = "F"
    if item["DIRECTION"][1] == "up":
      item["DIRECTION"][1] = "INWARD"
    if item["DIRECTION"][1] == "down":
      item["DIRECTION"][1] = "BACKWARD"
  
  db = Database().get_database()
  database = Database().get_word_database()
  # result = most_character(queue, db, database)
  result = ""
  for i in range(len(queue)):
    for j in range(len(db)):
      result = check_similar_hand_state(queue[i],queue[j])
      if result:
        word = find_word(tuple([j]),database)
        return {"result": word}
  return {"result": result}
  

  # return { "result": result }

  # data = []
  # for i in queue:
  #   p = Punish()
  #   score_array = p.punish(i).tolist()
  #   data.append(score_array)
  # result = beam_search_decoder(data, 3)
  # print(result)
  # return str(result)




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
