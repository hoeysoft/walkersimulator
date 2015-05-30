from kivy.metrics import *

MAN_COUNT  = 20

# visual options
ZOMBIE_COLOR = [1, 0, 0, 1]
MAN_COLOR    = [1, 1, 1, 1]

# resolution dependent
ZOMBIE_SIZE  = dp(45) # radius
ZOMBIE_SPEED = dp(500)

MAN_SIZE  = dp(60) # radius
MAN_SPEED = dp(300)

MAN_SIGHT = MAN_SPEED*1
MAN_AVOID = MAN_SPEED*20
