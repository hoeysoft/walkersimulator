from kivy.event      import EventDispatcher
from kivy.properties import ObjectProperty, ListProperty, NumericProperty
from kivy.vector     import Vector


class Zombie(EventDispatcher):
    position  = ObjectProperty(Vector(0, 0))
    velocity  = ObjectProperty(Vector(0, 0))
    direction = ObjectProperty(Vector(0, 0))
    speed     = NumericProperty(0)
    sight     = NumericProperty(0)
    force     = NumericProperty(0)
    radius    = NumericProperty(0)
    color     = ListProperty([])

#from kivy.uix.widget import Widget
#from kivy.vector     import Vector
#
#from random import uniform
#
#from myutil   import *
#from settings import *
#
#
#class Zombie(Widget):
#    def build(self, settings):
#        self.accs = set()
#
#        def on_use_avoidance(ins, val):
#            self.use_avoidance = val
#            self._reset_position()
#
#        self.use_avoidance = settings.use_avoidance
#        settings.bind(use_avoidance=on_use_avoidance)
#
#    def acc(self, arrow):
#        self.accs.add(arrow)
#
#    def deacc(self, arrow):
#        self.accs.remove(arrow)
#
#    def update(self, dt):
#        self.pos = self._direction()*ZOMBIE_SPEED*dt + self.pos
#
#    def _direction(self):
#        if not self.accs:
#            return Vector(0,0)
#        directions = [KEY_DIRECTION[d] for d in self.accs]
#        return reduce(lambda x,y: x+y, directions).normalize()
#
#    def _reset_position(self):
#        x = uniform(MAN_SIZE*2, self.parent.width-MAN_SIZE*2)
#        y = uniform(MAN_SIZE*2, self.parent.height-MAN_SIZE*2)
#        self.pos = (x,y)
#
#    def _reset_direction(self):
#        pass
