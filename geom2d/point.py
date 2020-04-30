
import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distans(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        return math.sqrt(dx*dx + dy*dy)

    def __eq__(self, other):
         return self.x == other.x and self.y == other.y