import pygame, pygame.event, pygame.locals
import comgwa
from comgwa import getSpriteFromTileMap, getPlayerPalette

pygame.init()
pygame.display.set_mode((1280, 720))

'''
게임에 필요한 파일(Asset) 불러오기
'''

# 캐릭터 이미지
stanleySpriteTilemap = pygame.image.load("asset//sprite//character//stanley.png").convert_alpha()
zeroSpriteTilemap = pygame.image.load("asset//sprite//character//zero.png").convert_alpha()

#지형 타일맵
dirtTilemap = pygame.image.load("asset//sprite//terrain//terrain_dirts.png").convert_alpha()
wetDirtTilemap = pygame.image.load("asset//sprite//terrain//terrain_wetdirts.png").convert_alpha()
iceTilemap = pygame.image.load("asset//sprite//terrain//terrain_ice.png").convert_alpha()
fenceTilemap = pygame.image.load("asset//sprite//terrain//terrain_fence.png").convert_alpha()
goalTilemap = pygame.image.load("asset//sprite//terrain//terrain_goal.png").convert_alpha()

#오브젝트 스프라이트
dirtPileSprite = pygame.image.load("asset//sprite//object//object_dirt.png").convert_alpha()
holeSprite = pygame.image.load("asset//sprite//object//object_hole.png").convert_alpha()

dirtTerrain = comgwa.getTerrainDict(dirtTilemap)
wetDirtTerrain = comgwa.getTerrainDict(wetDirtTilemap)
iceTerrain = comgwa.getTerrainDict(iceTilemap)
fenceTerrain = comgwa.getTerrainDict(fenceTilemap)
goalTerrain = comgwa.getTerrainDict(goalTilemap)

counterSprite = pygame.image.load("asset//sprite//counter.png")

lineback = pygame.image.load("asset/sprite/cutscene/lineback.png")
lineback = pygame.transform.scale(lineback, (1000, 250))

#배경 이미지
mountain = pygame.image.load("asset/sprite/background/bigThumb.png")
bus = pygame.image.load("asset/sprite/background/bus.png")
camp1 = pygame.image.load("asset/sprite/background/camp1.png")
camp2 = pygame.image.load("asset/sprite/background/camp2.png")
camp3 = pygame.image.load("asset/sprite/background/camp3.png")
lawcourt = pygame.image.load("asset/sprite/background/lawCourt.png")
town = pygame.image.load("asset/sprite/background/town.png")

mountain = comgwa.makeImage(pygame.transform.scale(mountain, (1280, 720)), 0)
bus = comgwa.makeImage(pygame.transform.scale(bus, (1280, 720)), 0)
camp1 = comgwa.makeImage(pygame.transform.scale(camp1, (1280, 720)), 0)
camp2 = comgwa.makeImage(pygame.transform.scale(camp2, (1280, 720)), 0)
camp3 = comgwa.makeImage(pygame.transform.scale(camp3, (1280, 720)), 0)
lawcourt = comgwa.makeImage(pygame.transform.scale(lawcourt, (1280, 720)), 0)
town = comgwa.makeImage(pygame.transform.scale(town, (1280, 720)), 0)

# 인물 이미지
stanley_normal = pygame.image.load("asset/sprite/cutscene/character/stanleynormal.png")
stanley_sad = pygame.image.load("asset/sprite/cutscene/character/stanleysad.png")
stanley_happy = pygame.image.load("asset/sprite/cutscene/character/stanleyhappy.png")
stanley_angry = pygame.image.load("asset/sprite/cutscene/character/stanleyangry.png")
zero_normal = pygame.image.load("asset/sprite/cutscene/character/zeronormal.png")
zero_sad = pygame.image.load("asset/sprite/cutscene/character/zerosad.png")
zero_happy = pygame.image.load("asset/sprite/cutscene/character/zerohappy.png")
zero_angry = pygame.image.load("asset/sprite/cutscene/character/zeroangry.png")

image_size = (450, 450)

