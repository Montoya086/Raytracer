class Material:
    def __init__(self, diffuse=(1, 1, 1), spec=1.0, ks=0.0):
        self.diffuse = diffuse
        self.spec = spec
        self.ks = ks


def brick():
    return Material(diffuse=(1, 0.3, 0.2), spec=8, ks=0.01)


def grass():
    return Material(diffuse=(0.2, 0.8, 0.2), spec=32, ks=0.1)


def water():
    return Material(diffuse=(0.2, 0.2, 0.8), spec=256, ks=0.5)


def snow():
    return Material(diffuse=(1, 1, 1), spec=64, ks=0.5)


def stone():
    return Material(diffuse=(0.2, 0.2, 0.2), spec=32, ks=0.5)


def brigthStone():
    return Material(diffuse=(0.2, 0.2, 0.2), spec=256, ks=0.05)


def carrot():
    return Material(diffuse=(1, 0.5, 0), spec=32, ks=0.5)