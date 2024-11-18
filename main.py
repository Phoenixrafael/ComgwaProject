import pygame, pygame.event, pygame.locals
import comgwa
from comgwa import getSpriteFromTileMap, getPlayerPalette

'''
게임에 필요한 파일(Asset) 및 불러오기 메서드 정의
'''

pygame.init()
pygame.display.set_mode((1280, 720))


stanleySpriteTilemap = pygame.image.load("asset//sprite//character//stanley.png").convert_alpha()
zeroSpriteTilemap = pygame.image.load("asset//sprite//character//zero.png").convert_alpha()

dirtTilemap = pygame.image.load("asset//sprite//terrain//terrain_dirts.png").convert_alpha()
wetDirtTilemap = pygame.image.load("asset//sprite//terrain//terrain_wetdirts.png").convert_alpha()
iceTilemap = pygame.image.load("asset//sprite//terrain//terrain_ice.png").convert_alpha()
fenceTilemap = pygame.image.load("asset//sprite//terrain//terrain_fence.png").convert_alpha()

dirtPileSprite = pygame.image.load("asset//sprite//object//object_dirt.png").convert_alpha()
holeSprite = pygame.image.load("asset//sprite//object//object_hole.png").convert_alpha()

dirtTerrain = comgwa.getTerrainDict(dirtTilemap)
wetDirtTerrain = comgwa.getTerrainDict(wetDirtTilemap)
iceTerrain = comgwa.getTerrainDict(iceTilemap)
fenceTerrain = comgwa.getTerrainDict(fenceTilemap)

lineback = pygame.image.load("asset/sprite/cutscene/lineback.png")
lineback = pygame.transform.scale(lineback, (1000, 250))

palette = [("dirt", dirtTerrain, {'O', 'W', 'I', 'F'}, 1),
           ("wetDirt", wetDirtTerrain, {'W'}),
           ("ice", iceTerrain, {'I'}),
           ("fence", fenceTerrain, {'F'})]
dirtPalette = ("dirtPile", [(dirtPileSprite, 0)])
holePalette = ("hole", [(holeSprite, 0)])

'''
테스트용 코드
'''

def testStart(self) :
    self.anchor = comgwa.tiktok()

def testUpdate(self) :
    level = comgwa.Level("""
    ________
    _FFFFFF_
    _FOOOOF_
    _FOOOOF_
    _FOOOOF_
    _FOOOOF_
    _FFFFFF_
    ________
    """, palette, [
        comgwa.Object(holePalette, (3, 2)),
        comgwa.Object(dirtPalette, (4, 3)),
        comgwa.Object(getPlayerPalette(zeroSpriteTilemap, (1, 2), "zero"), (5, 4), 2, True),
        comgwa.Object(getPlayerPalette(stanleySpriteTilemap, (2, 4), "stanley"), (5, 2), 0, True)
    ], (100, 100), 0.7)
    self.surface.blit(level.getLevelSurface(comgwa.tiktok() - self.anchor), (0, 0))

testScene = comgwa.Scene("testScene", testStart, testUpdate, None)
scenes = [testScene]
manager = comgwa.SceneManager(scenes)
manager.run()