# 인물 좌우반전 이미지 생성
stanley_normal_left = comgwa.makeImage(pygame.transform.scale(stanley_normal, image_size), 1)
stanley_normal_right = comgwa.makeImage(pygame.transform.scale(stanley_normal, image_size), 2)
stanley_sad_left = comgwa.makeImage(pygame.transform.scale(stanley_sad, image_size), 1)
stanley_sad_right = comgwa.makeImage(pygame.transform.scale(stanley_sad, image_size), 2)
stanley_happy_left = comgwa.makeImage(pygame.transform.scale(stanley_happy, image_size), 1)
stanley_happy_right = comgwa.makeImage(pygame.transform.scale(stanley_happy, image_size), 2)
stanley_angry_left = comgwa.makeImage(pygame.transform.scale(stanley_angry, image_size), 1)
stanley_angry_right = comgwa.makeImage(pygame.transform.scale(stanley_angry, image_size), 2)
zero_normal_left = comgwa.makeImage(pygame.transform.scale(zero_normal, image_size), 1)
zero_normal_right = comgwa.makeImage(pygame.transform.scale(zero_normal, image_size), 2)
zero_sad_left = comgwa.makeImage(pygame.transform.scale(zero_sad, image_size), 1)
zero_sad_right = comgwa.makeImage(pygame.transform.scale(zero_sad, image_size), 2)
zero_happy_left = comgwa.makeImage(pygame.transform.scale(zero_happy, image_size), 1)
zero_happy_right = comgwa.makeImage(pygame.transform.scale(zero_happy, image_size), 2)
zero_angry_left = comgwa.makeImage(pygame.transform.scale(zero_angry, image_size), 1)
zero_angry_right = comgwa.makeImage(pygame.transform.scale(zero_angry, image_size), 2)

''' cutscene 만들기 '''

cutscenes = []
screen = pygame.display.set_mode((1280, 720))

cutscenes.append(comgwa.CutScene("intro", lineback,
[[town, zero_normal_left],
            [town, stanley_normal_right],
            [town, stanley_happy_right],
            [town, stanley_angry_right],
            [town, stanley_angry_right],
            [town, stanley_angry_right],
            [town, stanley_angry_right],
            [town, stanley_sad_right],
            [lawcourt],
            [lawcourt],
            [lawcourt, stanley_sad_left],
            [lawcourt, stanley_happy_left],
            [bus],
            [bus, stanley_normal_left]],
comgwa.makeScript('''
black/40/Zero/
헉...헉...
일단 신발을 여기 두자..
#
black/40/Stanley/
어? 이 신발 뭐지?
#
black/40/Stanley/
주워 가면 아버지의 구두 냄새 제거 연구에
도움이 되겠지? 주워 가야...
#
black/40/Police/
Clyde Livingstone의 신발을 훔친 범인이다!
#
black/32/Police/
당신은 묵비권을 행사할 수  있으며
당신이 한 발언은 법정에서 불리하게 작용할 수 있습니다.
#
black/32/Police/
당신은 변호인을 선임할 수 있으며,
질문을 받을 때 변호인에게 대신 발언하게 할 수 있습니다.
#
black/32/Police/
변호인을 선임하지 못할 경우, 국선변호안이 선임될 것입니다.
이 권리가 있음을 인지했습니까?
#
black/40/Stanley/
네... 인지했습니다..
#
white/50/Narration/
그렇게 법정으로 가게 된 Stanley...
#
black/40/Judge/
Stanley, 그래서 Camp Green Lake와
감옥 중 어디를 가겠니?
#
black/40/Stanley/
'Camp Green Lake? 재밌어 보이는데?'
#
black/40/Stanley/
Camp Green Lake로 갈게요!
#
white/50/Narration/
깊이 잠에 들었던 Stanley...
#
black/40/Stanley/
여...여기가 어디지?
버..버스잖아?



'''), "level01"))


palette = [("dirt", dirtTerrain, {'O', 'W', 'I', 'F', 'G'}, 0),
           ("wetDirt", wetDirtTerrain, {'W'}),
           ("ice", iceTerrain, {'I'}),
           ("fence", fenceTerrain, {'F'}),
           ("goal", goalTerrain, {'G'})]
dirtPalette = ("dirtPile", [(dirtPileSprite, 0)])
holePalette = ("hole", [(holeSprite, 0)])

