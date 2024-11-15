import pygame, pygame.event, pygame.locals
import comgwa
from comgwa import getSpriteFromTileMap

'''
게임에 필요한 파일(Asset) 및 불러오기 메서드 정의
'''

stanleySprite = pygame.image.load("asset//character//stanley.png")
zeroSprite = pygame.image.load("asset//character//zero.png")
terrain1 = pygame.image.load("asset//terrain//terrain_tiles.png")
terrain2 = pygame.image.load("asset//terrain//water_and_island_tiles.png")

'''
테스트용 코드
'''

def testUpdate(self) :
    tilemap = comgwa.Tilemap(6, 6)
    tilemap.addSprite(1, 1, getSpriteFromTileMap(terrain1, 4, 3))
    tilemap.addSprite(2, 1, getSpriteFromTileMap(terrain1, 5, 0))
    tilemap.addSprite(3, 1, getSpriteFromTileMap(terrain1, 6, 0))
    tilemap.addSprite(2, 2, getSpriteFromTileMap(terrain1, 4, 2))
    tilemap.addSprite(3, 2, getSpriteFromTileMap(terrain1, 5, 2))
    tilemap.addSprite(4, 2, getSpriteFromTileMap(terrain1, 6, 3))
    self.surface.blit(tilemap.getMergedTiles(), (0, 0))

testScene = comgwa.Scene("testScene", None, testUpdate, None)
scenes = [testScene]
manager = comgwa.SceneManager(scenes)
manager.run()
