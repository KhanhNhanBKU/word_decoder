class HandState:
  def __init__(self, _pattern, _location, _direction) -> None:
    self.pattern = _pattern
    self.location = _location
    self.direction = _direction

  def get_pattern(self):
    return self.pattern

  def get_location(self):
    return self.location
  
  def get_direction(self):
    return self.direction

  def set_pattern(self, _pattern):
    self.pattern = _pattern
  
  def set_location(self, _location):
    self.location = _location
  
  def set_direction(self, _direction):
    self.direction = _direction

  def get_hand_state(self):
    return (self.pattern, self.location, self.direction)