import pygame, pygame.event, pygame.locals
import comgwa
from comgwa import getSpriteFromTileMap

'''
게임에 필요한 파일(Asset) 및 불러오기 메서드 정의
'''

pygame.init()
pygame.display.set_mode((1280, 720))
stanleySprite = pygame.image.load("asset//character//stanley.png").convert_alpha()
zeroSprite = pygame.image.load("asset//character//zero.png").convert_alpha()
terrain1 = pygame.image.load("asset//terrain//terrain_tiles.png").convert_alpha()
terrain2 = pygame.image.load("asset//terrain//water_and_island_tiles.png").convert_alpha()


'''
테스트용 코드
'''

def testUpdate(self) :
    self.surface.fill((255, 255, 255))
    tilemap = comgwa.Tilemap(16, 9)
    for i in range(16):
        for j in range(9):
            tilemap.addSprite(i, j, getSpriteFromTileMap(terrain1, 5, 1))
    tilemap.addSprite(1, 1, getSpriteFromTileMap(terrain1, 4, 3))
    tilemap.addSprite(2, 1, getSpriteFromTileMap(terrain1, 5, 0))
    tilemap.addSprite(3, 1, getSpriteFromTileMap(terrain1, 6, 0))
    tilemap.addSprite(2, 2, getSpriteFromTileMap(terrain1, 4, 2))
    tilemap.addSprite(3, 2, getSpriteFromTileMap(terrain1, 5, 2))
    tilemap.addSprite(4, 2, getSpriteFromTileMap(terrain1, 6, 3))
    tilemap.addSprite(1, 2, getSpriteFromTileMap(terrain1, 0, 12))
    tilemap.addSprite(2, 3, getSpriteFromTileMap(terrain1, 0, 12))
    tilemap.addSprite(3, 3, getSpriteFromTileMap(terrain1, 1, 12))
    tilemap.addSprite(4, 3, getSpriteFromTileMap(terrain1, 2, 12))
    self.surface.blit(tilemap.getMergedTiles(), (0, 0))

testScene = comgwa.Scene("testScene", None, testUpdate, None)
scenes = [testScene]
manager = comgwa.SceneManager(scenes)
manager.run()
