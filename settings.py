from kivy.metrics    import *
from kivy.event      import EventDispatcher
from kivy.properties import ObjectProperty, BooleanProperty, BoundedNumericProperty
from kivy.vector     import Vector


class Settings(EventDispatcher):
    world_size    = ObjectProperty(Vector(100, 100))
    use_avoidance = BooleanProperty(True)

    walker_count  = BoundedNumericProperty(30, min=0, max=200)
    walker_radius = BoundedNumericProperty(dp(20),  min=dp(5),  max=dp(100))
    walker_sight  = BoundedNumericProperty(dp(100), min=dp(10), max=dp(200))
    walker_speed  = BoundedNumericProperty(dp(50),  min=dp(1),  max=dp(200))
    walker_force  = BoundedNumericProperty(dp(500), min=dp(100), max=dp(5000))
