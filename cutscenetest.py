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

person1 = comgwa.makeLine("Stanley", black, 35, "person", 0)
person2 = comgwa.makeLine("Zero", black, 35, "person", 0)
person3 = comgwa.makeLine("Warden", black, 35, "person", 0)

line1 = comgwa.makeLine("Hello!", black, 40, "oneline", 1)
line2 = comgwa.makeLine("안녕?", black, 40, "twoline1", 1)
line3 = comgwa.makeLine("I'm hungry.", magenta, 40, "twoline2", 1)
line4 = comgwa.makeLine("Wow!", black, 40, "oneline", 1)
line5 = comgwa.makeLine("Thanks for your efforts, Sieul!", red, 50, "oneline", 1)

lines = [[person1, line1], [person2, line2, line3], [person1, line4], [person3, line5]]
backgrounds = [background_image] * 4

running = 1

cutscene1 = comgwa.CutScene("new_scene", lineback, backgrounds, lines)
cutscene1.run()
pygame.quit()
sys.exit()