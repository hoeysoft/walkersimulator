from kivy.event      import EventDispatcher
from kivy.properties import ObjectProperty, ListProperty, NumericProperty
from kivy.vector     import Vector

from random    import uniform
from myutil    import *

import avoid


class Walker(EventDispatcher):
    position  = ObjectProperty(Vector(0, 0))
    velocity  = ObjectProperty(Vector(0, 0))
    direction = ObjectProperty(Vector(0, 0))
    speed     = NumericProperty(0)
    sight     = NumericProperty(0)
    force     = NumericProperty(0)
    radius    = NumericProperty(0)
    color     = ListProperty([])

    updater    = ObjectProperty(None)

    def update(self, dt):
        self.position, self.velocity = self.updater.update(self, dt)


class WalkerFactory(EventDispatcher):
    def build(self, settings, quadtree):
        self.settings   = settings

        self.updater    = Updater()
        self.updater.build(settings, quadtree)

        sync_property(settings, 'world_size', self, 'world_size')
        sync_property(settings, 'walker_radius', self, 'radius')
        sync_property(settings, 'walker_speed' , self, 'speed')

    def create(self):
        w = Walker()
        w.position  = Vector([uniform(0, self.world_size[0]), \
                               uniform(0, self.world_size[1])])
        w.direction = Vector(uniform(-1, 1), uniform(-1, 1)).normalize()

        sync_property(self.settings, 'walker_radius', w, 'radius')
        sync_property(self.settings, 'walker_speed',  w, 'speed')

        w.updater = self.updater
        return w


class Updater:
    def build(self, settings, quadtree):
        sync_property(settings, 'use_avoidance', self)
        sync_property(settings, 'walker_force' , self, 'forcemax')
        self.quadtree = quadtree

    def update(self, walker, dt):
        force = self._calculate_force(walker)
        vel = walker.velocity+(force*dt)
        pos = vel*dt + walker.position
        return pos, vel

    def _calculate_force(self, walker):
        force  = self._force_base(walker)
        force += self._force_damping()
        if self.use_avoidance:
            force += self._force_avoid(walker)
        return force

    def _force_base(self, walker):
        return ((walker.direction*walker.speed*2.0)-walker.velocity)/.5

    def _force_damping(self):
        return Vector(uniform(-1., 1.), uniform(-1., 1.))

    def _force_avoid(self, walker):
        pos, vel, rad = walker.position, walker.velocity, walker.radius

        fa = Vector(0, 0)
        for opos, ovel, orad in self.quadtree.query(walker.position):
            fa += self._force_avoid_with(pos-opos, vel-ovel, rad+orad)
        return fa

    def _force_avoid_with(self, x_ij, v_ij, rsum):
        if x_ij.length2() > 1000**2: return Vector(0, 0)
        f = avoid.force(x_ij, v_ij, rsum)
        return f.normalize()*min(f.length(), self.forcemax)

