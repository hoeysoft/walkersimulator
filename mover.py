from kivy.event      import EventDispatcher
from kivy.properties import ObjectProperty, NumericProperty
from kivy.vector     import Vector

from random import uniform


class Mover(EventDispatcher):
    position  = ObjectProperty(Vector(0, 0))
    direction = ObjectProperty(Vector(0, 0))
    velocity  = ObjectProperty(Vector(0, 0))
    speed     = NumericProperty(0)

    def update(self, dt, settings):
        force = self._calculate_force(settings)
        self.velocity = self.velocity+(force*dt)
        self.position = (self.velocity*dt) + self.position

    def _calculate_force(self, settings):
        force  = self._base_force()
        force += self._damping_force()
        #force += self._favoid_others(men_locinfo)
        return force

    def _base_force(self):
        return ((self.direction*self.speed*1.5)-self.velocity)/.5

    def _damping_force(self):
        return Vector(uniform(-1., 1.), uniform(-1., 1.))
