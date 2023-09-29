import pygame
from pygame.locals import *

from Shape import Sphere
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
    Sphere(position=(-1, -0.5, -3), radius=0.4, material=Material.glass())
)
rayTracer.scene.append(
    Sphere(position=(-1, -0.2, -5), radius=0.6, material=Material.saturn())
)
rayTracer.scene.append(
    Sphere(position=(-1, 1, -3), radius=0.4, material=Material.diamond())
)
rayTracer.scene.append(
    Sphere(position=(0, -0.5, -3), radius=0.4, material=Material.moon())
)
rayTracer.scene.append(
    Sphere(position=(0, 1, -3), radius=0.4, material=Material.mirror())
)
rayTracer.scene.append(
    Sphere(position=(1, -0.5, -3), radius=0.4, material=Material.earth())
)
rayTracer.scene.append(
    Sphere(position=(1, 1, -3), radius=0.4, material=Material.mars())
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
rayTracer.rtClear()
rayTracer.rtRender()

print("Done!")

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

rect = pygame.Rect(0, 0, width, height)
sub = screen.subsurface(rect)
pygame.image.save(sub, "output.png")

pygame.quit()
