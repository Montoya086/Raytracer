import pygame
from pygame.locals import *

from Shape import Sphere
from Light import Ambient as AmbientLight
from Light import Directional as DirectionalLight
from Light import Point as PointLight
from RayTracer import RayTracer
import Materials.Material as Material

width = 300
height = 300

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rayTracer = RayTracer(screen)
rayTracer.rtClearColor(0, 0, 0)
rayTracer.rtColor(1, 1, 1)

#snow
rayTracer.scene.append(
    Sphere(position=(0, -1.5, -5), radius=1, material=Material.snow())
)
rayTracer.scene.append(
    Sphere(position=(0, -0.3, -5), radius=0.9, material=Material.snow())
)
rayTracer.scene.append(
    Sphere(position=(0, 0.7, -5), radius=0.7, material=Material.snow())
)
#buttons
rayTracer.scene.append(
    Sphere(position=(0, 0, -2), radius=0.05, material=Material.stone())
)
rayTracer.scene.append(
    Sphere(position=(0, -0.7, -2), radius=0.08, material=Material.stone())
)
rayTracer.scene.append(
    Sphere(position=(0, -0.35, -2), radius=0.065, material=Material.stone())
)
#mouth
rayTracer.scene.append(
    Sphere(position=(0.03, 0.25, -2), radius=0.02, material=Material.stone())
)
rayTracer.scene.append(
    Sphere(position=(-0.03, 0.25, -2), radius=0.02, material=Material.stone())
)
rayTracer.scene.append(
    Sphere(position=(0.08, 0.275, -2), radius=0.02, material=Material.stone())
)
rayTracer.scene.append(
    Sphere(position=(-0.08, 0.275, -2), radius=0.02, material=Material.stone())
)
#carrot
rayTracer.scene.append(
    Sphere(position=(0, 0.35, -2), radius=0.05, material=Material.carrot())
)
#eyes
rayTracer.scene.append(
    Sphere(position=(0.1, 0.4, -2), radius=0.04, material=Material.brigthStone())
)
rayTracer.scene.append(
    Sphere(position=(-0.1, 0.4, -2), radius=0.04, material=Material.brigthStone())
)

#lights
rayTracer.lights.append(
    AmbientLight(intensity=0.5)
)
rayTracer.lights.append(
    DirectionalLight(direction=(-1, -1, -1), intensity=0.3)
)
rayTracer.lights.append(
    PointLight(position=(2.5, 0, -5), intensity=1)
)

isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

    rayTracer.rtClear()
    rayTracer.rtRender()
    pygame.display.flip()

pygame.quit()
