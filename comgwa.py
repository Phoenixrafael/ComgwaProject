import pygame, pygame.event, pygame.locals
import sys, math, inspect

tiktok = lambda : pygame.time.get_ticks() / 1000
easer = lambda x : math.atan(5*(x-0.5))/(2*math.atan(5*0.5))+0.5

def smartCopy(obj, visited=None):
    """
    chatGPT를 사용하여 구현한 deepcopy의 개선 버전입니다.
    :param obj: 복사할 오브젝트를 뜻합니다.
    :param visited: 해당 오브젝트를 이미 복사했는지의 여부를 체크합니다.
    :return:
    """
    if visited is None:
        visited = {}

    if id(obj) in visited:
        return visited[id(obj)]

    if isinstance(obj, list):
        copy_list = []
        visited[id(obj)] = copy_list
        for item in obj:
            copy_list.append(smartCopy(item, visited))
        return copy_list

    if isinstance(obj, dict):
        copy_dict = {}
        visited[id(obj)] = copy_dict
        for key, value in obj.items():
            copy_dict[smartCopy(key, visited)] = smartCopy(value, visited)
        return copy_dict

    if isinstance(obj, tuple):
        copy_tuple = tuple(smartCopy(item, visited) for item in obj)
        visited[id(obj)] = copy_tuple
        return copy_tuple

    if isinstance(obj, set):
        copy_set = set()
        visited[id(obj)] = copy_set
        for item in obj:
            copy_set.add(smartCopy(item, visited))
        return copy_set

    if hasattr(obj, "__dict__"):
        copy_obj = obj.__class__.__new__(obj.__class__)
        visited[id(obj)] = copy_obj
        for key, value in obj.__dict__.items():
            setattr(copy_obj, key, smartCopy(value, visited))
        return copy_obj

    # 복사할 수 없는 경우 그냥 리턴
    return obj

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
    def __init__(self, name, lineback, backgrounds, lines, displaySize=(1280, 720)):
        self.name = name
        self.surface = pygame.display.set_mode(displaySize)
        self.lineback = lineback
        assert backgrounds, "배경이 없음"
        assert len(backgrounds) == len(lines), "배경 수와 대사 수가 불일치함"
        self.background = backgrounds #배경 목록
        self.lines = lines # 대사 목록, 시용법은 cutscenetest.py 참고
        self.lineindex = 0
        pygame.display.flip()

    def run(self):
        end = 0
        self.surface.fill((0, 0, 0))
        for image, position in self.background[self.lineindex]:
            self.surface.blit(image, position)
        pygame.display.flip()
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.locals.KEYDOWN and event.key == pygame.locals.K_SPACE:
                    if self.lineindex == len(self.lines):
                        end = 1; break
                    effect_texts, uneffect_texts = [], []
                    for idx, text_info in enumerate(self.lines[self.lineindex]):
                        if text_info[3] == 1:
                            effect_texts.append((idx, text_info))
                        else:
                            uneffect_texts.append((idx, text_info))
                    final_time = tiktok()
                    for idx, text_info in effect_texts:
                        i = 1
                        while i <= len(text_info[0]):
                            if tiktok() - final_time > 0.03:
                                text = text_info[0][:i]
                                final_time = tiktok()
                                self.surface.fill((0, 0, 0))
                                for image, position in self.background[self.lineindex]:
                                    self.surface.blit(image, position)
                                self.surface.blit(self.lineback, (160, 470))
                                for uneffect_idx, uneffect_text_info in uneffect_texts:
                                    render = uneffect_text_info[5].render(uneffect_text_info[0], True, uneffect_text_info[4])
                                    if uneffect_text_info[2] == 1:
                                        self.surface.blit(render, render.get_rect(center=uneffect_text_info[1]))
                                    else:
                                        self.surface.blit(render, render.get_rect(midleft=uneffect_text_info[1]))
                                render = text_info[5].render(text, True, text_info[4])
                                if text_info[2] == 1:
                                    self.surface.blit(render, render.get_rect(center = text_info[1]))
                                else:
                                    self.surface.blit(render, render.get_rect(midleft = text_info[1]))
                                pygame.display.flip()
                                i += 1
                        uneffect_texts.append((idx, text_info))
                    self.lineindex += 1

            if end: break

