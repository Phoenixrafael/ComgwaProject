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
warden_normal = pygame.image.load("asset/sprite/cutscene/character/wardennormal.png")
warden_happy = pygame.image.load("asset/sprite/cutscene/character/wardenhappy.png")
warden_angry = pygame.image.load("asset/sprite/cutscene/character/wardenangry.png")
xray_normal = pygame.image.load("asset/sprite/cutscene/character/xraynormal.png")
xray_happy = pygame.image.load("asset/sprite/cutscene/character/xrayhappy.png")
lawyer_normal = pygame.image.load("asset/sprite/cutscene/character/lawyernormal.png")

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
warden_normal_left = comgwa.makeImage(pygame.transform.scale(warden_normal, image_size), 1)
warden_normal_right = comgwa.makeImage(pygame.transform.scale(warden_normal, image_size), 2)
warden_happy_left = comgwa.makeImage(pygame.transform.scale(warden_happy, image_size), 1)
warden_happy_right = comgwa.makeImage(pygame.transform.scale(warden_happy, image_size), 2)
warden_angry_left = comgwa.makeImage(pygame.transform.scale(warden_angry, image_size), 1)
warden_angry_right = comgwa.makeImage(pygame.transform.scale(warden_angry, image_size), 2)
xray_happy_left = comgwa.makeImage(pygame.transform.scale(xray_happy, image_size), 1)
xray_happy_right = comgwa.makeImage(pygame.transform.scale(xray_happy, image_size), 2)
xray_normal_left = comgwa.makeImage(pygame.transform.scale(xray_normal, image_size), 1)
xray_normal_right = comgwa.makeImage(pygame.transform.scale(xray_normal, image_size), 2)
lawyer_normal_left = comgwa.makeImage(pygame.transform.scale(lawyer_normal, image_size), 1)
lawyer_normal_right = comgwa.makeImage(pygame.transform.scale(lawyer_normal, image_size), 2)

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
            [],
            [lawcourt],
            [lawcourt, stanley_sad_left],
            [lawcourt, stanley_happy_left],
            [bus],
            [bus, stanley_normal_left],
            [],
            [camp1, stanley_normal_left, warden_normal_right],
            [camp1, stanley_normal_left, warden_happy_right],
            [camp1, stanley_normal_left, warden_happy_right],
            [camp1, stanley_normal_left, warden_happy_right],
            [camp1, stanley_sad_left, warden_happy_right],
            [camp1, stanley_normal_left, warden_normal_right],
            [camp1, stanley_normal_left, warden_normal_right],
            [camp1, stanley_normal_left, warden_angry_right],
            [camp1, stanley_sad_left, warden_normal_right],
            [camp1, stanley_normal_left, warden_normal_right],
            [camp1, stanley_normal_left, warden_normal_right],
            [camp1, stanley_sad_left, warden_angry_right],
            [camp2, stanley_normal_left, warden_happy_right],
            []],
comgwa.makeScript('''
black/35/Zero/
헉...헉...
일단 신발을 여기 두자..
#
black/35/Stanley/
어? 이 신발 뭐지?
#
black/35/Stanley/
주워 가면 아버지의 구두 냄새 제거 연구에
도움이 되겠지? 주워 가야...
#
black/35/Police/
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
black/35/Stanley/
네... 인지했습니다..
#
white/50/Narration/
그렇게 법정으로 가게 된 Stanley...
#
black/35/Judge/
Stanley, 그래서 Camp Green Lake와
감옥 중 어디를 가겠니?
#
black/35/Stanley/
'Camp Green Lake? 재밌어 보이는데?'
#
black/35/Stanley/
Camp Green Lake로 갈게요!
#
white/50/Narration/
깊이 잠에 들었던 Stanley...
#
black/35/Stanley/
여...여기가 어디지?
버..버스잖아?
#
white/50/Narration/
금세 다시 잠에 들어 버린 Stanley
#
black/35/Stanley/
여기가 어디죠...?
#
black/35/Warden/
만나서 반갑다. Stanley.
여기가 바로 Camp Green Lake란다.
#
black/35/Stanley/
아... 그렇군요..
제가 여기서 무엇을 하면 되나요?
#
black/35/Warden/
지금부터 내가 Camp Green Lake의 규칙을
설명해줄 테니 잘 듣도록.
#
black/35/Stanley/
네..넵!
#
black/35/Warden/
첫째, 매일 내가 지정한 장소에 구덩이를 판다.
내가 지정한 장소는 X표가 되어 있을 것이다.
#
black/35/Stanley/
자..잠시만요.
구덩이를 왜 파야 하는 거죠?
#
black/35/Warden/
그건 바로 너의 인격 수양을 위해서야.
그리고 내 말을 중간에 끊지 말고 끝까지 듣도록 해라.
#
black/35/Stanley/
아 네.. 죄송합니다.
#
black/35/Warden/
둘째, 신기한 물건을 발견했을 경우 이를 즉시 보고할 것.
이해했을 것이라고 믿는다.
#
black/35/Stanley/
그럼 구덩이는 내일부터 파는 건가요?
#
black/35/Warden/
무슨 소리! 구덩이는 오늘부터 파야지.
일단 네가 생활할 D 캠프로 안내해줄 테니 따라와라.
#
black/35/Warden/
첫날은 매우 힘들 것이다. 행운을 빈다.
#
white/50/Narration/
Stanley가 무사히 구덩이를 파도록 도와주자.

'''), "level01"))

