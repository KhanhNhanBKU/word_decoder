#TODO: INPUT hand_state
from typing import Tuple
import numpy as np
from database import Database


class Punish:
  def __init__(self) -> None:
    self.database = Database().get_database()


  def punish(self, input):
    #TODO
    # Pattern correct -> 100 point, incorrect -> -50, -25, -10, -5 correctpodings to pattern
    # Location correct -> 50 point, incorrect -> 0 point
    # Direction correct -> 25 point, incorrect -> 0 point
    # Point < 0 -> 0 point
    score_array = []
    for hand_state in self.database:

      # Process for pattern
      score_pattern = self.process_pattern(hand_state["PATTERN"], input["PATTERN"])
      # Process for location
      score_location = self.process_location(hand_state["LOCATION"], input["LOCATION"])
      # Process for direction
      score_direction = self.process_direction(hand_state["DIRECTION"], input["DIRECTION"])
      
      score = score_pattern + score_location + score_direction

      score_array.append(score)

    result = self.soft_max(score_array)
    return result

  def process_pattern(self, origin_pattern, input_pattern):
    """
      input: 2 pattern
      output: score for pattern
    """
    score = 100
    left_pattern, right_pattern = origin_pattern
    left_pattern_input, right_pattern_input = input_pattern
    
    if left_pattern == left_pattern_input and right_pattern == right_pattern_input:
      return score
    elif left_pattern != left_pattern_input and right_pattern != right_pattern_input:
      return 0
    else:
      return 50 + self.get_score_for_incorrect_pattern(origin_pattern,input_pattern)


  def get_score_for_incorrect_pattern(self,pattern, input_pattern):
    left_pattern, right_pattern = pattern
    left_pattern_input, right_pattern_input = input_pattern

    database = Database()
    score = 50
    if left_pattern == left_pattern_input:
      if left_pattern_input == "_":
        score -= 20
      pattern_relative = database.get_hand_state_relation(right_pattern_input)
      if right_pattern_input in pattern_relative:
        score -= 10
      else:
        if right_pattern_input == "_":
          score -= 50
        else:
          score -= 20
    elif right_pattern == right_pattern_input:
      if right_pattern_input == "_":
        score -= 20
      pattern_relative = database.get_hand_state_relation(left_pattern_input)
      if left_pattern_input in pattern_relative:
        score -= 10
      else:
        if left_pattern_input == "_":
          score -= 50
        else:
          score -= 20
    return score

  def process_location(self, origin_location, input_location):
    """
      input: 2 location
      output: score for location
    """
    left_location, right_location = origin_location
    left_location_input, right_location_input = input_location
    if left_location == left_location_input and right_location == right_location_input:
      return 100
    elif left_location == left_location_input and right_location != right_location_input:
      return 50
    elif left_location != left_location_input and right_location == right_location_input:
      return 50
    else:
      return 0

  def process_direction(self,origin_direction, input_direction):
    """
      input: 2 direction
      output: score for direction
    """
    left_direction, right_direction = origin_direction
    left_direction_input, right_direction_input = input_direction

    left_direction, right_direction = origin_direction
    left_direction_input, right_direction_input = input_direction
    if left_direction == left_direction_input and right_direction == right_direction_input:
      return 100
    elif left_direction == left_direction_input and right_direction != right_direction_input:
      return 50
    elif left_direction != left_direction_input and right_direction == right_direction_input:
      return 50
    else:
      return 0

  def soft_max(self, score_array):
    e_x = np.exp(score_array - np.max(score_array)) 
    return e_x / e_x.sum(axis=0) 

  def CTC(self):
    
    pass



# p = Punish()
# input = { 
#           "PATTERN": ("_","E"),
#           "LOCATION": ("_","MOUTH"),
#           "DIRECTION": ("_","_") 
#         }

# result = p.punish(input)
# print(result)
  
