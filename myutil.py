from kivy.vector     import Vector


def sync_property(src, srcname, dst, dstname=None):
    if not dstname: dstname = srcname
    setattr(dst, dstname, getattr(src,srcname))
    def listener(ins, val):
        setattr(dst, dstname, val)
    src.bind(**{srcname:listener})

KEY_DIRECTION = { \
    'up'    : Vector(0, 1), \
    'w'     : Vector(0, 1), \

    'left'  : Vector(-1, 0), \
    'a'     : Vector(-1, 0), \

    'down'  : Vector(0, -1), \
    's'     : Vector(0, -1), \

    'right' : Vector(1, 0), \
    'd'     : Vector(1, 0), \
}

def is_arrowkey(k):
    return (k in KEY_DIRECTION)
