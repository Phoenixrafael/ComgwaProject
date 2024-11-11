import pygame, pygame.event, pygame.locals
import comgwa

## comgwa 라이브러리 테스트용 코드입니다 :)

def colorScene_onUpdate(color) :
    def dec_onUpdate(self) :
        self.surface.fill(color)
    return dec_onUpdate

def colorScene_onEvent(nextSceneName) :
    def dec_onEvent(self, event) :
        if(event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_SPACE) :
            self.manager.loadScene(self, nextSceneName)
    return dec_onEvent

redScene = comgwa.Scene("redScene", None, colorScene_onUpdate((255, 0, 0)), colorScene_onEvent("greenScene"))
greenScene = comgwa.Scene("greenScene", None, colorScene_onUpdate((0, 255, 0)), colorScene_onEvent("blueScene"))
blueScene = comgwa.Scene("blueScene", None, colorScene_onUpdate((0, 0, 255)), colorScene_onEvent("redScene"))

scenes = [redScene, greenScene, blueScene]
manager = comgwa.SceneManager(scenes)
manager.run()