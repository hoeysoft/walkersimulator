from kivy.metrics         import *
from kivy.vector          import Vector
from kivy.uix.boxlayout   import BoxLayout
from kivy.uix.stencilview import StencilView
from kivy.graphics        import Ellipse, Line, Color

from myutil   import *

class Screen(BoxLayout, StencilView):
    def build(self, settings, world):
        self.world    = world
        self.selected = None

    def update(self, dt):
        self.canvas.clear()
        with self.canvas:
            for walker in self.world.walkers:
                pos       = walker.position+self.pos
                rad, rad2 = walker.radius, walker.radius*2

                Color(1, 1, 1)
                lbpos = pos - Vector(rad, rad)
                Ellipse(pos=lbpos, size=(rad2, rad2))


                Color(1, 0, 0)
                dirlen = rad*1.5
                points = [pos]+[pos+walker.direction*dirlen]
                Line(points=[e for p in points for e in p])


                Color(0, 1, 0)
                vellen = rad*1.8
                points = [pos]+[pos+walker.velocity.normalize()*vellen]
                Line(points=[e for p in points for e in p])

            if self.selected:
                pos = self.selected.position+self.pos
                rad = self.selected.radius
                Color(1, 0, 0)
                Line(width=3., circle=(pos[0], pos[1], rad))

                for t,_,_,_ in self.selected.targets:
                    if t == self.selected: continue
                    tpos = t.position+self.pos
                    rad  = t.radius
                    Color(0, 1, 0)
                    Line(width=3., circle=(tpos[0], tpos[1], rad))


    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False

        pos = Vector(touch.pos) - self.pos
        targets = self.world.quadtree.query(pos, dp(100))
        if not targets:
            return False

        # pick the nearest one: sort by pos distnace
        self.selected = sorted(targets, key=lambda t: pos.distance2(t[1]))[0][0]

    def on_touch_move(self, touch):
        if not self.selected:
            return False
        pos = Vector(touch.pos) - self.pos
        self.selected.direction = (pos-self.selected.position).normalize()

    def on_touch_up(self, touch):
        if not self.selected:
            return False
        self.selected = None
