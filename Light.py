import MontiMaths as mm

class Light:
    def __init__(self, intensity=1, color=(1, 1, 1), lightType="LIGHT"):
        self.intensity = intensity
        self.color = color
        self.type = lightType

    def getColor(self):
        return [self.color[0] * self.intensity,
                self.color[1] * self.intensity,
                self.color[2] * self.intensity]

    def getDiffuseColor(self, intercept):
        return None

    def getSpecularColor(self, intercept, viewPosition):
        return None
    

class Ambient(Light):
    def __init__(self, intensity=1, color=(1, 1, 1)):
        super().__init__(intensity, color, "AMBIENT")


def reflect(normal, direction):
    reflectValue = mm.subVec(mm.escMultVector(2 * mm.dotProd(normal, direction), normal), direction)
    return mm.normVec(reflectValue)

class Directional(Light):
    def __init__(self, direction=(0, 1, 0), intensity=1, color=(1, 1, 1)):
        super().__init__(intensity, color, "DIRECTIONAL")
        self.direction = mm.normVec(direction)

    def getDiffuseColor(self, intercept):
        direction = [i * -1 for i in self.direction]

        intensity = mm.dotProd(intercept.normal, direction) * self.intensity
        intensity = max(0, min(1, intensity))
        intensity *= 1 - intercept.obj.material.ks

        return [i * intensity for i in self.color]

    def getSpecularColor(self, intercept, viewPosition):
        direction = [i * -1 for i in self.direction]

        reflectDirection = reflect(intercept.normal, direction)

        viewDirection = mm.subVec(viewPosition, intercept.point)
        viewDirection = mm.normVec(viewDirection)

        intensity = max(0, min(1, mm.dotProd(reflectDirection, viewDirection))) ** intercept.obj.material.spec
        intensity *= self.intensity
        intensity *= intercept.obj.material.ks

        return [i * intensity for i in self.color]


class Point(Light):
    def __init__(self, position=(0, 0, 0), intensity=1, color=(1, 1, 1)):
        super().__init__(intensity, color, "POINT")
        self.position = position

    def getDiffuseColor(self, intercept):
        direction = mm.subVec(self.position, intercept.point)
        radius = mm.magVec(direction)
        direction = mm.vectorDivEsc(direction, radius)

        intensity = mm.dotProd(intercept.normal, direction) * self.intensity
        intensity *= 1 - intercept.obj.material.ks

        if radius != 0:
            intensity /= radius ** 2
        intensity = max(0, min(1, intensity))

        return [i * intensity for i in self.color]

    def getSpecularColor(self, intercept, viewPosition):
        direction = mm.subVec(self.position, intercept.point)
        radius = mm.magVec(direction)
        direction = mm.vectorDivEsc(direction, radius)

        reflectDirection = reflect(intercept.normal, direction)

        viewDirection = mm.subVec(viewPosition, intercept.point)
        viewDirection = mm.normVec(viewDirection)

        intensity = max(0, min(1, mm.dotProd(reflectDirection, viewDirection))) ** intercept.obj.material.spec
        intensity *= self.intensity
        intensity *= intercept.obj.material.ks

        if radius != 0:
            intensity /= radius ** 2
        intensity = max(0, min(1, intensity))

        return [i * intensity for i in self.color]
