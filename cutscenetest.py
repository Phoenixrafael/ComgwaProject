import pygame, pygame.event, pygame.locals
import comgwa
import sys
pygame.init()

background_image = pygame.image.load("asset/sprite/terrain/water_and_island_tiles.png")
background_image = pygame.transform.scale(background_image, (1280, 720))
lineback = pygame.image.load("asset/sprite/cutscene/lineback.png")
lineback = pygame.transform.scale(lineback, (1000, 250))

screen = pygame.display.set_mode((1280, 720))

black = (0, 0, 0)
white = (255, 255, 255)
magenta = (255, 0, 255)
red = (255, 0, 0)

person1 = comgwa.makeLine("Stanley", black, 50, (309, 521))

line1 = comgwa.makeLine("Hello!", black, 50, (640, 610))
line2 = comgwa.makeLine("Hi!", black, 50, (640, 590))
line3 = comgwa.makeLine("I'm hungry.", magenta, 60, (640, 640))
line4 = comgwa.makeLine("Wow!", black, 50, (640, 610))
line5 = comgwa.makeLine("Thank you for your efforts, Sieul!", red, 100, (640, 610))

lines = [[person1, line1], [line2, line3], [line4], [line5]]
backgrounds = [background_image] * 4

running = 1

cutscene1 = comgwa.CutScene("new_scene", lineback, backgrounds, lines)
cutscene1.run()
pygame.quit()
sys.exit()