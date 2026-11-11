# 《第一印象》第一章试玩版 v2
# 版本重点：接入第一批锚点立绘与第二批扩充立绘，并适度丰富关键剧情。

# ---------- 角色定义 ----------
define n = Character(None)
define e = Character("伊丽莎白")
define j = Character("简")
define mb = Character("班纳特太太")
define mr = Character("班纳特先生")
define b = Character("宾利")
define d = Character("达西")
define c = Character("夏洛特")

default prejudice = 0
default pride = 0
default insight = 0
default sister_bond = 0
default darcy_attention = 0

default joked_at_darcy = False
default silent_grudge = False
default public_retort = False

default protected_jane = 0
default watched_family = 0

image bg_longbourn_breakfast = "images/bg_longbourn_breakfast.png"
image bg_carriage_night = "images/bg_carriage_night.png"
image bg_meryton_ball = "images/bg_meryton_ball.png"
image bg_ball_corner = "images/bg_ball_corner.png"
image bg_longbourn_night = "images/bg_longbourn_night.png"

image elizabeth home neutral = "images/characters/elizabeth_home_neutral.png"
image elizabeth home teasing = "images/characters/elizabeth_home_teasing.png"
image elizabeth ball neutral = "images/characters/elizabeth_ball_neutral.png"
image elizabeth ball surprised = "images/characters/elizabeth_ball_surprised.png"
image elizabeth ball serious = "images/characters/elizabeth_ball_serious.png"
image jane ball neutral = "images/characters/jane_ball_neutral.png"
image mrs_bennet home excited = "images/characters/mrs_bennet_home_excited.png"
image mrs_bennet home directing = "images/characters/mrs_bennet_home_directing.png"
image mrs_bennet ball proud = "images/characters/mrs_bennet_ball_proud.png"
image mr_bennet home neutral = "images/characters/mr_bennet_home_neutral.png"
image bingley ball smile = "images/characters/bingley_ball_smile.png"
image darcy ball cold = "images/characters/darcy_ball_cold.png"
image darcy ball formal = "images/characters/darcy_ball_formal.png"
image darcy ball observing = "images/characters/darcy_ball_observing.png"
image darcy ball awkward = "images/characters/darcy_ball_awkward.png"
image charlotte ball neutral = "images/characters/charlotte_ball_neutral.png"

transform sprite_left:
    xalign 0.16
    yalign 1.0
    zoom 0.34
transform sprite_midleft:
    xalign 0.34
    yalign 1.0
    zoom 0.34
transform sprite_center:
    xalign 0.50
    yalign 1.0
    zoom 0.34
transform sprite_midright:
    xalign 0.66
    yalign 1.0
    zoom 0.34
transform sprite_right:
    xalign 0.84
    yalign 1.0
    zoom 0.34
transform sprite_big_center:
    xalign 0.50
    yalign 1.0
    zoom 0.38
transform sprite_tall_left:
    xalign 0.22
    yalign 1.0
    zoom 0.31
transform sprite_tall_right:
    xalign 0.78
    yalign 1.0
    zoom 0.31
transform sprite_breakfast_left:
    xalign 0.12
    yalign 1.0
    zoom 0.30
transform sprite_breakfast_center:
    xalign 0.50
    yalign 1.0
    zoom 0.30
transform sprite_breakfast_right:
    xalign 0.88
    yalign 1.0
    zoom 0.30
transform sprite_ball_charlotte_farleft:
    xalign 0.04
    yalign 1.0
    zoom 0.30
transform sprite_ball_darcy_intro:
    xalign 0.42
    yalign 1.0
    zoom 0.32
transform sprite_ball_elizabeth_farright:
    xalign 0.90
    yalign 1.0
    zoom 0.34

label start:
    scene black
    with fade
    n "《第一印象》"
    n "第一章：梅里屯舞会"
    n "本章已接入扩充立绘，并加入横屏手机 UI 适配。不同场景与情绪节点中，人物会以不同状态出现。"
    jump breakfast_scene
