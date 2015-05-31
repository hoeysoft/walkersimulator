from kivy.metrics    import *
from kivy.event      import EventDispatcher
from kivy.properties import ObjectProperty, BooleanProperty, \
                            NumericProperty, BoundedNumericProperty
from kivy.vector     import Vector


# visual options
ZOMBIE_COLOR = [1, 0, 0, 1]
MAN_COLOR    = [1, 1, 1, 1]

# resolution dependent
ZOMBIE_SIZE  = dp(40) # radius
ZOMBIE_SPEED = dp(500)

MAN_SIZE  = dp(30) # radius
MAN_SPEED = dp(100)

MAN_SIGHT = MAN_SPEED*7
MAN_AVOID = MAN_SPEED*5

class Settings(EventDispatcher):
    world_size    = ObjectProperty(Vector(100, 100))
    use_avoidance = BooleanProperty(True)
    walker_count  = BoundedNumericProperty(30, min=1, max=100)
    walker_radius = BoundedNumericProperty(dp(20), min=dp(5), max=dp(100))
    walker_speed  = BoundedNumericProperty(dp(30), min=dp(1), max=dp(200))
