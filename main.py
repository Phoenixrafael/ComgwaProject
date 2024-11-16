import pygame, pygame.event, pygame.locals
import comgwa
from comgwa import getSpriteFromTileMap

'''
게임에 필요한 파일(Asset) 및 불러오기 메서드 정의
'''

print("???")

pygame.init()
pygame.display.set_mode((1280, 720))
stanleySprite = pygame.image.load("asset//sprite//character//stanley.png").convert_alpha()
zeroSprite = pygame.image.load("asset//sprite//character//zero.png").convert_alpha()
terrain = pygame.image.load("asset//sprite//terrain//terrain_dirts.png").convert_alpha()

terrainDict = dict()
terrainDict[(0, 0, 1, 1)] = getSpriteFromTileMap(terrain, 0, 0)
terrainDict[(0, 1, 1, 1)] = getSpriteFromTileMap(terrain, 1, 0)
terrainDict[(0, 1, 1, 0)] = getSpriteFromTileMap(terrain, 2, 0)
terrainDict[(0, 0, 1, 0)] = getSpriteFromTileMap(terrain, 3, 0)
terrainDict[(1, 0, 1, 1)] = getSpriteFromTileMap(terrain, 0, 1)
terrainDict[(1, 1, 1, 1)] = getSpriteFromTileMap(terrain, 1, 1)
terrainDict[(1, 1, 1, 0)] = getSpriteFromTileMap(terrain, 2, 1)
terrainDict[(1, 0, 1, 0)] = getSpriteFromTileMap(terrain, 3, 1)
terrainDict[(1, 0, 0, 1)] = getSpriteFromTileMap(terrain, 0, 2)
terrainDict[(1, 1, 0, 1)] = getSpriteFromTileMap(terrain, 1, 2)
terrainDict[(1, 1, 0, 0)] = getSpriteFromTileMap(terrain, 2, 2)
terrainDict[(1, 0, 0, 0)] = getSpriteFromTileMap(terrain, 3, 2)
terrainDict[(0, 0, 0, 1)] = getSpriteFromTileMap(terrain, 0, 3)
terrainDict[(0, 1, 0, 1)] = getSpriteFromTileMap(terrain, 1, 3)
terrainDict[(0, 1, 0, 0)] = getSpriteFromTileMap(terrain, 2, 3)
terrainDict[(0, 0, 0, 0)] = getSpriteFromTileMap(terrain, 3, 3)
terrainDict[0] = getSpriteFromTileMap(terrain, 2, 4)
terrainDict[1] = getSpriteFromTileMap(terrain, 4, 0)
terrainDict[2] = getSpriteFromTileMap(terrain, 5, 0)
terrainDict[3] = getSpriteFromTileMap(terrain, 6, 0)
terrainDict[4] = getSpriteFromTileMap(terrain, 7, 0)

'''
테스트용 코드
'''

def testUpdate(self) :
    self.surface.fill((255, 255, 255))
    map = comgwa.Map(
        """
                _______________________________
                ______******_______******______
                ____**********___**********____
                __***___*******_******_**_***__
                _****_**_**_******_*_*__*_****_
                _****_**_*_*_*_*_*_*_*_*__****_
                _****___**_*_*___*_*_*_**_****_
                __*********_***_**___********__
                ____***********_***********____
                ______*******************______
                ________***************________
                __________***********__________
                ____________*******____________
                ______________***______________
                _______________*_______________
                _______________________________
        """, terrainDict, (40, 40)
    )
    self.surface.blit(map.getMapSprite(), (0, 0))

testScene = comgwa.Scene("testScene", None, testUpdate, None)
scenes = [testScene]
manager = comgwa.SceneManager(scenes)
manager.run()