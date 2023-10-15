import pygame
from pygame.locals import *

from Shape import Sphere, Plane, Disk, AABB, Triangle, Pyramid, TextPlane, Diamond
from Light import Ambient as AmbientLight
from Light import Directional as DirectionalLight
from Light import Point as PointLight
from RayTracer import RayTracer
import Materials.Material as Material

width = 1080
height = 720

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rayTracer = RayTracer(screen)
rayTracer.envMap = pygame.image.load("Textures/room.jpg")
rayTracer.rtClearColor(0, 0, 0)
rayTracer.rtColor(1, 1, 1)
#Ceiling
rayTracer.scene.append(
    AABB(position=(0, 3, -7), size=(10, 0.1, 10), material=Material.mosaicCeiling())
)
#Floor
rayTracer.scene.append(
    AABB(position=(0, -2.5, -7), size=(10, 0.1, 10), material=Material.woodFloor())
)  
#Right wall
rayTracer.scene.append(
    AABB(position=(5, 0, -11), size=(4, 6, 10), material=Material.brickWall())
)
#Back wall
rayTracer.scene.append(
    AABB(position=(-2, 0, -12), size=(10, 6, 0.1), material=Material.brickWall())
)
#Left wall
rayTracer.scene.append(
    AABB(position=(-5, 0, -8), size=(0.1, 6, 10), material=Material.brickWall())
) 
#Box
rayTracer.scene.append(
    AABB(position=(-1, -1.75, -7), size=(1.5, 1.5, 1.5), material=Material.marmol())
)
#Glass
rayTracer.scene.append(
    AABB(position=(-1, -0.75, -7), size=(1.5, 1, 1.5), material=Material.glass())
)
#Diamond
rayTracer.scene.append(
    Diamond(position=(-1.35, -0.6, -6.65), width=0.5, height=0.5, depth=0.5, rotation=(0,0,180), material=Material.diamond())
)
#Emerald
rayTracer.scene.append(
    Pyramid(position=(-0.55, -1, -6.65), width=0.25, height=0.25, depth=0.25, rotation=(0,45,0), material=Material.emerald())
)
#Ruby
rayTracer.scene.append(
    Sphere(position=(-1, -0.97, -6.45), radius=0.15, material=Material.ruby())
) 
#Monalisa
rayTracer.scene.append(
    AABB(position=(4.15, 0, -6), size=(2, 2.5, 0.1), material=Material.monalisa())
) 
#Scream
rayTracer.scene.append(
    AABB(position=(3, 0, -9), size=(0.05, 3, 2.5), material=Material.scream())
)
#Monet
rayTracer.scene.append(
    AABB(position=(-1, 0, -11.75), size=(5, 3.5, 0.1), material=Material.monet())
)
#Vangoh
rayTracer.scene.append(
    AABB(position=(-4.9, 0, -8.5), size=(0.05, 3.5, 5), material=Material.vangoh())
)




""" rayTracer.scene.append(
    AABB(position=(-1, 0, -5), size=(1, 1, 1), material=Material.copper())
) """
""" rayTracer.scene.append(
    Sphere(position=(0, 0, -3), radius=1, material=Material.brick())
) """
""" rayTracer.scene.append(
    Triangle(vertices=((-1, -1.5, -3), (1, -1.5, -3), (0, 0.5, -4)), material=Material.mirror())
) """
""" rayTracer.scene.append(
    Pyramid(position=(0, -1.8, -7), width=1.7, height=1.7, depth=1.7, rotation=(0,45,0), material=Material.mirror())
)
rayTracer.scene.append(
    Pyramid(position=(-1.5, -1.8, -5), width=1.7, height=1.7, depth=1.7, rotation=(0,45,0), material=Material.diamond())
)
rayTracer.scene.append(
    Pyramid(position=(1.5, -1.8, -5), width=1.7, height=1.7, depth=1.7, rotation=(0,45,0), material=Material.saturn())
)
rayTracer.scene.append(
    Plane(position=(0, -1.5, 0), normal=(0, 1, 0), material=Material.floor())
) """
""" rayTracer.scene.append(
    Plane(position=(0, 3, 0), normal=(0, -1, 0), material=Material.ceiling())
)
rayTracer.scene.append(
    Plane(position=(0, 0, -12), normal=(0, 0, -1), material=Material.wall2())
)
rayTracer.scene.append(
    Plane(position=(0, 0, 6), normal=(0, 0, 1), material=Material.wall2())
)
rayTracer.scene.append(
    Plane(position=(-3, 0, 0), normal=(1, 0, 0), material=Material.wall1())
)
rayTracer.scene.append(
    Plane(position=(3, 0, 0), normal=(-1, 0, 0), material=Material.wall1())
) """





#lights
rayTracer.lights.append(
    AmbientLight(intensity=0.4)
)
""" rayTracer.lights.append(
    DirectionalLight(direction=(0.01, 0, -1), intensity=1)
) """
""" rayTracer.lights.append(
    DirectionalLight(direction=(-0.25, 0, -1), intensity=1)
) """
rayTracer.lights.append(
    PointLight(position=(1.7, -2, -3), intensity=10)
)
rayTracer.lights.append(
    PointLight(position=(-2, -2, -3), intensity=10)
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
