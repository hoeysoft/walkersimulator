from kivy.metrics         import *
from kivy.vector          import Vector
from kivy.uix.boxlayout   import BoxLayout
from kivy.uix.stencilview import StencilView
from kivy.graphics        import Ellipse, Line, Color

from myutil   import *


LINERADIUS_RATIO = 1.8

class Screen(BoxLayout, StencilView):
    def build(self, settings, world):
        sync_property(settings, 'walker_radius'  , self)
        sync_property(settings, 'show_directions', self)

        self.world    = world
        self.selected = None

    def update(self, dt):
        if self.selected:
            if self.selected not in self.world.walkers:
                self.selected = None
        self.canvas.clear()
        with self.canvas:
            for walker in self.world.walkers:
                pos       = walker.position+self.pos
                rad, rad2 = walker.radius, walker.radius*2

                # make highlighted
                if self.selected: Color(.5, .5, .5)
                else:             Color(1, 1, 1)

                self._draw_walker(walker)

                if self.show_directions or walker == self.selected:
                    Color(1, 0, 0)
                    self._draw_direction(walker)

                    Color(0, 1, 0)
                    self._draw_velocity(walker)

            if self.selected:
                Color(1, 1, 1)
                self._draw_walker(self.selected)

                Color(1, 0, 0)
                self._draw_selected(self.selected)
                
                target_len = len(self.selected.targets)
                for i, target  in enumerate(self.selected.targets):
                    t, _, _, _ = target # (obj, pos, vel, rad)
                    if t == self.selected: continue

                    Color(1, 1, 0)
                    self._draw_selected(t)
                    self._draw_force(self.selected, self.selected.aforces[i])



    def _draw_walker(self, w):
        pos, rad, rad2 = w.position+self.pos, w.radius, w.radius+w.radius
        Ellipse(pos=pos-Vector(rad, rad), size=(rad2, rad2))

    def _draw_direction(self, w):
        pos, dir, rad = w.position+self.pos, w.direction, w.radius
        #points = [pos]+[pos+dir*rad*1.5]
        Line(width=1.5, points=_flat_points([pos]+[pos+dir*rad*LINERADIUS_RATIO]))

    def _draw_velocity(self, w):
        pos, vel, rad = w.position+self.pos, w.velocity, w.radius
        Line(width=1.5, points=_flat_points([pos]+[pos+vel.normalize()*rad*LINERADIUS_RATIO]))

    def _draw_selected(self, w):
        pos, rad = w.position+self.pos, w.radius
        Line(width=2., circle=(pos[0], pos[1], rad))

    def _draw_force(self, w, f):
        pos, rad = w.position+self.pos, w.radius
        vn, vl   = f.normalize(), f.length()
        Line(width=3., points=_flat_points([pos]+[pos+vn*max(vl, rad*LINERADIUS_RATIO)]))


    def on_touch_down(self, touch):
        if not self.collide_point(*touch.pos):
            return False

        pos = Vector(touch.pos) - self.pos
        targets = self.world.quadtree.query(pos, self.walker_radius*1.5)
        if not targets:
            self.selected = None
            return False

        # pick the nearest one: sort by pos distnace
        self.selected = sorted(targets, key=lambda t: pos.distance2(t[1]))[0][0]

    def on_touch_move(self, touch):
        if not self.selected:
            return False
        pos = Vector(touch.pos) - self.pos
        self.selected.direction = (pos-self.selected.position).normalize()

def _flat_points(points):
    return [e for p in points for e in p]
