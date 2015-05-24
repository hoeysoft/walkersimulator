from kivy.uix.widget import Widget
from kivy.vector     import Vector

class Zombie(Widget):
    def build(self):
        self.accs = set()
        self.vel = Vector(0, 0)

    def acc(self, arrow):
        self.accs.add(arrow)

    def deacc(self, arrow):
        self.accs.remove(arrow)

    def update(self):
        self.pos = self.vel + self.pos
