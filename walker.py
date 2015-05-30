from kivy.event      import EventDispatcher
from kivy.properties import ObjectProperty, ListProperty, NumericProperty
from kivy.vector     import Vector

from random import uniform


class Walker(EventDispatcher):
    position  = ObjectProperty(Vector(0, 0))
    velocity  = ObjectProperty(Vector(0, 0))
    direction = ObjectProperty(Vector(0, 0))
    speed     = NumericProperty(0)
    sight     = NumericProperty(0)
    force     = NumericProperty(0)
    radius    = NumericProperty(0)
    color     = ListProperty([])

    controller = ObjectProperty(None)
    updater    = ObjectProperty(None)

    def update(self, dt):
        self.direction = self.controller(self)
        self.position, self.velocity = self.updater(self, dt)
