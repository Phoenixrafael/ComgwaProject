import pygame, pygame.event, pygame.locals
import comgwa
from comgwa import getSpriteFromTileMap, getPlayerPalette

'''
게임에 필요한 파일(Asset) 불러오기
'''

pygame.init()
pygame.display.set_mode((1280, 720))

stanleySpriteTilemap = pygame.image.load("asset//sprite//character//stanley.png").convert_alpha()
zeroSpriteTilemap = pygame.image.load("asset//sprite//character//zero.png").convert_alpha()

dirtTilemap = pygame.image.load("asset//sprite//terrain//terrain_dirts.png").convert_alpha()
wetDirtTilemap = pygame.image.load("asset//sprite//terrain//terrain_wetdirts.png").convert_alpha()
iceTilemap = pygame.image.load("asset//sprite//terrain//terrain_ice.png").convert_alpha()
fenceTilemap = pygame.image.load("asset//sprite//terrain//terrain_fence.png").convert_alpha()
goalTilemap = pygame.image.load("asset//sprite//terrain//terrain_goal.png").convert_alpha()

dirtPileSprite = pygame.image.load("asset//sprite//object//object_dirt.png").convert_alpha()
holeSprite = pygame.image.load("asset//sprite//object//object_hole.png").convert_alpha()

dirtTerrain = comgwa.getTerrainDict(dirtTilemap)
wetDirtTerrain = comgwa.getTerrainDict(wetDirtTilemap)
iceTerrain = comgwa.getTerrainDict(iceTilemap)
fenceTerrain = comgwa.getTerrainDict(fenceTilemap)
goalTerrain = comgwa.getTerrainDict(goalTilemap)

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
stanley_normal = pygame.image.load("asset/sprite/cutscene/character/stanley-normal.png")
stanley_sad = pygame.image.load("asset/sprite/cutscene/character/stanley-sad.png")
stanley_happy = pygame.image.load("asset/sprite/cutscene/character/stanley-happy.png")
stanley_angry = pygame.image.load("asset/sprite/cutscene/character/stanley-angry.png")
zero_normal = pygame.image.load("asset/sprite/cutscene/character/zero-normal.png")
zero_sad = pygame.image.load("asset/sprite/cutscene/character/zero-sad.png")
zero_happy = pygame.image.load("asset/sprite/cutscene/character/zero-happy.png")
zero_angry = pygame.image.load("asset/sprite/cutscene/character/zero-angry.png")

image_size = (450, 450)

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

screen = pygame.display.set_mode((1280, 720))

cutscene_text1 = '''
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
Clyde Livingstone의 신발을 훔친 범인이다!"
'''

lines = comgwa.makeScript(cutscene_text1)
backgrounds = [[town, stanley_happy_left], [town, stanley_angry_left], [camp1, zero_normal_left, stanley_angry_right], [camp2, stanley_angry_left]]

cutscene1 = comgwa.CutScene("new_scene", lineback, backgrounds, lines, "level03")


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
    _____O_
    _____G_
    _____O_
    _OGOOO_
    _______
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 2), (1, 4))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level02"))

levelList.append(comgwa.LevelScene("level02", comgwa.Level("""
    _______
    _OGOOO_
    _______
    _OOOOO_
    _OOOGO_
    _OOOOO_
    _______
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (3, 3))
    ], (60, 60), 0.3), holePalette, dirtPalette, "new_scene"))

levelList.append(comgwa.LevelScene("level03", comgwa.Level("""
    ________
    ___OOO__
    __OOGOO_
    _____OO_
    _____OO_
    ________
    _OOOOOO_
    _GOOO_O_
    __OO__O_
    ________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (3, 6))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level04"))


levelList.append(comgwa.LevelScene("level04", comgwa.Level("""
    __OOO____
    OOO__O___
    OF_OOO___
    OF__OOOOO
    OGO_O_O_O
    ___OO_O_O
    G__OO_OOO
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (3, 6))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level05"))

'''
테스트용 코드
'''

pygame.key.set_repeat(500, 500)

scenes = levelList + [cutscene1]

manager = comgwa.SceneManager(scenes)
manager.run()