def makeLine(sentence, color, size, position, effect):
    """
    대사 text 객체를 만드는 함수, lines에 넣어서 사용
    :param string sentence: 대사 문장
    :param color: 대사의 색
    :param int size: 대사 크기
    :param position: 대사 표시 위치
    :param int effect: 1이면 한 글자씩 텍스르를 출력, 0이면 한꺼번에
    """
    type = 0
    if position == "person":
        type = 1
        position = (309, 521)
    elif position == "oneline":
        position = (230, 630)
    elif position == "twoline1":
        position = (230, 608)
    elif position == "twoline2":
        position = (230, 658)
    return [sentence, position, type, effect, color, pygame.font.Font("asset/font/Galmuri11.ttf", size)]

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


def getPlayerPalette(playerTilemapSprite, state, playerName="stanley"):
    """
    대충 머 그거 하는 함수야
    :param playerTilemapSprite: 플레이어의 타일맵을 입력하시오.
    :param (int, int) state: (걍멈춰있으면0/움직이는중이면1/땅파는중이면2, 향하는방향)
    :param string playerName: 마이 네임 이즈 스탠리 나이스 투 미츄
    :return: 플레이어 팔레트를 리턴할껄?
    """
    dir = [None, 0, 2, 1, 3][state[1]]
    li = []
    if(state[0] == 0) :
        li.append((getSpriteFromTileMap(playerTilemapSprite, 0, dir), 0))
    elif(state[0] == 1) :
        for i in range(16) :
            li.append((getSpriteFromTileMap(playerTilemapSprite, (i+1)%8, dir), 1/16 * (i+1)))
    elif(state[0] == 2) :
        for i in range(5) :
            li.append((getSpriteFromTileMap(playerTilemapSprite, i, dir+41), 1/5 * (i+1)))
        li.append((getSpriteFromTileMap(playerTilemapSprite, 0, dir), 1))
    return (playerName, li)

class Tilemap():
    """
    게임의 타일맵을 관리하는 클래스입니다.
    :param int columns: 열의 개수를 의미합니다.
    :param int rows: 열의 개수를 의미합니다.
    """
    def __init__(self, name, columns, rows, gridSize=(80, 80)) :
        self.name = name
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
    def __init__(self, name, mapStr, terrainDict, height=1, gridSize=(80, 80)):
        self.updateMap(mapStr)
        self.terrainDict = terrainDict
        self.height = height
        super().__init__(name, len(self.bitArray[0]), len(self.bitArray), gridSize)

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

class Object():
    """
    오브젝트 어쩌고 클래스
    :param string name: 이름 여따.
    :param palette: ("이름", [(스프라이트, 시간) 리스트]) 여따.
    :param (int, int) position: 위치 (열번호, 행번호) 여따. 왼쪽 위가 (0, 0)임.
    :param int moving: 안움직이면0/위로움직이면1/왼쪽움직이면2/아래쪽움직이면3/오른쪽움직이면4
    :param bool vanish: 이새끼는 움직이고 나서 사라지나요?
    """
    def __init__(self, palette, position, moving=0, vanish=False):
        self.name = palette[0]
        self.palette = palette
        self.position = position
        self.moving = moving
        self.vanish = vanish
        self.gridSize = (0, 0)
        self.columns = 0
        self.rows = 0
        self.movingTime = 0

    def setParentMap(self, parentMap):
        self.gridSize = parentMap.gridSize
        self.columns = parentMap.columns
        self.rows = parentMap.rows

    def getObjectSprite(self, deltaTime=0):
        surface = pygame.Surface((self.gridSize[0] * self.columns, self.gridSize[1] * self.rows)).convert_alpha()
        surface.fill((0, 0, 0, 0))

        sprite = None
        for p in self.palette[1] :
            if(p[1] * self.movingTime > deltaTime) :
                sprite = p[0]
                break
        if(sprite == None) : sprite = self.palette[1][-1][0]

        deltaTime = min(self.movingTime, deltaTime)
        r = 0 if (self.movingTime == 0) else 1 - deltaTime / self.movingTime
        r = easer(r)

        curDeltaPos = (0, 0)
        if(self.moving == 1) : curDeltaPos = (0, -1)
        if(self.moving == 2) : curDeltaPos = (-1, 0)
        if(self.moving == 3) : curDeltaPos = (0, +1)
        if(self.moving == 4) : curDeltaPos = (+1, 0)

        if(not (self.vanish and deltaTime == self.movingTime)) :
            surface.blit(pygame.transform.scale(sprite, self.gridSize).convert_alpha(),
                         (self.gridSize[0] * (self.position[0] + curDeltaPos[0] * r), self.gridSize[1] * (self.position[1] + curDeltaPos[1] * r)))
        return surface

