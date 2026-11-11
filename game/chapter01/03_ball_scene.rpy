label ball_scene:
    scene bg_meryton_ball
    with fade
    n "梅里屯的舞会，是乡绅社会最温柔也最残酷的剧场。"
    n "在这里，一次鞠躬可以被解读为承诺，一次沉默可以被解读为轻蔑。"
    show bingley ball smile at sprite_left
    show jane ball neutral at sprite_right
    b "班纳特小姐，能否请您跳下一支舞？"
    j "我很荣幸。"
    n "简的回答很轻，脸上的喜悦也很轻。"
    n "但伊丽莎白看得出来，那种喜悦正因克制而显得更加明显。"
    hide bingley
    hide jane
    show elizabeth ball neutral at sprite_right
    show charlotte ball neutral at sprite_left
    c "宾利先生似乎很喜欢简。"
    e "我希望他比看起来更聪明一些，聪明到能看出简也喜欢他。"
    c "简的温柔，有时简直像一封写得太含蓄的信。"
    e "所以我才担心收信人是否识字。"
    show mrs_bennet ball proud at sprite_center
    mb "两支舞！简已经同宾利先生跳了两支舞！"
    show elizabeth ball serious at sprite_right
    e "妈妈，也许不必让整个梅里屯都参与这项统计。"
    mb "你不懂，丽萃，舞会上的数字可比账本上的数字重要多了。"
    hide mrs_bennet
    hide charlotte
    hide elizabeth
    n "就在这时，宾利先生身旁那位沉默的朋友终于引起了全场更持久的注意。"
    show charlotte ball neutral at sprite_ball_charlotte_farleft
    show darcy ball formal at sprite_ball_darcy_intro
    show elizabeth ball neutral at sprite_ball_elizabeth_farright
    c "那位就是达西先生。"
    e "他看起来像一封密封得过于严实的信。"
    c "也许里面写着一万镑年收入。"
    show elizabeth ball serious at sprite_ball_elizabeth_farright
    e "那倒解释了他为何不急着被人读懂。"
    hide charlotte
    hide darcy
    hide elizabeth
    jump darcy_insult_scene
