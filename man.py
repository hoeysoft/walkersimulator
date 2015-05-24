from kivy.uix.widget import Widget
from kivy.vector     import Vector

from random import uniform

from myutil   import *
from settings import *

import avoid


class Man(Widget):
    def build(self):
        self.direction = Vector(0, 0)
        self.vel       = Vector(0, 0)

    def set_target(self, zombie):
        zombie.bind(pos=self._on_zombie_move)

    def update(self, dt, men_locinfo):
        fsum  = ((self.direction*MAN_SPEED*1.5)-self.vel)/.5
        fsum += Vector(uniform(-1., 1.), uniform(-1., 1.))
        fsum += self._favoid_others(men_locinfo)
        fsum += self._favoid_wall()

        self.vel = self.vel+fsum*dt
        self.pos = self.vel*dt + self.pos

    def _on_zombie_move(self, instance, value):
        self.direction = (Vector(value)-Vector(self.pos)).normalize()

    def _favoid_others(self, men_locinfo):
        pos = Vector(self.pos)
        vel = self.vel

        fav = Vector(0, 0)
        for li in men_locinfo:
            fav += _favoid(pos-li[0], vel-li[1], MAN_SIZE+MAN_SIZE)
        return fav

    def _favoid_wall(self):
        width  = self.parent.width/2
        height = self.parent.height/2

        if self.x < width/2: wall1 = Vector(0, self.y)
        else:                wall1 = Vector(width, self.y)

        if self.y < height/2: wall2 = Vector(self.x, 0)
        else:                 wall2 = Vector(self.x, height)

        pos = Vector(self.pos)
        vel = self.vel

        fav  = Vector(0, 0)
        fav += _favoid(pos-wall1, vel, MAN_SIZE)
        fav += _favoid(pos-wall2, vel, MAN_SIZE)
        return fav

def _favoid(x_ij, v_ij, rsum):
    if x_ij.length2() > MAN_SIGHT**2: return Vector(0, 0)
    f = avoid.force(x_ij, v_ij, rsum)
    return f.normalize()*min(f.length(), MAN_AVOID)
