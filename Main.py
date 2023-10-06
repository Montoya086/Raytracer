import pygame
from pygame.locals import *

from Shape import Sphere, Plane, Disk, AABB
from Light import Ambient as AmbientLight
from Light import Directional as DirectionalLight
from Light import Point as PointLight
from RayTracer import RayTracer
import Materials.Material as Material

width = 720
height = 720

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rayTracer = RayTracer(screen)
rayTracer.envMap = pygame.image.load("Textures/desert.bmp")
rayTracer.rtClearColor(0.5, 0.5, 0.5)
rayTracer.rtColor(1, 1, 1)


rayTracer.scene.append(
    AABB(position=(-1.5, -0.75, -5), size=(1.5, 1.5, 1.5), material=Material.mars())
)
rayTracer.scene.append(
    AABB(position=(1.5, -0.75, -5), size=(1.5, 1.5, 1.5), material=Material.saturn())
)
rayTracer.scene.append(
    AABB(position=(0, 2, -8), size=(1.5, 1.5, 1.5), material=Material.earth())
)
rayTracer.scene.append(
    Disk(position=(0, 0.50, -11.9), normal=(0, 0, 1), radius=1.5, material=Material.mirror())
)
rayTracer.scene.append(
    Plane(position=(0, -1.5, 0), normal=(0, 1, 0), material=Material.floor())
)
rayTracer.scene.append(
    Plane(position=(0, 3, 0), normal=(0, -1, 0), material=Material.ceiling())
)
rayTracer.scene.append(
    Plane(position=(0, 0, -12), normal=(0, 0, -1), material=Material.opaqueCopper())
)
rayTracer.scene.append(
    Plane(position=(0, 0, 6), normal=(0, 0, 1), material=Material.ceiling())
)
rayTracer.scene.append(
    Plane(position=(-3, 0, 0), normal=(1, 0, 0), material=Material.opaqueGold())
)
rayTracer.scene.append(
    Plane(position=(3, 0, 0), normal=(-1, 0, 0), material=Material.opaqueGold())
)


#lights
rayTracer.lights.append(
    AmbientLight(intensity=0.4)
)
""" rayTracer.lights.append(
    DirectionalLight(direction=(-1, -1, -1), intensity=0.9)
) """
rayTracer.lights.append(
    PointLight(position=(0, 0, -5), intensity=2)
)

isRunning = True
rayTracer.rtClear()
rayTracer.rtRender()

print("Done!")

""" while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False """

rect = pygame.Rect(0, 0, width, height)
sub = screen.subsurface(rect)
pygame.image.save(sub, "output.png")

pygame.quit()
