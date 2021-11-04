class HandState:
  def __init__(self, _pattern, _location, _direction) -> None:
    self.pattern = _pattern
    self.location = _location
    self.direction = _direction

  def get_pattern(self) -> str:
    return self.pattern

  def get_location(self) -> str:
    return self.location
  
  def get_direction(self) -> str:
    return self.direction

  def set_pattern(self, _pattern) -> None:
    self.pattern = _pattern
  
  def set_location(self, _location) -> None:
    self.location = _location
  
  def set_direction(self, _direction) -> None:
    self.direction = _direction

  def get_hand_state(self) -> tuple:
    return (self.pattern, self.location, self.direction)