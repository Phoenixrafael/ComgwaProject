import pygame, pygame.event
from pygame.locals import *
import comgwa
from comgwa import Scene


## comgwa 라이브러리 테스트용 코드입니다 :)

def colorScene_onStart(self) :
    self.counter = 0

def colorScene_onUpdate(color) :
    def dec_onUpdate(self) :
        self.surface.fill(color)
    return dec_onUpdate

def colorScene_onEvent(nextSceneName) :
    def dec_onEvent(self, event) :
        if event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_SPACE:
            self.manager.loadScene(self, nextSceneName)
        if event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_RETURN:
            self.counter += 1
            print("Hello, enter is pushed! this is scene", self.name, "and counter is ", self.counter)
    return dec_onEvent

redScene = comgwa.Scene("redScene", colorScene_onStart, colorScene_onUpdate((255, 0, 0)), colorScene_onEvent("greenScene"))
greenScene = comgwa.Scene("greenScene", colorScene_onStart, colorScene_onUpdate((0, 255, 0)), colorScene_onEvent("blueScene"))
blueScene = comgwa.Scene("blueScene", colorScene_onStart, colorScene_onUpdate((0, 0, 255)), colorScene_onEvent("redScene"))

scenes = [redScene, greenScene, blueScene]
manager = comgwa.SceneManager(scenes)
manager.run()