class Player(Object):
    """
    플레이어 오브젝트야.
    :param playerPalette: (이름, 스프라이트)
    """
    def __init__(self, playerPalette, playerState, position) :
        self.playerPalette = playerPalette
        self.playerState = playerState
        super().__init__(getPlayerPalette(playerPalette[1], playerState, playerPalette[0]), position, (playerState[0] == 1), False)

    def updateState(self, playerState, position) :
        self.playerState = playerState
        self.palette = getPlayerPalette(self.playerPalette[1], playerState, self.playerPalette[0])
        self.position = position
        self.moving = self.playerState[1] if (playerState[0] == 1) else 0

class Level():
    def __init__(self, terrainStr, palette, objects, gridSize=(80, 80), movingTime=0.7):
        t = terrainStr.split()
        self.terrainList = []
        for p in palette :
            mapStr = ""
            for l in t :
                for c in l:
                    mapStr += c if (c in p[2]) or c == "\n" else "_"
                mapStr += "\n"
            self.terrainList.append(TerrainMap(p[0], mapStr, p[1], 0 if len(p)==3 else p[3], gridSize))
        for object in objects :
            object.setParentMap(self.terrainList[0])
            object.movingTime = movingTime
        self.objects = objects
        self.gridSize = gridSize
        self.movingTime = movingTime

    def getLevelSurface(self, deltaTime):
        mergedTile = pygame.Surface((self.gridSize[0] * self.terrainList[0].columns, self.gridSize[1] * self.terrainList[0].rows)).convert_alpha()
        mergedTile.fill((0, 0, 0, 0))
        mergedTile.fill((0, 0, 0))
        for terr in self.terrainList:
            mergedTile.blit(terr.getMapSprite(), (0, -self.gridSize[1]*0.33) if terr.name in ["fence"] else (0, 0))
        for obj in self.objects :
            mergedTile.blit(obj.getObjectSprite(deltaTime), (0, -self.gridSize[1]*0.33) if obj.name in ["stanley", "zero"] else (0, 0))
        return mergedTile

    def isWall(self, columnNo, rowNo):
        if( (not (0 <= columnNo < self.terrainList[0].columns))
                or (not (0 <= rowNo < self.terrainList[0].rows)) ) :
            return False
        for terr in self.terrainList:
            if(terr.name in ["fence"]) :
                if(terr.bitArray[rowNo][columnNo]) :
                    return True
        return False

    def isEnd(self, columnNo, rowNo):
        if( (not (0 <= columnNo < self.terrainList[0].columns))
                or (not (0 <= rowNo < self.terrainList[0].rows)) ) :
            return False
        void = True
        isTall = True
        for terr in self.terrainList:
            if(terr.name in ["dirt"]) :
                if(terr.height == 0) : isTall = False
                if(terr.bitArray[rowNo][columnNo]) :
                    void = False
        if(void) :
            return 2 if isTall else 1
        else :
            return 0

    def isHole(self, columnNo, rowNo):
        if ((not (0 <= columnNo < self.terrainList[0].columns))
                or (not (0 <= rowNo < self.terrainList[0].rows))):
            return False
        for obj in self.objects:
            if (obj.name == "hole"):
                if (obj.position == (columnNo, rowNo)):
                    return True
        return False

    def getDirtPile(self, columnNo, rowNo):
        if( (not (0 <= columnNo < self.terrainList[0].columns))
                or (not (0 <= rowNo < self.terrainList[0].rows)) ) :
            return False
        for obj in self.objects :
            if(obj.name == "dirtPile") :
                if(obj.position == (columnNo, rowNo)) :
                    return obj
        return None

    def getNextLevel(self, inp):
        nextLevel = smartCopy(self)
        i = 0
        for _ in range(len(nextLevel.objects)) :
            if(nextLevel.objects[i].vanish) :
                nextLevel.objects.remove(nextLevel.objects[i])
                i -= 1
            if(nextLevel.objects[i].name == "dirtPile" and nextLevel.objects[i].moving != 0) :
                nextLevel.objects[i].moving = 0
            i += 1
        if(inp != 5) :
            deltaPos = [None, (0, -1), (-1, 0), (0, 1), (1, 0)][inp]
            for i,obj in enumerate(nextLevel.objects) :
                if(obj.name in ["stanley", "zero"]) :
                    newPosition = (obj.position[0]+deltaPos[0], obj.position[1]+deltaPos[1])

                    if(not(nextLevel.isWall(*newPosition) or
                    nextLevel.isEnd(*newPosition) or
                    nextLevel.isHole(*newPosition))) :
                        getDirtPile = nextLevel.getDirtPile(newPosition[0], newPosition[1])
                        if(getDirtPile != None) :
                            if(not(nextLevel.isWall(obj.position[0]+deltaPos[0]*2, obj.position[1]+deltaPos[1]*2))) :
                                getDirtPile.position = (obj.position[0]+deltaPos[0]*2, obj.position[1]+deltaPos[1]*2)
                                getDirtPile.moving = (1+inp)%4+1
                                nextLevel.objects[i].updateState((1, (1+inp)%4+1), newPosition)
                            else : return None
                        else:
                            nextLevel.objects[i].updateState((1, (1+inp)%4+1), newPosition)

                        for obj1 in nextLevel.objects :
                            for obj2 in nextLevel.objects :
                                if(obj1.name == "dirtPile" and obj2.name == "hole"
                                and obj1.position == obj2.position) :
                                    obj1.vanish = True
                                    obj2.vanish = True

                        return nextLevel
                    else : return None
            return None
        else :
            pass

