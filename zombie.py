from kivy.uix.widget import Widget
from kivy.vector     import Vector

from myutil   import *
from settings import *


class Zombie(Widget):
    def build(self, settings):
        self.accs = set()

        def on_use_avoidance(ins, val): self.use_avoidance = val
        self.use_avoidance = settings.use_avoidance
        settings.bind(use_avoidance=on_use_avoidance)

    def acc(self, arrow):
        self.accs.add(arrow)

    def deacc(self, arrow):
        self.accs.remove(arrow)

    def update(self, dt):
        self.pos = self._direction()*ZOMBIE_SPEED*dt + self.pos

    def _direction(self):
        if not self.accs:
            return Vector(0,0)
        directions = [KEY_DIRECTION[d] for d in self.accs]
        return reduce(lambda x,y: x+y, directions).normalize()
