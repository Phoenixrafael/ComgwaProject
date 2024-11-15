import pygame, pygame.event, pygame.locals
import comgwa
pygame.init()

'''
게임에 필요한 파일(Asset) 및 불러오기 메서드 정의
'''

stanleySprite = pygame.image.load("asset//character//stanley.png")
zeroSprite = pygame.image.load("asset//character//zero.png")


'''
테스트용 코드
'''

def testUpdate(self) :
    testSprite1 = comgwa.getSpriteFromTileMap(stanleySprite, 2, 3)
    self.surface.blit(testSprite1, (0, 0))
    testSprite2 = comgwa.getSpriteFromTileMap(zeroSprite, 2, 3)
    self.surface.blit(testSprite2, (0, 100))

testScene = comgwa.Scene("testScene", None, testUpdate, None)
scenes = [testScene]
manager = comgwa.SceneManager(scenes)
manager.run()