class LevelScene(Scene):
    def __init__(self, levelName, initialLevel):
        self.levelList = []
        self.levelQueue = []
        self.anchor = 0
        def onStart_deco(initLevel) :
            def onStart(self):
                """
                :param LevelScene self:
                """
                self.levelList = [initLevel]
                self.anchor = tiktok()

            return onStart

        def onUpdate(self):
            """
            :param LevelScene self:
            """
            sprite = self.levelList[-1].getLevelSurface(tiktok() - self.anchor)
            self.surface.blit(sprite, (self.surface.get_size()[0]/2 - sprite.get_size()[0]/2
                                       , self.surface.get_size()[1]/2 - sprite.get_size()[1]/2))
            if(len(self.levelQueue) != 0) :
                if (tiktok() - self.anchor > self.levelList[-1].movingTime) :
                    self.levelList.append(self.levelQueue[0])
                    self.anchor = tiktok()
                    self.levelQueue = self.levelQueue[1:]
            pass

        def onEvent(self, event):
            """
            :param LevelScene self:
            """
            inp = 0
            if(event.type == pygame.KEYDOWN) :
                if(event.key in [pygame.K_UP, pygame.K_w]) :
                    inp = 1
                elif(event.key in [pygame.K_LEFT, pygame.K_a]) :
                    inp = 2
                elif(event.key in [pygame.K_DOWN, pygame.K_s]) :
                    inp = 3
                elif(event.key in [pygame.K_RIGHT, pygame.K_d]) :
                    inp = 4
                elif(event.key in [pygame.K_SPACE]) :
                    inp = 5
                elif(event.key in [pygame.K_z]) :
                    if (tiktok() - self.anchor > self.levelList[-1].movingTime and len(self.levelList) > 1):
                        self.levelList.pop()
            if(inp == 0) : return
            nextLevel = (self.levelList[-1] if len(self.levelQueue) == 0 else self.levelQueue[0]).getNextLevel(inp)
            if(nextLevel != None) :
                if(tiktok() - self.anchor > self.levelList[-1].movingTime) :
                    self.levelList.append(nextLevel)
                    self.anchor = tiktok()
                else :
                    if(len(self.levelQueue) <= 1) :
                        self.levelQueue.append(nextLevel)
        super().__init__(levelName, onStart_deco(initialLevel), onUpdate, onEvent)