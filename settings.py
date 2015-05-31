from kivy.metrics    import *
from kivy.event      import EventDispatcher
from kivy.properties import ObjectProperty, BooleanProperty, \
                            NumericProperty, BoundedNumericProperty
from kivy.vector     import Vector


#MAN_SIGHT = MAN_SPEED*7

class Settings(EventDispatcher):
    world_size    = ObjectProperty(Vector(100, 100))
    use_avoidance = BooleanProperty(True)
    walker_count  = BoundedNumericProperty(10, min=0, max=200)

    walker_radius = BoundedNumericProperty(dp(20), min=dp(5),  max=dp(100))
    walker_speed  = BoundedNumericProperty(dp(50), min=dp(1),  max=dp(200))
    walker_force  = BoundedNumericProperty(dp(50), min=dp(10), max=dp(2500))
