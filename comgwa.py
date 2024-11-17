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

# todo
# class LevelScene(Scene):
#     """
#     레벨을 관리하는 씬 객체입니다.
#     :param list[(str, dict)] terrains: ㅁㄴㅇㄹ
#     """
#     def __init__(self, terrains, objects):
#         self.terrains = terrains
#         self.objects = objects
#
#     def onStart(self):
#         def onStartDeco(self):
#             pass
#         return onStartDeco
#
#     def onUpdate(self):
#         def onUpdateDeco(self):
#             pass
#         return onUpdateDeco
#
#     def onEvent(self):
#         def onEventDeco(self):
#             pass
#         return onEventDeco

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

def getSpriteFromTileMap(sprite, column, row, size=(32, 32)) :
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
    return croppedSprite

def getTerrainDict(terrainTilemapSprite) :
    """
    어쩌고저쩌고.png 파일을 실제 맵에 놓을 수 있는 파일의 형태로 바꿔주는 아이입니다. 아마도?
    :param terrainTilemapSprite: 어쩌고저쩌고.png 파일을 load한 아이를 여따 넣으세요.
    :return: terrainDict라고 불리우는 정제된 무언가를 내놓습니다.
    """
    terrain = terrainTilemapSprite
    terrainDict = dict()
    # 0으로 시작하는 아이는 빈 칸입니다.
    terrainDict[(0,)] = getSpriteFromTileMap(terrain, 5, 3)
    # 1로 시작하는 아이는 (1, W연결, A연결, S연결, D연결)을 의미합니다.
    terrainDict[(1, 0, 0, 1, 1)] = getSpriteFromTileMap(terrain, 0, 0)
    terrainDict[(1, 0, 1, 1, 1)] = getSpriteFromTileMap(terrain, 1, 0)
    terrainDict[(1, 0, 1, 1, 0)] = getSpriteFromTileMap(terrain, 2, 0)
    terrainDict[(1, 0, 0, 1, 0)] = getSpriteFromTileMap(terrain, 3, 0)
    terrainDict[(1, 1, 0, 1, 1)] = getSpriteFromTileMap(terrain, 0, 1)
    terrainDict[(1, 1, 1, 1, 1)] = getSpriteFromTileMap(terrain, 1, 1)
    terrainDict[(1, 1, 1, 1, 0)] = getSpriteFromTileMap(terrain, 2, 1)
    terrainDict[(1, 1, 0, 1, 0)] = getSpriteFromTileMap(terrain, 3, 1)
    terrainDict[(1, 1, 0, 0, 1)] = getSpriteFromTileMap(terrain, 0, 2)
    terrainDict[(1, 1, 1, 0, 1)] = getSpriteFromTileMap(terrain, 1, 2)
    terrainDict[(1, 1, 1, 0, 0)] = getSpriteFromTileMap(terrain, 2, 2)
    terrainDict[(1, 1, 0, 0, 0)] = getSpriteFromTileMap(terrain, 3, 2)
    terrainDict[(1, 0, 0, 0, 1)] = getSpriteFromTileMap(terrain, 0, 3)
    terrainDict[(1, 0, 1, 0, 1)] = getSpriteFromTileMap(terrain, 1, 3)
    terrainDict[(1, 0, 1, 0, 0)] = getSpriteFromTileMap(terrain, 2, 3)
    terrainDict[(1, 0, 0, 0, 0)] = getSpriteFromTileMap(terrain, 3, 3)
    # 2로 시작하는 아이는 (2, 좌상비어있음, 우상비어있음, 우하비어있음, 좌하비어있음)을 의미합니다.
    terrainDict[(2, 1)] = getSpriteFromTileMap(terrain, 4, 0)
    terrainDict[(2, 2)] = getSpriteFromTileMap(terrain, 5, 0)
    terrainDict[(2, 3)] = getSpriteFromTileMap(terrain, 6, 0)
    terrainDict[(2, 4)] = getSpriteFromTileMap(terrain, 7, 0)
    terrainDict[(3, 0)] = getSpriteFromTileMap(terrain, 4, 3)
    # 3, 4으로 시작하는 아이는 (연결중이면3아니면4, 좌측연결여부, 우측연결여부)을 의미합니다.
    terrainDict[(3, 0, 0)] = getSpriteFromTileMap(terrain, 7, 2)
    terrainDict[(3, 0, 1)] = getSpriteFromTileMap(terrain, 4, 2)
    terrainDict[(3, 1, 0)] = getSpriteFromTileMap(terrain, 6, 2)
    terrainDict[(3, 1, 1)] = getSpriteFromTileMap(terrain, 5, 2)
    terrainDict[(4, 0, 0)] = getSpriteFromTileMap(terrain, 7, 1)
    terrainDict[(4, 0, 1)] = getSpriteFromTileMap(terrain, 4, 1)
    terrainDict[(4, 1, 0)] = getSpriteFromTileMap(terrain, 6, 1)
    terrainDict[(4, 1, 1)] = getSpriteFromTileMap(terrain, 5, 1)
    return terrainDict

