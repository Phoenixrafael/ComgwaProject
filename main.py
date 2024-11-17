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
dirtTilemap = pygame.image.load("asset//sprite//terrain//terrain_dirts.png").convert_alpha()
wetDirtTilemap = pygame.image.load("asset//sprite//terrain//terrain_wetdirts.png").convert_alpha()

dirtTerrain = comgwa.getTerrainDict(dirtTilemap)
wetDirtTerrain = comgwa.getTerrainDict(wetDirtTilemap)


'''
테스트용 코드
'''

def testUpdate(self) :
    self.surface.fill((255, 255, 255))
    map = comgwa.TerrainMap(
        """
        __________
        ___ooo____
        ___ooooo__
        ______oo__
        ____oooo__
        ___oo_____
        __o_o_____
        __ooo_____
        __________
        """, dirtTerrain, 1, (80, 80)
    )
    self.surface.blit(map.getMapSprite(), (0, 0))
    wetmap = comgwa.TerrainMap(
        """
        __________
        ___ooo____
        ___oooo___
        __________
        ____oooo__
        __________
        __________
        __________
        __________
        """, wetDirtTerrain, 0, (80, 80)
    )
    self.surface.blit(wetmap.getMapSprite(), (0, 0))

testScene = comgwa.Scene("testScene", None, testUpdate, None)
scenes = [testScene]
manager = comgwa.SceneManager(scenes)
manager.run()