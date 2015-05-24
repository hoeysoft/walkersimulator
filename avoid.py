from kivy.vector import Vector
from math        import sqrt, exp


def force(x_ij, v_ij, rsum, settings=None):
    '''calculate avoidance force
    x_ij = x_i - x_j
    v_ij = v_i - v_j
    rsum = r_i + r_j
    '''
    if settings is None: settings = {}
    k    = settings.get('k'   , 1.5)
    m    = settings.get('m'   , 2.0)
    t0   = settings.get('t0'  , 3)
    maxt = settings.get('maxt', 999)

    # handle so close case
    dist = x_ij.length()
    if rsum > dist: rsum = .99*dist

    # speed diff is low
    a =  v_ij.dot(v_ij)
    if a < 0.001 and a > - 0.001:
        return Vector(0, 0)

    b      = -x_ij.dot(v_ij)
    c      = x_ij.dot(x_ij) - rsum**2;
    discr2 = b*b - a*c;

    # can't collide
    if discr2 <= 0:
        return Vector(0,0)

    discr = sqrt(discr2)
    t     = (b - discr) / a

    # can't collide
    if t < 0:    return Vector(0, 0)
    if t > maxt: return Vector(0, 0)
    
    return -k*exp(-t/t0)*(v_ij - (a*x_ij + b*v_ij)/(discr))/(a*t**m)*(m/t+ 1/t0)
