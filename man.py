from kivy.uix.widget import Widget
from kivy.vector     import Vector

from random import uniform

from myutil   import *
from settings import *

import avoid


class Man(Widget):
    def build(self):
        self.vel = Vector(0,0)

    def set_target(self, zombie):
        pass
        #direction = Vector(uniform(-1,1), uniform(-1,1)).normalize() 
        #self.vel = direction*MAN_SPEED
        #zombie.bind(pos=self._on_zombie_move)
        #direction = (Vector(self.pos)-Vector(zombie.pos)).normalize()
        #self.vel = direction*MAN_SPEED

    def update(self, dt, men_locinfo):
        pass
        #pos  = Vector(self.pos)
        #vel  = self.vel
        #fsum = Vector(0, 0)
        #for li in men_locinfo:
        #    x_ij = pos - li[0]
        #    if x_ij.length() > MAN_SIGHT: continue
        #    v_ij = vel - li[1]
        #    fsum += avoid.force(x_ij, v_ij, MAN_SIZE+MAN_SIZE)

        #self.pos = (vel+fsum*dt)*dt + self.pos

    def _on_zombie_move(self, instance, value):
        direction = (Vector(self.pos)-Vector(value)).normalize()
        self.vel = direction*MAN_SPEED
