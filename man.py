from kivy.uix.widget import Widget
from kivy.vector     import Vector

from myutil  import *
from options import *


class Man(Widget):
    def build(self):
        self._away_direction = Vector(0,0)
        pass

    def set_target(self, zombie):
        zombie.bind(pos=self._on_zombie_move)

    def update(self):
        self.pos = self._direction()*MAN_SPEED + self.pos

    def _on_zombie_move(self, instance, value):
        self._away_direction = vsub(self.pos, value).normalize()

    def _direction(self):
        return self._away_direction
