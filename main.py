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
bigThumb = pygame.image.load("asset/sprite/background/bigThumb.png")
bus = pygame.image.load("asset/sprite/background/bus.png")
camp1 = pygame.image.load("asset/sprite/background/camp1.png")
camp2 = pygame.image.load("asset/sprite/background/camp2.png")
camp3 = pygame.image.load("asset/sprite/background/camp3.png")
lawCourt = pygame.image.load("asset/sprite/background/lawCourt.png")
town = pygame.image.load("asset/sprite/background/town.png")
bigThumb_dark = pygame.image.load("asset/sprite/background/bigThumb_dark.png")
bigThumb_white = pygame.image.load("asset/sprite/background/bigThumb_white.png")
bus_dark = pygame.image.load("asset/sprite/background/bus_dark.png")
bus_white = pygame.image.load("asset/sprite/background/bus_white.png")
camp1_dark = pygame.image.load("asset/sprite/background/camp1_dark.png")
camp1_white = pygame.image.load("asset/sprite/background/camp1_white.png")
camp2_dark = pygame.image.load("asset/sprite/background/camp2_dark.png")
camp2_white = pygame.image.load("asset/sprite/background/camp2_white.png")
camp3_dark = pygame.image.load("asset/sprite/background/camp3_dark.png")
camp3_white = pygame.image.load("asset/sprite/background/camp3_white.png")
lawCourt_dark = pygame.image.load("asset/sprite/background/lawCourt_dark.png")
lawCourt_white = pygame.image.load("asset/sprite/background/lawCourt_white.png")
town_dark = pygame.image.load("asset/sprite/background/town_dark.png")
town_white = pygame.image.load("asset/sprite/background/town_white.png")

# 배경 이미지 변환
bigThumb = comgwa.makeImage(pygame.transform.scale(bigThumb, (1280, 720)), 0)
bus = comgwa.makeImage(pygame.transform.scale(bus, (1280, 720)), 0)
camp1 = comgwa.makeImage(pygame.transform.scale(camp1, (1280, 720)), 0)
camp2 = comgwa.makeImage(pygame.transform.scale(camp2, (1280, 720)), 0)
camp3 = comgwa.makeImage(pygame.transform.scale(camp3, (1280, 720)), 0)
lawCourt = comgwa.makeImage(pygame.transform.scale(lawCourt, (1280, 720)), 0)
town = comgwa.makeImage(pygame.transform.scale(town, (1280, 720)), 0)
bigThumb_dark = comgwa.makeImage(pygame.transform.scale(bigThumb_dark, (1280, 720)), 0)
bigThumb_white = comgwa.makeImage(pygame.transform.scale(bigThumb_white, (1280, 720)), 0)
bus_dark = comgwa.makeImage(pygame.transform.scale(bus_dark, (1280, 720)), 0)
bus_white = comgwa.makeImage(pygame.transform.scale(bus_white, (1280, 720)), 0)
camp1_dark = comgwa.makeImage(pygame.transform.scale(camp1_dark, (1280, 720)), 0)
camp1_white = comgwa.makeImage(pygame.transform.scale(camp1_white, (1280, 720)), 0)
camp2_dark = comgwa.makeImage(pygame.transform.scale(camp2_dark, (1280, 720)), 0)
camp2_white = comgwa.makeImage(pygame.transform.scale(camp2_white, (1280, 720)), 0)
camp3_dark = comgwa.makeImage(pygame.transform.scale(camp3_dark, (1280, 720)), 0)
camp3_white = comgwa.makeImage(pygame.transform.scale(camp3_white, (1280, 720)), 0)
lawCourt_dark = comgwa.makeImage(pygame.transform.scale(lawCourt_dark, (1280, 720)), 0)
lawCourt_white = comgwa.makeImage(pygame.transform.scale(lawCourt_white, (1280, 720)), 0)
town_dark = comgwa.makeImage(pygame.transform.scale(town_dark, (1280, 720)), 0)
town_white = comgwa.makeImage(pygame.transform.scale(town_white, (1280, 720)), 0)


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

