from kivy.uix.widget import Widget
from kivy.vector     import Vector

class Man(Widget):
    def build(self):
        pass

    def set_target(self, zombie):
        zombie.bind(pos=self._on_zombie_move)

    def update(self):
        pass

    def _on_zombie_move():
        pass