class Tilemap():
    """
    게임의 타일맵을 관리하는 클래스입니다.
    :param int columns: 열의 개수를 의미합니다.
    :param int rows: 열의 개수를 의미합니다.
    """
    def __init__(self, columns, rows, gridSize=(80, 80)) :
        self.columns = columns
        self.rows = rows
        self.spriteList = [[[] for i in range(rows)] for j in range(columns)]
        self.gridSize = gridSize

    def getMapSprite(self):
        mergedTile = pygame.Surface((self.gridSize[0] * self.columns, self.gridSize[1] * self.rows)).convert_alpha()
        mergedTile.fill((0, 0, 0, 0))
        for i in range(self.rows) :
            for j in range(self.columns) :
                for sprite in self.spriteList[j][i] :
                    mergedTile.blit(pygame.transform.scale(sprite, self.gridSize).convert_alpha(), (j * self.gridSize[0], i * self.gridSize[1]))
        return mergedTile

    def addSprite(self, columnNo, rowNo, sprite):
        self.spriteList[columnNo][rowNo].append(sprite)

    def deleteSprite(self, columnNo, rowNo, sprite):
        try :
            self.spriteList[columnNo][rowNo].remove(sprite)
        except :
            print("Warning : couldn't remove a sprite")

    def clearSprites(self):
        self.spriteList = [[[] for i in range(self.rows)] for j in range(self.columns)]

class TerrainMap(Tilemap):
    """
    게임의 지형(같은 애들끼리 연결되서 막 난리나는 애들)을 관리하는 클래스일껄?
    :param string mapStr: _는 빈 칸, 나머지 아무 문자는 채운 칸을 의미할껄?
    :param dictionary terrainDict: 그냥 내가 위에 만들어놓은 어쩌고Terrain으로 끝나는 그거 넣으면 될껄?
    :param int height: 얼마나 높게 띄울건지 정하는거일껄?
    :param (int, int) gridSize: 한 칸이 어느정도 사이즈로 표시될지일껄?
    """
    def __init__(self, mapStr, terrainDict, height=1, gridSize=(80, 80)):
        self.updateMap(mapStr)
        self.terrainDict = terrainDict
        self.height = height
        super().__init__(len(self.bitArray[0]), len(self.bitArray), gridSize)

    def updateMap(self, mapStr):
        lines = [i for i in list(mapStr.split()) if i != ""]
        self.bitArray = []
        for line in lines :
            bits = []
            for char in line :
                bits.append(0 if char=='_' else 1)
            self.bitArray.append(bits)

    def getBit(self, i, j):
        if(not (0 <= i < len(self.bitArray))) : return 0
        if(not (0 <= j < len(self.bitArray[0]))) : return 0
        return self.bitArray[i][j]

    def placeSprite(self, i, j):
        if(self.getBit(i, j)) :
            if(self.height) : self.addSprite(j, i, self.terrainDict[(3, 0)])
            self.addSprite(j, i, self.terrainDict[(1, self.getBit(i - 1, j), self.getBit(i, j - 1),
                                                   self.getBit(i+1, j), self.getBit(i, j+1))])
            if(self.getBit(i-1, j) and self.getBit(i, j-1) and (not self.getBit(i-1, j-1))) :
                self.addSprite(j, i, self.terrainDict[(2, 1)])
            if(self.getBit(i+1, j) and self.getBit(i, j-1) and (not self.getBit(i+1, j-1))) :
                self.addSprite(j, i, self.terrainDict[(2, 4)])
            if(self.getBit(i+1, j) and self.getBit(i, j+1) and (not self.getBit(i+1, j+1))) :
                self.addSprite(j, i, self.terrainDict[(2, 3)])
            if(self.getBit(i-1, j) and self.getBit(i, j+1) and (not self.getBit(i-1, j+1))) :
                self.addSprite(j, i, self.terrainDict[(2, 2)])
        elif(self.height) :
            for k in range(1, self.height+1) :
                if(self.getBit(i-k, j)) :
                    self.addSprite(j, i, self.terrainDict[(3 if (self.height == k) else 4, self.getBit(i - k, j - 1), self.getBit(i - k, j + 1))])

    def getMapSprite(self):
        self.clearSprites()
        for i in range(len(self.bitArray)) :
            for j in range(len(self.bitArray[0])) :
                self.addSprite(j, i, self.terrainDict[(0,)])
                self.placeSprite(i, j)
        return super().getMapSprite()