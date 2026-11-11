label darcy_insult_scene:
    scene bg_ball_corner
    with fade
    show bingley ball smile at sprite_left
    show darcy ball formal at sprite_tall_right
    b "达西，你为什么不跳舞？这里有许多可爱的小姐。"
    d "你知道我不喜欢与不熟悉的人跳舞。"
    b "那位伊丽莎白小姐很聪明，也很讨人喜欢。你该请她跳一支。"
    show darcy ball cold at sprite_tall_right
    d "她还算可以。"
    d "但还没有漂亮到让我愿意受罚似地跳舞。"
    scene bg_ball_corner
    with dissolve
    show elizabeth ball surprised at sprite_right
    show charlotte ball neutral at sprite_left
    n "这句话落在伊丽莎白耳中时，并不锋利。"
    n "它太平静，太理所当然，像一个人随手合上一本不值得阅读的书。"
    c "丽萃？你听见了？"
    menu:
        "你如何处理达西的评价？"
        "把这句话当成笑话，转身告诉夏洛特。":
            $ prejudice += 1
            $ pride += 1
            $ darcy_attention += 1
            $ joked_at_darcy = True
            show elizabeth home teasing at sprite_right
            e "夏洛特，我刚刚获得了一项新知识。"
            c "什么知识？"
            e "原来我的美貌还不足以惩罚达西先生。"
            c "你生气吗？"
            e "不。若一个人的评价如此缺乏想象力，我实在不好意思为它动怒。"
            n "伊丽莎白笑得很轻，却正好越过人群。"
            show darcy ball observing at sprite_tall_left
            n "达西的目光短暂停了一下，像是第一次意识到自己刚才评价的并不是一件家具。"
        "保持沉默，但记住他的傲慢。":
            $ prejudice += 2
            $ insight += 1
            $ silent_grudge = True
            show elizabeth ball serious at sprite_right
            n "伊丽莎白没有说话。"
            n "她只是看了达西一眼，然后把那句话安静地收进心里。"
            c "你会忘掉它吗？"
            e "大概不会。"
            n "有些冒犯不值得立刻回应。它们更适合成为一个人画像中的第一笔阴影。"
        "主动走近，用礼貌的讽刺回应。":
            $ pride += 2
            $ prejudice += 1
            $ darcy_attention += 2
            $ public_retort = True
            show elizabeth home teasing at sprite_right
            show darcy ball formal at sprite_tall_left
            e "达西先生，请原谅我无意中听见了您的判断。"
            d "班纳特小姐？"
            e "您不必担心。我并不打算强迫您跳舞。毕竟，让一位先生受罚，并非淑女应有的仁慈。"
            show darcy ball awkward at sprite_tall_left
            d "我无意冒犯。"
            e "那真令人安心。若这是有意的，我恐怕要重新估量您的表达能力。"
            n "宾利先生几乎笑出声。达西却罕见地停顿了片刻。"
            show darcy ball observing at sprite_tall_left
            d "班纳特小姐很善于反击。"
            e "只在对方先开火的时候。"
    jump charlotte_conversation_scene