cutscenes.append(comgwa.CutScene("intro", lineback, town,
[[town_white, zero_normal_left],
[town_white, stanley_normal_right],
[town_white, stanley_happy_right],
[town_white, stanley_angry_right],
[town_white, stanley_angry_right],
[town_white, stanley_angry_right],
[town_white, stanley_angry_right],
[town_white, stanley_sad_right],
[],
[lawCourt],
[lawCourt_white, stanley_sad_left],
[lawCourt_white, stanley_happy_left],
[bus_dark],
[bus_white, stanley_normal_left],
[],
[camp1_white, stanley_normal_left, warden_normal_right],
[camp1_white, stanley_normal_left, warden_happy_right],
[camp1_white, stanley_normal_left, warden_happy_right],
[camp1_white, stanley_normal_left, warden_happy_right],
[camp1_white, stanley_sad_left, warden_happy_right],
[camp1_white, stanley_normal_left, warden_normal_right],
[camp1_white, stanley_normal_left, warden_normal_right],
[camp1_white, stanley_normal_left, warden_angry_right],
[camp1_white, stanley_sad_left, warden_normal_right],
[camp1_white, stanley_normal_left, warden_normal_right],
[camp1_white, stanley_normal_left, warden_normal_right],
[camp1_white, stanley_sad_left, warden_angry_right],
[camp2_white, stanley_normal_left, warden_happy_right],
[camp2_dark]],
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

cutscenes.append(comgwa.CutScene("afterday1", lineback, camp1,
[[camp1_white, stanley_sad_left]],
comgwa.makeScript("""
black/35/Stanley/
휴..역시 첫날은 쉽지 않구나...
내일은 조금 더 편할까?
"""), "level02"))

cutscenes.append(comgwa.CutScene("afterday3", lineback, camp2,
[[camp2_white, stanley_normal_left],
[camp2_white, stanley_happy_left],
[camp2_white, stanley_happy_left, warden_normal_right],
[camp2_white, stanley_happy_left, warden_happy_right],
[camp2_white, stanley_sad_left, warden_happy_right],
[camp3_white, xray_normal_left],
[],
[camp3_white, xray_normal_left, stanley_normal_right],
[camp3_white, xray_normal_left, stanley_normal_right],
[camp3_white, xray_normal_left, stanley_normal_right],
[camp3_white, xray_normal_left, stanley_normal_right],
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

cutscenes.append(comgwa.CutScene("afterday5", lineback, camp1,
[[camp1_white, stanley_normal_left],
[camp1_white, stanley_normal_left],
[camp1_white, stanley_normal_left, xray_normal_right],
[camp1_white, stanley_normal_left, xray_happy_right],
[camp1_white, stanley_normal_left, xray_happy_right],
[camp1_white, stanley_happy_left, xray_happy_right],
[],
[camp3_white, xray_happy_right],
[camp3_white, warden_normal_left, xray_happy_right],
[camp3_white, warden_happy_left, xray_happy_right],
[camp3_white, warden_happy_left, xray_happy_right],
[camp3_white, warden_happy_left, stanley_normal_right],
[camp3_white, warden_happy_left, stanley_sad_right],
[camp3_white, warden_happy_left, stanley_sad_right],
[]],
comgwa.makeScript("""
black/35/Stanley/
어...이게 뭐지...?
쓰읍...이런 거 찾으면 X-ray 주기로 했는데..
#
black/35/Stanley/
K...B...라고 적혀 있네.
하...그래도 X-ray 줘야겠지?
#
black/35/Stanley/
X-ray! 나 여기 신기한 물건을 찾았어.
네가 저번에 부탁했던 대로 너 주려고.
#
black/35/X-ray/
고마워 Stanley! 소장님...!
#
black/35/Stanley/
자..잠시만. 너 오늘 구덩이 거의 다 팠잖아.
내일 아침에 발견한 척하고 내일 쉬는 게 어때?
#
black/35/X-ray/
오 그거 좋은 생각인데?
아무튼 고마워!
#
white/50/Narration/
다음 날...
#
black/35/X-ray/
소장님! 저 여기서 신기한 물건을 찾았어요!
어서 와보세요!
#
black/35/Warden/
어디 보자꾸나. K.B...?
X-ray, 이거 어디에서 났니?
#
black/35/X-ray/
여기 제가 파려고 하자마자 나왔어요.
#
black/35/Warden/
일단 너는 오늘 하루 쉬도록 해라.
그리고 다른 학생들, 모두 여기로 와봐.
#
black/35/Warden/
모두들 이 근처를 크게 파도록 해라.
알겠나?
#
black/35/Stanley/
네...
#
black/35/Stanley/
'흠... 인격 수양을 목적으로 파는 게 맞아..?'
'아무리 봐도 다른 목적이 있단 말이지.'
#
white/40/Narration/
Warden이 땅을 파라고 하는 진짜 이유가 있을까?
"""), "level06"))

cutscenes.append(comgwa.CutScene("afterday9", lineback, camp1,
[[camp1_white, stanley_normal_left, zero_normal_right],
[camp1_white, stanley_normal_left, zero_normal_right],
[camp1_white, stanley_normal_left, zero_normal_right],
[camp1_white, stanley_normal_left, zero_normal_right],
[camp1_white, stanley_normal_left, zero_normal_right],
[camp1_white, stanley_normal_left, zero_normal_right]],
comgwa.makeScript("""
black/35/Stanley/
안녕..? 넌 이름이 뭐야?
#
black/35/Zero/
난 Zero야.
#
black/35/Stanley/
만나서 반가워. 난 Stanley라고 해.
#
black/35/Zero/
넌 어쩌다가 이곳에 오게 되었니?
#
black/35/Stanley/
난 갑자기 억울하게 신발을 훔쳤다는 명목으로
붙잡혀 왔어.
#
black/35/Zero/
'신발...? 그렇다면 혹시...?'
"""), "level10"))

cutscenes.append(comgwa.CutScene("afterday10", lineback, camp1,
[
[camp1_dark],
[camp1_white, stanley_normal_left, zero_normal_right],
[camp1_white, stanley_angry_left, zero_normal_right],
[camp1_white, stanley_normal_left, zero_sad_right],
[camp1_white, stanley_normal_left, zero_normal_right],
[camp1_white, stanley_normal_left, zero_normal_right],
[camp1_white, stanley_happy_left, zero_normal_right],
[camp1_white, stanley_happy_left, zero_normal_right],
[camp1_white, stanley_happy_left, zero_normal_right],
[camp2_dark],
[camp2_white, zero_sad_left],
[camp2_white, zero_sad_left],
[]
],
comgwa.makeScript("""
white/50/Narration/
부모님께 편지를 쓰던 Stanley
#
black/35/Zero/
우와...
#
black/35/Stanley/
왜 남이 쓰는 편지를 구경하는 거야?
#
black/35/Zero/
나는 알파벳을 읽을 줄 몰라.
혹시 나한테 알파벳 가르쳐줄 수 있니?
#
black/35/Stanley/
음...
#
black/35/Zero/
그 대신 내가 너의 구덩이를 대신 파 줄게.
#
black/35/Stanley/
'오 그러면 완전 이득이잖아?'
#
black/35/Stanley/
그래!
#
black/35/Stanley/
그러면 얼마든지 내가 알파벳을 가르쳐 줄 수 있지!
#
white/50/Narration/
열심히 구덩이를 판 Zero...
#
black/35/Zero/
에휴 힘들다...
#
black/35/Zero/
Stanley의 구덩이는 최대한 적게 이동하면서
효율적으로 파야겠어.
#
white/50/Narration/
Zero가 효율적으로 구덩이를 파도록 도와주자.
"""), "level11"))

cutscenes.append(comgwa.CutScene("afterday12", lineback, camp2,
[[camp2_white, stanley_normal_left, zero_normal_right],
[camp2_white, stanley_normal_left, zero_normal_right],
[camp2_white, stanley_normal_left, zero_normal_right]],
comgwa.makeScript("""
black/35/Stanley/
너 알파벳 아는 거 있어?
#
black/35/Zero/
A, B, C, D, ...
#
black/35/Stanley/
그 다음은 E야.
"""), "level13"))


cutscenes.append(comgwa.CutScene("afterday15", lineback, camp1,
[[camp1_white, warden_angry_left, stanley_angry_right],
[camp1_white, warden_angry_left, stanley_normal_right],
[camp1_white, warden_angry_left, stanley_sad_right],
[camp1_white, warden_angry_left, stanley_angry_right],
[camp1_white, warden_angry_left, stanley_angry_right],
[camp1_white, warden_angry_left, stanley_angry_right],
[camp1_white, warden_angry_left, stanley_angry_right],
[camp1_white, warden_angry_left, zero_normal_right],
[camp1_white, warden_angry_left, zero_sad_right],
[camp1_white, warden_angry_left, zero_sad_right],
[camp1_white, warden_normal_left, zero_angry_right],
[camp1_white, warden_angry_left, stanley_normal_right],
[camp1_white, warden_angry_left, stanley_normal_right],
[camp1_white, warden_happy_left, stanley_sad_right],
[],
[camp2_white, stanley_sad_left],
[camp2_white, stanley_normal_left],
[camp3_white, stanley_normal_left],
[camp3_white, stanley_normal_right],
[camp3_dark]],
comgwa.makeScript("""
black/35/Warden/
잠시만, Stanley.
너 왜 땅을 파지 않니?
#
black/35/Stanley/
저... 저 Zero에게 알파벳을 가르쳐주는 대신
Zero가 제 구덩이를 대신 파주기로 했어요
#
black/35/Warden/
구덩이를 파는 건 남이 대신해도
되는 일이 아니야!
#
black/35/Stanley/
어차피 인격 수양은 명목이잖아요!
#
black/35/Warden/
무슨 소리니! Stanley!
어서 구덩이이나 파!
#
black/35/Stanley/
저는 알파벳을 가르쳐주면서 인격을
수양하고 있다고요!
#
black/35/Warden/
그래? 어디 잘 가르쳤는지나 한 번 볼까?
#
black/35/Warden/
Zero, h-a-t을 어떻게 발음하니?
#
black/35/Zero/
...
#
black/35/Warden/
푸흡! 기초적인 발음도 못하네!
Zero 너는 머릿속에 들은 게 없어.
#
black/35/Zero/
'안 되겠다. 난 여기를 떠나야겠어.'
#
black/35/Stanley/
너 갑자기 어디 가! Zero!
#
black/35/Warden/
괜찮아. 어차피 이 인근에는 물 한 방울조차
없어서 다시 돌아올 수밖에 없어.
#
black/35/Warden/
이 기회에 안 그래도 거슬리던
Zero 관련 파일을 영구 삭제해야겠군.
#
white/50/Narration/
힌편, Stanley...
#
black/35/Stanley/
하... Zero가 없으니까 무언가 허전해..
#
black/35/Stanley/
어쩔 수 없다. 나도 Zero를 따라가야겠어.
#
black/35/Stanley/
여기는 흙이 젖어 있네.
#
black/35/Stanley/
뭐야 이 흙은 안 파지잖아?
#
white/50/Narration/
Stanley의 여정을 계속 따라가보자.

"""), "level16"))

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
    ], (60, 60), 0.2), holePalette, dirtPalette, "afterday1"))

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
    ], (60, 60), 0.3), holePalette, dirtPalette, "afterday5"))

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
    ], (60, 60), 0.3), holePalette, dirtPalette, "afterday9"))


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
    ], (60, 60), 0.3), holePalette, dirtPalette, "afterday10"))


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
    ], (60, 60), 0.3, comgwa.Counter(counterSprite, 20, False, True)), holePalette, dirtPalette, "afterday12"))


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
        comgwa.Player(zeroPalette, (0, 1), (3, 6))
    ], (60, 60), 0.3, comgwa.Counter(counterSprite, 6, True, False)), holePalette, dirtPalette, "level15"))

