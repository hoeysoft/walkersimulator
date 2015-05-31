from kivy.event      import EventDispatcher
from kivy.properties import ObjectProperty, ListProperty, NumericProperty
from kivy.vector     import Vector

from random    import uniform
from myutil    import *


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
        self.direction               = self.controller.update(self, dt)
        self.position, self.velocity = self.updater.update(self, dt)


class Controller:
    def update(self, walker, dt):
        return walker.direction

class Updater:
    def __init__(self, quadtree):
        pass

    def update(self, walker, dt):
        self.velocity = self.velocity+(force*dt)
        self.position = (self.velocity*dt) + self.position
        return walker.position, walker.velocity

    def update(self, walker, dt):
        force = self._calculate_force(walker)
        vel = walker.velocity+(force*dt)
        pos = vel*dt + walker.position
        return pos, vel

    def _calculate_force(self, walker):
        force  = self._base_force(walker)
        force += self._damping_force()
        #force += self._favoid_others(men_locinfo)
        return force

    def _base_force(self, walker):
        return ((walker.direction*walker.speed*1.5)-walker.velocity)/.5

    def _damping_force(self):
        return Vector(uniform(-1., 1.), uniform(-1., 1.))


class WalkerFactory(EventDispatcher):
    def build(self, settings, quadtree):
        self.settings   = settings
        self.controller = Controller()
        self.updater    = Updater(quadtree)

        sync_property(settings, 'world_size', self, 'world_size')
        sync_property(settings, 'walker_radius', self, 'radius')
        sync_property(settings, 'walker_speed' , self, 'speed')

    def create(self):
        w = Walker()
        w.position   = [uniform(0, self.world_size[0]), uniform(0, self.world_size[1])]
        w.direction  = Vector(uniform(-1, 1), uniform(-1, 1)).normalize()

        sync_property(self.settings, 'walker_speed',  w, 'speed')
        sync_property(self.settings, 'walker_radius', w, 'radius')

        w.controller = self.controller
        w.updater    = self.updater
        return w
