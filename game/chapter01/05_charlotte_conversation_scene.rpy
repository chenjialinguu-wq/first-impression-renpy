label charlotte_conversation_scene:
    scene bg_ball_corner
    with fade
    show charlotte ball neutral at sprite_left
    show elizabeth ball serious at sprite_right
    c "你不该太在意达西先生的话。他太骄傲了，几乎所有人都这样说。"
    e "我并没有太在意。"
    if public_retort:
        e "我只是觉得，既然他把一句冒犯说得像事实，我也可以把一句事实说得像礼貌。"
    elif joked_at_darcy:
        e "我只是愿意把它当成笑话。笑话若不被分享，未免太浪费。"
    elif silent_grudge:
        e "我只是愿意相信公众的判断偶尔也会准确。"
    c "他有一万镑年收入。"
    show elizabeth home teasing at sprite_right
    e "那他的傲慢便有了非常宽敞的住宅。"
    c "丽萃，你会因为一句话讨厌一个人吗？"
    menu:
        "你如何回答夏洛特？"
        "不是因为一句话，而是因为他说这句话时毫不怀疑自己有权这样说。":
            $ insight += 2
            $ prejudice += 1
            show elizabeth ball serious at sprite_right
            e "有些话真正刺人的地方，不在内容，而在说话人确信自己有资格这样评价别人。"
            c "你看得比你说出来的还深。"
        "我只是觉得他很可笑。":
            $ pride += 1
            $ prejudice += 1
            show elizabeth home teasing at sprite_right
            e "可笑的人若足够富有，人们就称之为‘高傲’。这也算语言的礼貌。"
            c "你今晚会把自己逗得很开心。"
        "也许我该多观察他，而不是立刻下判断。":
            $ insight += 2
            $ prejudice -= 1
            $ darcy_attention += 1
            show elizabeth ball serious at sprite_right
            e "也许我该多观察他，而不是立刻下判断。"
            c "这不像你。"
            e "是吗？那更值得一试。"
    n "舞会仍在继续，仿佛刚才的一切只是烛光里微小的一次晃动。"
    n "但伊丽莎白已经知道，今晚的记忆不会只属于简和宾利。"
    jump family_risk_scene
