import MontiMaths as mm
from math import tan, pi, atan2, acos

class Shape:
    def __init__(self, position, material):
        self.position = position
        self.material = material

    def intersect(self, origin, direction):
        return None

    def normal(self, point):
        raise NotImplementedError()
    

class Intercept:
    def __init__(self, distance, point, normal, obj, texcoords):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.texcoords = texcoords
        self.obj = obj


class Sphere(Shape):
    def __init__(self, position, radius, material):
        super().__init__(position, material)
        self.radius = radius

    def intersect(self, origin, direction):
        L = mm.subVec(self.position, origin)
        lengthL = mm.magVec(L)
        tca = mm.dotProd(L, direction)
        d = (lengthL ** 2 - tca ** 2) ** 0.5

        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1

        if t0 < 0:
            return None

        point = mm.addVec(origin, mm.escMultVector(t0, direction))
        normal = mm.subVec(point, self.position)
        normal = mm.normVec(normal)

        u = (atan2(normal[2], normal[0]) / (2 * pi)) + 0.5
        v = acos(normal[1]) / pi

        return Intercept(distance=t0,
                         point=point,
                         normal=normal,
                         texcoords=(u, v),
                         obj=self)