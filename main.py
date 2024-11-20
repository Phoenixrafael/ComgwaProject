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
    ], (60, 60), 0.3), holePalette, dirtPalette, "level03"))

levelList.append(comgwa.LevelScene("level03", comgwa.Level("""
    ________
    ___OGOO_
    _____OO_
    ______O_
    ________
    _OOOOOO_
    _OOOO_O_
    __OO__O_
    ________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (3, 6))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level04"))

'''
테스트용 코드
'''

pygame.key.set_repeat(500, 500)

manager = comgwa.SceneManager(levelList)
manager.run()