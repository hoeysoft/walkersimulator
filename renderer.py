from kivy.uix.boxlayout   import BoxLayout
from kivy.uix.stencilview import StencilView
from kivy.graphics        import Rectangle, Ellipse, Line, Color

from myutil   import *

class Renderer(BoxLayout, StencilView):
    def update(self, world, dt):
        self.canvas.clear()
        with self.canvas:
            for walker in world.walkers:
                pos       = walker.position+self.pos
                rad, rad2 = walker.radius, walker.radius*2

                Color(1, 1, 1)
                center = pos - Vector(rad, rad)
                Ellipse(pos=center, size=(rad2, rad2))

                Color(1, 0, 0)
                dirlen = rad*1.5
                points = [pos]+[pos+walker.direction*dirlen]
                Line(points=[e for p in points for e in p])

                Color(0, 1, 0)
                vellen = rad*1.8
                points = [pos]+[pos+walker.velocity.normalize()*vellen]
                Line(points=[e for p in points for e in p])
