from kivy.uix.widget import Widget
from kivy.vector     import Vector

from myutil import *
from options import *


class Zombie(Widget):
    def build(self):
        self.accs = set()

    def acc(self, arrow):
        self.accs.add(arrow)

    def deacc(self, arrow):
        self.accs.remove(arrow)

    def update(self):
        self.pos = self._direction()*ZOMBIE_SPEED + self.pos

    def _direction(self):
        if not self.accs:
            return Vector(0,0)
        directions = [KEY_DIRECTION[d] for d in self.accs]
        return reduce(lambda x,y: x+y, directions).normalize()
