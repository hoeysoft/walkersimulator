from kivy.metrics    import *
from kivy.event      import EventDispatcher
from kivy.properties import ObjectProperty, BooleanProperty, BoundedNumericProperty
from kivy.vector     import Vector


class Settings(EventDispatcher):
    world_size      = ObjectProperty(Vector(100, 100))
    use_avoidance   = BooleanProperty(False)
    show_directions = BooleanProperty(False)

    walker_count  = BoundedNumericProperty(25, min=0, max=150)
    walker_radius = BoundedNumericProperty(dp(50), min=dp(5),  max=dp(100))
    walker_sight  = BoundedNumericProperty(dp(50), min=dp(10), max=dp(200))
    walker_speed  = BoundedNumericProperty(dp(20), min=dp(1),  max=dp(200))
    walker_force  = BoundedNumericProperty(dp(500),min=dp(100), max=dp(5000))