cutscenes.append(comgwa.CutScene("afterday3", lineback,
[[camp2, stanley_normal_left],
            [camp2, stanley_happy_left],
            [camp2, stanley_happy_left, warden_normal_right],
            [camp2, stanley_happy_left, warden_happy_right],
            [camp2, stanley_sad_left, warden_happy_right],
            [camp3, xray_normal_left],
            [],
            [camp3, xray_normal_left, stanley_normal_right],
            [camp3, xray_normal_left, stanley_normal_right],
            [camp3, xray_normal_left, stanley_normal_right],
            [camp3, xray_normal_left, stanley_normal_right],
            []],
comgwa.makeScript("""
black/35/Stanley/
어? 저기 떨어져 있는 건 뭐지?
#
black/35/Stanley/
뭔지 모르겠지만 신기한데?
아 맞다, 소장님께 보고해야겠다.
#
black/35/Stanley/
소장님, 저 신기한 걸 찾았어요!
#
black/35/Warden/
이건 나한테 주고 오늘 하루는 들어가서 쉬도록 해라.
#
black/35/Stanley/
'이미 오늘 팔 건 거의 다 팠는데...'
네 감사합니다!
#
black/35/X-ray/
'우와... 부럽다.'
#
white/50/Narration/
잠시 후 X-ray가 Stanley를 불렀다
#
black/35/Stanley/
왜... 무슨 일이야?
#
black/35/X-ray/
별일은 아니고... 혹시 나중에도 신기한 물건을 찾으면
나한테 주면 안 될까?
#
black/35/X-ray/
내가 지금껏 몇 개월 동안 여기 있으면서
너처럼 쉬어본 적이 없어.
#
black/35/Stanley/
어... 알겠어...
#
white/50/Narration/
계속 Stanley를 도와주자.

"""), "level04"))

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
    ], (60, 60), 0.3), holePalette, dirtPalette, "afterday3"))

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
    _________
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
        comgwa.Player(zeroPalette, (0, 1), (1, 1))
    ], (60, 60), 0.3, comgwa.Counter(counterSprite, 3, True, False)), holePalette, dirtPalette, "level12"))

levelList.append(comgwa.LevelScene("level12", comgwa.Level("""
    __________
    _OOOOOO_G_
    __O__O____
    __O__O____
    __O__O____
    __OOOO____
    __________
    """, palette, [
        comgwa.Player(zeroPalette, (0, 2), (1, 1))
    ], (60, 60), 0.3, comgwa.Counter(counterSprite, 20, False, True)), holePalette, dirtPalette, "level13"))


levelList.append(comgwa.LevelScene("level13", comgwa.Level("""
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
        comgwa.Player(zeroPalette, (0, 2), (1, 2))
    ], (60, 60), 0.3, comgwa.Counter(counterSprite, 33, False, True)), holePalette, dirtPalette, "level14"))


levelList.append(comgwa.LevelScene("level14", comgwa.Level("""
    _______
    ___G___
    _______
    _______
    _______
    _______
    _OOOOO_
    _OOOOO_
    _OOOOO_
    _OOOOO_
    _OOOOO_
    _______
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (3, 6))
    ], (60, 60), 0.3, comgwa.Counter(counterSprite, 100, True, False)), holePalette, dirtPalette, "level15"))

levelList[-1].run()

'''
테스트용 코드
'''

pygame.key.set_repeat(500, 500)

scenes = cutscenes + levelList

manager = comgwa.SceneManager(scenes)
manager.run()