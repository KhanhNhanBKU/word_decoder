class Database:
  def __init__(self) -> None:
    PATTERN = 'PATTERN'
    LOCATION = 'LOCATION'
    DIRECTION = 'DIRECTION'
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    MOUTH = 'MOUTH'
    CHEST = 'CHEST'
    DOWN = 'DOWN'
    FORWARD = 'FORWARD'
    BACKWARD = 'BACKWARD'
    _ = '_'
    LEFT = 'LEFT'

    self.database = [
      { 
        PATTERN: (_,A),
        LOCATION: (_,MOUTH),
        DIRECTION: (_,_) 
      },
      { 
        PATTERN: (_,B),
        LOCATION: (_,CHEST),
        DIRECTION: (_,FORWARD) 
      },
      { 
        PATTERN: (_,C),
        LOCATION: (_,CHEST),
        DIRECTION: (_,BACKWARD) 
      },
      { 
        PATTERN: (_,C),
        LOCATION: (_,CHEST),
        DIRECTION: (_,FORWARD) 
      },
      {
        PATTERN: (A,D),
        LOCATION: (CHEST,CHEST),
        DIRECTION: (DOWN,LEFT)
      }
    ]
  def get_database(self) -> list:
    return self.database

  def get_hand_state_relation(self, input):
    data = {
      'A': ['D','E'],
      'B': [],
      'C': [],
      'D': ['A','E'],
      'E': ['A','D'],
      '_': [],
    }

    return data[input]