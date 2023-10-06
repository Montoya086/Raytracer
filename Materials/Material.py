import pygame
OPAQUE = 0
REFLECTIVE = 1
TRANSPARENT = 2

class Material:
    def __init__(self, diffuse=(1, 1, 1), spec=1.0, ks=0.0, ior= 1.0,matType=OPAQUE, texture = None):
        self.diffuse = diffuse
        self.spec = spec
        self.ks = ks
        self.ior = ior
        self.matType = matType
        self.texture = texture

def glass():
    return Material(diffuse=(0.9, 0.9, 0.9), spec=64, ks=0.15, ior=1.5, matType=TRANSPARENT)


def diamond():
    return Material(diffuse=(0.6, 0.6, 0.9), spec=128, ks=0.20, ior=2.417, matType=TRANSPARENT)


def earth():
    return Material(texture=pygame.image.load("Textures/earth.bmp"))


def mars():
    return Material(texture=pygame.image.load("Textures/mars.bmp"))


def saturn():
    return Material(texture=pygame.image.load("Textures/saturn.bmp"))


def moon():
    return Material(texture=pygame.image.load("Textures/moon.bmp"), spec=32, ks=0.1, matType=REFLECTIVE)


def mirror():
    return Material(diffuse=(0.9, 0.9, 0.9), spec=64, ks=0.2, matType=REFLECTIVE)


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


def opaqueGold():
    return Material(diffuse=(1, 0.8, 0.2), spec=32, ks=0.5)


def opaqueCopper():
    return Material(diffuse=(0.9, 0.5, 0.3), spec=32, ks=0.5)


def ceiling():
    return Material(diffuse=(0.8, 0.8, 0.8), spec=32, ks=0.5)


def floor():
    return Material(diffuse=(0.5, 0.5, 0.5), spec=32, ks=0.5, matType=REFLECTIVE)