import pygame, pygame.event, pygame.locals
import comgwa
import sys
pygame.init()

background_image = pygame.image.load("asset//sprite//background//bigThumb.png")
background_image = pygame.transform.scale(background_image, (1280, 720))
lineback = pygame.image.load("asset/sprite/cutscene/lineback.png")
lineback = pygame.transform.scale(lineback, (1000, 250))

screen = pygame.display.set_mode((1280, 720))


lines = [[person1, line1], [person2, line2, line3], [person1, line4], [person3, line5]]
backgrounds = [[] for _ in range(len(lines))]
for i in range(len(lines)):
    backgrounds[i].append([background_image, (0, 0)])

running = 1

cutscene1 = comgwa.CutScene("new_scene", lineback, backgrounds, lines, "no")
cutscene1.run()
pygame.quit()
sys.exit()