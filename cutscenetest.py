import pygame, pygame.event, pygame.locals
import comgwa
import sys
pygame.init()

background_image = pygame.image.load("asset/sprite/terrain/water_and_island_tiles.png")
background_image = pygame.transform.scale(background_image, (1280, 720))
screen = pygame.display.set_mode((1280, 720))
running = 1

white = (255, 255, 255)
magenta = (255, 0, 255)
red = (255, 0, 0)

line1 = comgwa.makeLine("Hello!", white, 50, (640, 500))
line2 = comgwa.makeLine("Hi!", white, 50, (640, 500))
line3 = comgwa.makeLine("I'm hungry.", magenta, 60, (640, 600))
line4 = comgwa.makeLine("Wow!", white, 50, (640, 500))
line5 = comgwa.makeLine("Thank you for your efforts, Sieul!", red, 100, (640, 500))

lines = [[line1], [line2, line3], [line4], [line5]]

cutscene1 = comgwa.CutScene("new_scene", background_image, lines)
cutscene1.run()
pygame.quit()
sys.exit()