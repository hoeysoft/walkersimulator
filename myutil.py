from kivy.vector     import Vector

KEY_DIRECTION = { \
    'left'  : Vector(-1, 0), \
    'right' : Vector(1, 0), \
    'up'    : Vector(0, 1), \
    'down'  : Vector(0, -1) \
}

def is_arrowkey(k):
    return (k in KEY_DIRECTION)