levelList.append(comgwa.LevelScene("level16", comgwa.Level("""

    _________
    _OOOOOGO_
    ___F_____
    _WWW_____
    __WWOO___
    _WWOOOOO_
    _WOO_____
    
    """, palette, [
    comgwa.Player(stanleyPalette, (0, 1), (5, 5)),
], (60, 60), 0.3), holePalette, dirtPalette, "level17"))

levelList.append(comgwa.LevelScene("level17", comgwa.Level("""
    
    ___OOO_
    _WOOOO_
    _WWOOO_
    _______
    _O_____
    _OOGOO_
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (2, 1)),
    ], (60, 60), 0.3), holePalette, dirtPalette, "level18"))


levelList.append(comgwa.LevelScene("level18", comgwa.Level("""
    _______
    ___G___
    _______
    _______
    _______
    _______
    _WWWWW_
    _WWWWW_
    _OOOOO_
    _OOOOO_
    _OOOOO_
    _______
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (3, 6))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level19"))

levelList.append(comgwa.LevelScene("level19", comgwa.Level("""
    _________
    __OO_____
    __OOOOWO_
    _OGOFOWO_
    _OFFFGWO_
    _____GW__
    _____O___
    _________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (5, 3))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level20"))

levelList.append(comgwa.LevelScene("level20", comgwa.Level("""
    __________
    _OOOOOFFFF
    _IIIIIOGOF
    _IIIIIFFFF
    _IIIII____
    _OOOOO____
    __________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 3), (1, 1))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level21"))

levelList.append(comgwa.LevelScene("level21", comgwa.Level("""
    ________
    _OOOOGO_
    ____FFF_
    _OIIIOI_
    _IIIIII_
    _IOIIIIF
    _IIIIII_
    _IOIIII_
    ___FFFO_
    __OOOOO_
    __OOOOO_
    __OOOOO_
    ________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (1, 3))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level22"))

levelList.append(comgwa.LevelScene("level22", comgwa.Level("""
    __________
    _OOOOOFFFF
    _IIIIIOGOF
    _IIIIIFFFF
    _IIIIIOGOF
    _OOOOOFFFF
    _OOOOO____
    _OOOOO____
    __________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 3), (1, 1))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level23"))

levelList.append(comgwa.LevelScene("level23", comgwa.Level("""
    ________
    _OOOOOO_
    _OOOOOO_
    _OOOIII_
    _OOOIII_
    _FFFF_F_
    _FOGO_F_
    _FFFFFF_
    ________
    """, palette, [
        comgwa.Player(stanleyPalette, (0, 1), (1, 1))
    ], (60, 60), 0.3), holePalette, dirtPalette, "level24"))

'''
테스트용 코드
'''

pygame.key.set_repeat(500, 500)

scenes = cutscenes + levelList

manager = comgwa.SceneManager(scenes)
manager.run()