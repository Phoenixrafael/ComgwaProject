import pygame, pygame.event, pygame.locals
import sys, math, inspect

class Scene():
    """
    게임의 한 장면을 맡는 Scene이라는 객체란다.
    Scene에서 변수 선언은 전역변수를 쓰지 말고, 모두 self.~~와 같은 형태로 선언해줘.
    :param string name: Scene의 이름을 정의해. 얘는 SceneManager에서 원하는 Scene을 불러올 때 사용한단다.
    :param callable onStart: Scene이 처음 실행될 때 실행될 함수야. 주로 변수 초기화와 같은 기능을 할 때 쓰렴.
    :param callable onUpdate: Scene이 실행되는 동안 매 틱마다 실행되는 함수란다.
    :param callable onEvent: Scene에서 키보드를 누르거나 마우스를 누르는 등 이벤트가 있을 때 호출되는 함수란다.
    :param int tick: 해당 Scene에서 사용할 fps를 나타내는 변수야. 기본값은 60이란다.
    :param (int, int) displaySize: 해당 Scene의 화면 크기를 나타내는 변수야. 기본값은 (1280, 720)이란다.
    """
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
                else:
                    self.stop = self.stop or self.onEvent(self, event)
            if self.stop: break
            pygame.time.Clock().tick(self.tick)


class SceneManager():
    """
    여러 개의 Scene들을 합쳐서 관리하는 개쩌는 객체입니다.
    :param list[Scene] scenes: 관리할 Scene 객체의 리스트입니다.
    """
    def __init__(self, scenes):
        assert all([isinstance(scene, Scene) for scene in scenes]), "Scene이 아닌 원소가 존재합니다;; 똥강아지야;"
        for scene in scenes:
            scene.manager = self
        self.scenes = scenes

    def loadScene(self, thisScene, sceneName):
        targetScene = None
        for scene in self.scenes:
            if(scene.name == sceneName): targetScene = scene
        if targetScene != None:
            thisScene.stop = True
            targetScene.run()
    
    def run(self) :
        self.scenes[0].run()

class CutScene(Scene):
    def __init__(self, name, background, lines, displaySize=(1280, 720)):
        self.name = name
        self.surface = pygame.display.set_mode(displaySize)
        self.background = background
        self.surface.blit(background, (0, 0))
        self.lines = lines # 대사 목록, 시용법은 cutscenetest.py 참고
        self.lineindex = 0
        pygame.display.flip()

    def run(self):
        end = 0
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_SPACE:
                    if self.lineindex == len(self.lines):
                        end = 1; break
                    self.surface.fill((0, 0, 0))
                    self.surface.blit(self.background, (0, 0))
                    for text_info in self.lines[self.lineindex]:
                        text = text_info[0]
                        text_rect = text.get_rect(center = text_info[1])
                        self.surface.blit(text, text_rect)
                    pygame.display.flip()
                    self.lineindex += 1

            if end: break

def makeLine(sentence, color, size, position):
    """
    대사 text 객체를 만드는 함수, lines에 넣어서 사용
    :param string sentence: 얘는 말할 대사를 의미하는듯 하구나.
    :param color: 대사의 색을 의미하는듯 하구나.
    :param int size: 대사의 크기를 의미하는듯 하구나.
    :param (int, int) position: 대사를 표시할 위치를 의마하는듯 하구나.
    """
    font_size = pygame.font.Font(None, size)
    return [font_size.render(sentence, True, color), position]

def getSpriteFromTileMap(sprite, column, row, size=(32, 32), displaySize=(80, 80)) :
    """
    타일맵 스프라이트에서 특정 열과 행에 있는 이미지만 잘라 리턴하는 함수란다.
    :param sprite: 자를 타일맵 스프라이트를 지정해.
    :param int column: 몇번째 열의 스프라이트를 가져올지 지정해. (가장 왼쪽이 0)
    :param int row: 몇번째 행의 스프라이트를 가져올지 지정해. (가장 위쪽이 0)
    :param (int, int) size: 타일맵의 스프라이트 크기를 지정해. 기본값인 (32, 32)에서 바뀔 일은 딱히 없을거야.
    :return 자른 이미지를 리턴한단다.
    """
    croppedSprite = pygame.Surface(size).convert_alpha()
    croppedSprite.fill((0, 0, 0, 0))
    croppedSprite.blit(sprite, (-column * size[0], -row * size[1]))
    return pygame.transform.scale(croppedSprite, displaySize)

class Tilemap():
    def __init__(self, columns, rows, gridSize=(80, 80)) :
        self.columns = columns
        self.rows = rows
        self.spriteList = [[[] for i in range(rows)] for j in range(columns)]
        self.gridSize = gridSize

    def getMergedTiles(self):
        mergedTile = pygame.Surface((self.gridSize[0] * self.columns, self.gridSize[1] * self.rows))
        for i in range(self.rows) :
            for j in range(self.columns) :
                for sprite in self.spriteList[j][i] :
                    mergedTile.blit(sprite, (j * self.gridSize[0], i * self.gridSize[1]))
        return mergedTile

    def addSprite(self, columnNo, rowNo, sprite):
        self.spriteList[columnNo][rowNo].append(sprite)

    def deleteSprite(self, columnNo, rowNo, sprite):
        try :
            self.spriteList[columnNo][rowNo].remove(sprite)
        except :
            print("Warning : couldn't remove a sprite")