from kivy.uix.widget import Widget
from kivy.vector     import Vector

from random import uniform

from myutil   import *
from settings import *

import avoid


class Man(Widget):
    def build(self, settings):
        self.target    = Vector(0, 0)
        self.direction = Vector(0, 0)
        self.vel       = Vector(0, 0)
        self._reset_direction()

    def set_target(self, zombie):
        pass
        #self.target = Vector(zombie.center)
        #zombie.bind(pos=self._on_zombie_moved)

    def decide(self, dt, men_locinfo):
        #self.direction = (Vector(self.target)-Vector(self.center)).normalize()
        fsum  = ((self.direction*MAN_SPEED*1.5)-self.vel)/.5
        fsum += Vector(uniform(-1., 1.), uniform(-1., 1.))
        fsum += self._favoid_others(men_locinfo)
        #fsum += self._favoid_wall()
        self.vel = self.vel+fsum*dt

    def update(self, dt):
        self.center = self.vel*dt + self.center

    def _on_zombie_moved(self, ins, val):
        self.target = Vector(ins.center)

    def _favoid_others(self, men_locinfo):
        pos = Vector(self.center)
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

        pos = Vector(self.center)
        vel = self.vel

        fav  = Vector(0, 0)
        fav += _favoid(pos-wall1, vel, MAN_SIZE)
        fav += _favoid(pos-wall2, vel, MAN_SIZE)
        return fav

    def _reset_position(self):
        x = uniform(MAN_SIZE*2, self.parent.width-MAN_SIZE*2)
        y = uniform(MAN_SIZE*2, self.parent.height-MAN_SIZE*2)
        self.pos = (x,y)

    def _reset_direction(self):
        self.direction = Vector(uniform(-1,1), uniform(-1,1)).normalize()

def _favoid(x_ij, v_ij, rsum):
    if x_ij.length2() > MAN_SIGHT**2: return Vector(0, 0)
    f = avoid.force(x_ij, v_ij, rsum)
    return f.normalize()*min(f.length(), MAN_AVOID)
