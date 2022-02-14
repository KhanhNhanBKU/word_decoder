class Database:
  def __init__(self) -> None:

    self.database = [
      {
        "PATTERN": ["_","F"],
        "LOCATION": ["_","_"],
        "DIRECTION": ["_","INWARD"]
      },
      {
        "PATTERN": ["_","F"],
        "LOCATION": ["_", "_"],
        "DIRECTION": ["_","FORWARD"]
      },
      {
        "PATTERN": ["_","D"],
        "LOCATION": ["_","MOUTH"],
        "DIRECTION": ["_","_"]
      },
      {
        "PATTERN": ["_","B"],
        "LOCATION": ["_","SHOULDER"],
        "DIRECTION": ["_","_"]
      },
      {
        "PATTERN": ["_", '_'],
        "LOCATION": ["_","_"],
        "DIRECTION": ["_","_"],
      }
    ]

    self.word_database = {
      "cảm_ơn" : [2,3],
      "tôi": [1],
      "bạn": [0]
    }
    

  def get_database(self) -> list:
    return self.database
  
  def get_word_database(self) -> list:
    return self.word_database

  def get_hand_state_relation(self, input):
    data = {
      'A': [],
      'B': ["G","D"],
      'C': [],
      'D': ["Q,","G","C","M","B"],
      'E': [],
      'F': [],
      "G": ["B"],
      '_': [],
    }

    return data[input]