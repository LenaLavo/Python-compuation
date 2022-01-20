import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color, num in kwargs.items():
      while num > 0:
        self.contents.append(color)
        num -= 1
  
  def draw(self, draw):
    balls = []

    if draw > len(self.contents):
      return self.contents

    for ball in range(draw):
      popped = self.contents.pop(random.randrange(len(self.contents)))
      balls.append(popped)
    return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for x in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn = hat_copy.draw(num_balls_drawn)
    Z = 0
    for key, value in expected_balls.items():
      if drawn.count(key) >= value:
        Z += 1
      if Z == len(expected_balls):
        M += 1
  return M / num_experiments

