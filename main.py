import pygame, pygame.event, pygame.locals
import comgwa
from comgwa import getSpriteFromTileMap, getPlayerPalette

'''
게임에 필요한 파일(Asset) 불러오기
'''

pygame.init()
pygame.display.set_mode((1280, 720))

stanleySpriteTilemap = pygame.image.load("asset//sprite//character//stanley.png").convert_alpha()
zeroSpriteTilemap = pygame.image.load("asset//sprite//character//zero.png").convert_alpha()

dirtTilemap = pygame.image.load("asset//sprite//terrain//terrain_dirts.png").convert_alpha()
wetDirtTilemap = pygame.image.load("asset//sprite//terrain//terrain_wetdirts.png").convert_alpha()
iceTilemap = pygame.image.load("asset//sprite//terrain//terrain_ice.png").convert_alpha()
fenceTilemap = pygame.image.load("asset//sprite//terrain//terrain_fence.png").convert_alpha()
goalTilemap = pygame.image.load("asset//sprite//terrain//terrain_goal.png").convert_alpha()

dirtPileSprite = pygame.image.load("asset//sprite//object//object_dirt.png").convert_alpha()
holeSprite = pygame.image.load("asset//sprite//object//object_hole.png").convert_alpha()

dirtTerrain = comgwa.getTerrainDict(dirtTilemap)
wetDirtTerrain = comgwa.getTerrainDict(wetDirtTilemap)
iceTerrain = comgwa.getTerrainDict(iceTilemap)
fenceTerrain = comgwa.getTerrainDict(fenceTilemap)
goalTerrain = comgwa.getTerrainDict(goalTilemap)

lineback = pygame.image.load("asset/sprite/cutscene/lineback.png")
lineback = pygame.transform.scale(lineback, (1000, 250))

''' cutscene 만들기 '''
background_image = pygame.image.load("asset//sprite//background//bigThumb.png")
background_image = pygame.transform.scale(background_image, (1280, 720))

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
backgrounds = [[] for _ in range(len(lines))]
for i in range(len(lines)):
    backgrounds[i].append([background_image, (0, 0)])

cutscene1 = comgwa.CutScene("new_scene", lineback, backgrounds, lines, "level03")


palette = [("dirt", dirtTerrain, {'O', 'W', 'I', 'F', 'G'}, 0),
           ("wetDirt", wetDirtTerrain, {'W'}),
           ("ice", iceTerrain, {'I'}),
           ("fence", fenceTerrain, {'F'}),
           ("goal", goalTerrain, {'G'})]
dirtPalette = ("dirtPile", [(dirtPileSprite, 0)])
holePalette = ("hole", [(holeSprite, 0)])

stanleyPalette = ("stanley", stanleySpriteTilemap)
zeroPalette = ("stanley", zeroSpriteTilemap)

'''
레벨 리스트
'''

levelList = []

levelList.append(comgwa.LevelScene("level01", comgwa.Level("""
    _______
    _____O_
    _____G_
    _____O_
    _OGOOO_
    _______
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 2), (1, 4))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level02"))

levelList.append(comgwa.LevelScene("level02", comgwa.Level("""
    _______
    _OGOOO_
    _______
    _OOOOO_
    _OOOGO_
    _OOOOO_
    _______
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (3, 3))
    ], (60, 60), 0.3), holePalette, dirtPalette, "new_scene"))

levelList.append(comgwa.LevelScene("level03", comgwa.Level("""
    ________
    ___OOO__
    __OOGOO_
    _____OO_
    _____OO_
    ________
    _OOOOOO_
    _GOOO_O_
    __OO__O_
    ________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (3, 6))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level04"))

'''
테스트용 코드
'''

pygame.key.set_repeat(500, 500)

scenes = levelList + [cutscene1]

manager = comgwa.SceneManager(scenes)
manager.run()