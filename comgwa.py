import pygame, pygame.event, pygame.locals
import sys, math, inspect

'''

'''
class Scene():
    def __init__(self, name, onStart=None, onUpdate=None, onEvent=None, tick=60, displaySize=(1280, 720)):
        assert onStart == None or callable(onStart), "onStart는 함수여야합니다;; 아무것도 안 넣고 싶으면 None을 넣으세요ㅠㅠ"
        assert onUpdate == None or callable(onUpdate), "onUpdate는 함수여야 합니다;; 아무것도 안 넣고 싶으면 None을 넣으세요ㅠㅠ"
        assert onEvent == None or callable(onEvent), "onEvent는 함수여야 합니다;; 아무것도 안 넣고 싶으면 None을 넣으세요ㅠㅠ"
        assert onStart == None or list(inspect.signature(onStart).parameters.keys()) == ["self"], \
            "onStart는 onStart(self) 꼴이어야 합니다;; 멍청아;"
        assert onUpdate == None or list(inspect.signature(onUpdate).parameters.keys()) == ["self"], \
            "onUpdate는 onUpdate(self) 꼴이어야 합니다;; 바보야;"
        assert onEvent == None or list(inspect.signature(onEvent).parameters.keys()) == ["self", "event"], \
            "onEvent는 onEvent(self, event) 꼴이어야 합니다;; 빡빡아;"

        self.onStart = onStart if onStart != None else lambda self : 0
        self.onUpdate = onUpdate if onUpdate != None else lambda self : 0
        self.onEvent = onEvent if onEvent != None else lambda self, event : 0
        self.tick = tick
        self.name = name
        self.surface = pygame.display.set_mode(displaySize)
        self.manager = None
        self.stop = False

    def run(self):
        self.stop = False
        self.onStart(self)
        while True:
            self.stop = self.stop or self.onUpdate(self)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()
                else :
                    self.stop = self.stop or self.onEvent(self, event)
            if self.stop : break
            pygame.time.Clock().tick(self.tick)


'''

'''
class SceneManager():
    def __init__(self, scenes) :
        assert all([isinstance(scene, Scene) for scene in scenes]), "Scene이 아닌 원소가 존재합니다;; 똥강아지야;"
        for scene in scenes :
            scene.manager = self
        self.scenes = scenes

    def loadScene(self, thisScene, sceneName) :
        targetScene = None
        for scene in self.scenes :
            if(scene.name == sceneName) : targetScene = scene
        if(targetScene != None) :
            thisScene.stop = True
            targetScene.run()
    
    def run(self) :
        self.scenes[0].run()

def getSpriteFromTileMap(sprite, column, row, size=(32, 32), displaySize=(100, 100)) :
    croppedSprite = pygame.Surface(size)
    croppedSprite.blit(sprite, (-column * size[0], -row * size[1]))
    return pygame.transform.scale(croppedSprite, displaySize)