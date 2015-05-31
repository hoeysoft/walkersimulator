from kivy.event       import EventDispatcher
from kivy.properties  import ObjectProperty, ListProperty
from kivy.vector      import Vector

from myutil   import *
from settings import *
from quadtree import *
from walker   import *


class World(EventDispatcher):
    quadtree = ObjectProperty(None)
    walkers  = ListProperty([])

    def build(self, settings):
        self.quadtree = QuadTree()
        self.walker_factory = WalkerFactory()
        self.walker_factory.build(settings, self.quadtree)

        sync_property(settings, 'world_size'   , self, 'size')
        sync_property(settings, 'walker_count' , self)
        sync_property(settings, 'use_avoidance', self)

    def update(self, dt):
        self._arrange_walkers()
        self._update_walkers(dt)

    def _arrange_walkers(self):
        # remove walkers in out of bound
        def is_inbound(w):
            x,  y  = w.position
            bx, by = self.size
            rad    = w.radius
            return x+rad>=0 and x-rad<=bx and y+rad>=0 and y-rad<=by
        self.walkers = [w for w in self.walkers if is_inbound(w)]

        # fit to walker_count
        remained_walker_count = len(self.walkers)
        if remained_walker_count < self.walker_count:
            for i in xrange(self.walker_count - remained_walker_count):
                self.walkers.append(self.walker_factory.create())
        elif remained_walker_count > self.walker_count:
            self.walkers = self.walkers[:self.walker_count]

        # rebuild quadtree
        self.quadtree.rebuild([0,0]+self.size, self.walkers)

    def _update_walkers(self, dt):
        for walker in self.walkers:
            walker.update(dt)
