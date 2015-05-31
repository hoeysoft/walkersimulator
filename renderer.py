#from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics           import Rectangle, Ellipse, Line, Color

from myutil   import *
from zombie   import Zombie
from man      import Man


class Renderer(RelativeLayout):
    def update(self, world, dt):
        self.canvas.clear()
        with self.canvas:
            for walker in world.walkers:

                pos       = walker.position
                rad, rad2 = walker.radius, walker.radius*2

                def is_inboundex():
                    x, y   = pos
                    bx, by = world.size
                    return x-rad>=0 and x+rad<=bx and y-rad>=0 and y+rad<=by

                if not is_inboundex(): continue

                Color(1, 1, 1)
                center = walker.position - Vector(rad, rad)
                Ellipse(pos=center, size=(rad2, rad2))

                Color(1, 0, 0)
                dirlen = rad*1.5
                points = [pos]+[pos+walker.direction*dirlen]
                Line(points=[e for p in points for e in p])


                Color(0, 1, 0)
                vellen = rad*1.8
                points = [pos]+[pos+walker.velocity.normalize()*vellen]
                Line(points=[e for p in points for e in p])


#    def build(self, settings):
#        self._register_keyboard()
#
#        self.zombie = Zombie()
#        self.zombie.build(settings)
#        self.add_widget(self.zombie)
#
#        self.men          = []
#        self.decide_order = 0
#        for i in xrange(MAN_COUNT):
#            man = Man()
#            man.build(settings)
#            self.add_widget(man)
#            self.men.append(man)
#
#    def start(self):
#        self.zombie.pos = self.center
#        for man in self.men:
#            man.pos = self._randpos()
#            man.set_target(self.zombie)
#
#    def update(self, dt):
#        self.zombie.update(dt)
#
#        men_locinfo = [(Vector(x.pos), Vector(x.vel)) for x in self.men]
#        for i, man in enumerate(self.men):
#            man.decide(dt, men_locinfo)
#            man.update(dt)
#        self._clamp_boundary()
#
#    def _register_keyboard(self):
#        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, 'text')
#        self._keyboard.bind(on_key_down=self._on_keyboard_down)
#        self._keyboard.bind(on_key_up=self._on_keyboard_up)
#
#    def _keyboard_closed(self):
#        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
#        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
#        self._keyboard = None
#
#    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
#        if is_arrowkey(keycode[1]):
#            self.zombie.acc(keycode[1])
#        return True
#
#    def _on_keyboard_up(self, keyboard, keycode):
#        if is_arrowkey(keycode[1]):
#            self.zombie.deacc(keycode[1])
#        return True
#
#    def _randpos(self):
#        x = uniform(MAN_SIZE*2, self.width-MAN_SIZE*2)
#        y = uniform(MAN_SIZE*2, self.height-MAN_SIZE*2)
#        return (x, y)
#
#    def _clamp_boundary(self):
#        for w in self.children:
#            lx, ux = 0, self.width -w.width
#            ly, uy = 0, self.height-w.height
#            if w.x < lx: w.x = lx
#            if w.x > ux: w.x = ux
#            if w.y < ly: w.y = ly
#            if w.y > uy: w.y = uy
#            if w.x == lx or w.x== ux or w.y == ly or w.y == uy:
#                w._reset_direction()
