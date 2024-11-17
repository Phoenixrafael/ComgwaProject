import pygame, pygame.event, pygame.locals
import comgwa
from comgwa import getSpriteFromTileMap

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
dirtSprite = pygame.image.load("asset//sprite//object//object_dirt.png").convert_alpha()
holeSprite = pygame.image.load("asset//sprite//object//object_hole.png").convert_alpha()

dirtTerrain = comgwa.getTerrainDict(dirtTilemap)
wetDirtTerrain = comgwa.getTerrainDict(wetDirtTilemap)
iceTerrain = comgwa.getTerrainDict(iceTilemap)

palette = [(dirtTerrain, {'O', 'W', 'I'}, 0), (wetDirtTerrain, {'W'}), (iceTerrain, {'I'})]

'''
테스트용 코드
'''

testScene = comgwa.LevelScene(1,
                              """
                              _____
                              ___O_
                              _OIW_
                              __IO_
                              __O__
                              _____
                              """, palette, [])
scenes = [testScene]
manager = comgwa.SceneManager(scenes)
manager.run()