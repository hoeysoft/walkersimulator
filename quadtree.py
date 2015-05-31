from kivy.vector import Vector

QTNODE_CAPACITY = 2

class QuadTree:
    def __init__(self):
        self.root  = QtNode([0,0,0,0], QTNODE_CAPACITY)

    def rebuild(self, boundary, walkers):
        self.root  = QtNode(boundary, QTNODE_CAPACITY)
        for w in walkers:
            self.root.insert(w, w.position)

    def query(self, pos, rad):
        return self.root.query(pos, rad)

class QtNode:
    def __init__(self, boundary, capacity):
        self.boundary = map(int, boundary)
        self.capacity = capacity
        self.objects  = []
        self.children = []

    def insert(self, obj, point):
        point = map(int, point)
        if not self._contains(point):
            return False

        # insert current node
        if len(self.objects) < self.capacity:
            self._add(obj)
            return True

        # insert one of children
        if not self.children:
            self._subdivide()

        for cn in self.children:
            if cn.insert(obj, point):
                return True

        print 'insert failed', self.boundary, point
        return False

    def query(self, point, rad):
        targets = []

        # not in this node
        if not self._intersect(point, rad):
            return targets

        # check current node
        rad2 = rad**2
        for obj in self.objects:
            _, pos, _, _ = obj
            if pos.distance2(point) <= rad2:
                targets.append(obj)

        # check children
        for cn in self.children:
            targets.extend(cn.query(point, rad))

        return targets

    def _contains(self, point):
        x, y = point
        lx, ly, ux, uy = self.boundary
        return lx <= x <= ux and ly <= y <= uy

    def _intersect(self, point, rad):
        x, y = point
        rad2 = rad*2
        lx, ly, ux, uy = self.boundary
        cx, cy, w, h   = (lx+ux)/2, (ly+uy)/2, ux-lx, uy-ly
        return abs(x-cx)*2 <= w+rad2 and abs(y-cy)*2 <= h+rad2

    def _add(self, obj):
        self.objects.append([obj, Vector(obj.position[:]), Vector(obj.velocity[:]), obj.radius])

    def _subdivide(self):
        lx, ly, ux, uy = self.boundary
        hx, hy = (ux-lx)/2, (uy-ly)/2
        self.children.append(QtNode([lx,     ly,      lx+hx, ly+hy], self.capacity))
        self.children.append(QtNode([lx+hx+1,ly,      ux   , ly+hy], self.capacity))
        self.children.append(QtNode([lx,     ly+hy+1, lx+hx, uy   ], self.capacity))
        self.children.append(QtNode([lx+hx+1,ly+hy+1, ux   , uy   ], self.capacity))
