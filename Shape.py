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
    

class Plane(Shape):
    def __init__(self, position, normal, material, repeat_texture=True):
        self.normal = mm.normVec(normal)
        super().__init__(position, material)
        self.repeat_texture = repeat_texture

    def intersect(self, origin, direction):
        denom = mm.dotProd(direction, self.normal)

        if abs(denom) <=0.0001:
            return None

        num = mm.dotProd(mm.subVec(self.position, origin), self.normal)
        t= num / denom

        if t < 0 :
            return None
        
        P = mm.addVec(origin, mm.escMultVector(t, direction))

        return Intercept(distance=t,
                         point=P,
                         normal=self.normal,
                         texcoords=None,
                         obj=self)


class Disk(Plane):
    def __init__(self, position, normal, radius, material):
        super().__init__(position, normal, material)
        self.radius = radius

    def intersect(self, origin, direction):
        intersect = super().intersect(origin, direction)

        if intersect is None:
            return None

        distance = mm.subVec(intersect.point, self.position)     
        distance = mm.magVec(distance)

        if distance > self.radius:
            return None
        
        return Intercept(distance=intersect.distance,
                         point=intersect.point,
                         normal=intersect.normal,
                         texcoords=None,
                         obj=self)


class AABB(Shape):
    def __init__(self, position, size, material):
        self.size = size
        super().__init__(position, material)

        self.planes = []

        self.size = size

        leftPlane = Plane(mm.addVec(position, (-size[0] / 2, 0, 0)), (-1, 0, 0), material)
        rightPlane = Plane(mm.addVec(position, (size[0] / 2, 0, 0)), (1, 0, 0), material)

        topPlane = Plane(mm.addVec(position, (0, size[1] / 2, 0)), (0, 1, 0), material)
        bottomPlane = Plane(mm.addVec(position, (0, -size[1] / 2, 0)), (0, -1, 0), material)

        frontPlane = Plane(mm.addVec(position, (0, 0, size[2]/ 2)), (0, 0, 1), material)
        backPlane = Plane(mm.addVec(position, (0, 0, -size[2]/ 2)), (0, 0, -1), material)

        self.planes.append(leftPlane)
        self.planes.append(rightPlane)
        self.planes.append(topPlane)
        self.planes.append(bottomPlane)
        self.planes.append(frontPlane)
        self.planes.append(backPlane)

        self.boundsMin =[0,0,0]
        self.boundsMax =[0,0,0]

        bias = 0.0001

        for i in range(3):
            self.boundsMin[i] = self.position[i] - (self.size[i] / 2 + bias)
            self.boundsMax[i] = self.position[i] + self.size[i] / 2 + bias

    def intersect(self, origin, direction):
        intersect = None
        t = float("inf")

        u=0
        v=0

        for plane in self.planes:

            planeIntersect = plane.intersect(origin, direction)

            if planeIntersect is not None:

                planePoint = planeIntersect.point

                if self.boundsMin[0] < planePoint[0] < self.boundsMax[0]:
                    if self.boundsMin[1] < planePoint[1] < self.boundsMax[1]:
                        if self.boundsMin[2] < planePoint[2] < self.boundsMax[2]:
                            if planeIntersect.distance < t:
                                t = planeIntersect.distance
                                intersect = planeIntersect

                                if abs(plane.normal[0])>0:
                                    u= (planePoint[1]-self.boundsMin[1]) / (self.size[1] + 0.002)
                                    v= (planePoint[2]-self.boundsMin[2]) / (self.size[2] + 0.002)
                                elif abs(plane.normal[1])>0:
                                    u= (planePoint[0]-self.boundsMin[0]) / (self.size[0] + 0.002)
                                    v= (planePoint[2]-self.boundsMin[2]) / (self.size[2] + 0.002)
                                elif abs(plane.normal[2])>0:
                                    u= (planePoint[0]-self.boundsMin[0]) / (self.size[0] + 0.002)
                                    v= (planePoint[1]-self.boundsMin[1]) / (self.size[1] + 0.002)


        if intersect is None:
            return None

        return Intercept(distance=t,
                            point=intersect.point,
                            normal=intersect.normal,
                            texcoords=(u,v),
                            obj=self)
