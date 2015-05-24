from kivy.metrics import *

MAN_COUNT = 50
MAN_AVOID = 10

# visual options
ZOMBIE_COLOR = [1, 0, 0, 1]
MAN_COLOR    = [1, 1, 1, 1]

# resolution dependent
BORDER       = dp(5)

ZOMBIE_SIZE  = dp(40) # radius
ZOMBIE_SPEED = dp(50)

MAN_SIZE     = dp(50) # radius
MAN_SPEED    = dp(50)

MAN_SIGHT    = MAN_SPEED*3
