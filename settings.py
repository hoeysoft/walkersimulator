from kivy.metrics import *

MAN_COUNT = 100

# visual options
ZOMBIE_COLOR = [1, 0, 0, 1]
MAN_COLOR    = [1, 1, 1, 1]

# resolution dependent
ZOMBIE_SIZE  = dp(20) # radius
ZOMBIE_SPEED = dp(500)

MAN_SIZE  = dp(15) # radius
MAN_SPEED = dp(100)

MAN_SIGHT = MAN_SIZE*35
MAN_AVOID = MAN_SIZE*25
