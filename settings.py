from kivy.metrics    import *
from kivy.event      import EventDispatcher
from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty
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
    world_size    = ObjectProperty(Vector(1024, 1024))
    walker_count  = NumericProperty(10)
    use_avoidance = BooleanProperty(True)
    walker_radius = NumericProperty(dp(30))
    walker_speed  = NumericProperty(dp(100))