stanleyPalette = ("stanley", stanleySpriteTilemap)
zeroPalette = ("stanley", zeroSpriteTilemap)

'''
레벨 리스트
'''

levelList = []

levelList.append(comgwa.LevelScene("level01", comgwa.Level("""
    _______
    _______
    _____G_
    _____O_
    _OOGOO_
    _______
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 2), (1, 4))
    ], (60, 60), 0.2), holePalette, dirtPalette, "level02"))

levelList.append(comgwa.LevelScene("level02", comgwa.Level("""
    _________
    _OOOOOOO_
    _O__OOOO_
    _O__OOOO_
    _G_____G_
    _______O_
    _OOOOOOO_
    _________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 2), (1, 6)),
        comgwa.Object(dirtPalette, (3, 6)),
        comgwa.Object(holePalette, (5, 6)),
        comgwa.Object(holePalette, (3, 1)),
    ], (60, 60), 0.3), holePalette, dirtPalette, "level03"))

levelList.append(comgwa.LevelScene("level03", comgwa.Level("""
    ______
    _OGOO_
    ______
    _O____
    _OOOO_
    _OOOO_
    ______
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (4, 5))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level04"))

levelList.append(comgwa.LevelScene("level04", comgwa.Level("""
    ____________
    ____________
    _OOOOO_OOGO_
    __OOO_______
    ____________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (2, 2))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level05"))

levelList.append(comgwa.LevelScene("level05", comgwa.Level("""
    ____________
    __OOO_______
    _OOOOO__OGO_
    __OO________
    ___OO_______
    ___OO_______
    ___OO_______
    ___O________
    ____________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 2), (1, 2))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level06"))

levelList.append(comgwa.LevelScene("level06", comgwa.Level("""
    ________
    ___OOO__
    __OOGOO_
    _____OO_
    _____OO_
    ________
    _OOOOOO_
    _GOOO_O_
    ______O_
    ________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (6, 8))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level07"))

levelList.append(comgwa.LevelScene("level07", comgwa.Level("""
    _______
    _OO____
    _OOFOO_
    _OGGGF_
    _OOOGO_
    _OOOFO_
    _OOOOO_
    _______
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (1, 1))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level08"))

levelList.append(comgwa.LevelScene("level08", comgwa.Level("""
    _________
    __OO_____
    __OOOOOO_
    _OGOFOOO_
    _OFFFGOO_
    _____GO__
    ____OOOO_
    ____OOOO_
    _________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (7, 6))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level09"))

levelList.append(comgwa.LevelScene("level09", comgwa.Level("""
    _____________
    _FFFFFFFF__O_
    _FOOOOOOF__O_
    _FOFFFFOF__O_
    _FOOOOOOF__O_
    _FFFOOOO___O_
    ___FFFOO___O_
    _OOOOFOO___O_
    _OFFOFFO___O_
    _OOOOOOO___G_
    ______OO___O_
    _____________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (6, 6))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level10"))

levelList.append(comgwa.LevelScene("level10", comgwa.Level("""
    __OOO____
    OOO__O___
    OF_OOO___
    OFFFOOOOO
    OGO_O_O_O
    ___OO_O_O
    G__OO_OOO
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (3, 6))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level11"))

levelList.append(comgwa.LevelScene("level11", comgwa.Level("""
    _______
    _OOOOO_
    _OOOOO_
    _OGOOO_
    _______
    _______
    _OOOGO_
    _______
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (1, 1))
    ], (60, 60), 0.3, comgwa.Counter(counterSprite, 3, True, False)), holePalette, dirtPalette, "level12"))

levelList.append(comgwa.LevelScene("level12", comgwa.Level("""
    _______
    _IIOOO_
    _OIOOO_
    _OOOOO_
    _OOOOO_
    _OOOOO_
    _OOGOO_
    _______
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (1, 1))
    ], (60, 60), 0.3, comgwa.Counter(counterSprite, 3, True, False)), holePalette, dirtPalette, "level13"))
levelList[-1].run()
'''
테스트용 코드
'''

pygame.key.set_repeat(500, 500)

scenes = cutscenes + levelList

manager = comgwa.SceneManager(scenes)
manager.run()