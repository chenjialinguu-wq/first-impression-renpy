label ch02_jane_ill_scene:

    scene bg_longbourn_morning_rain
    with fade

    show mrs_bennet home excited at sprite_breakfast_left
    show elizabeth home neutral at sprite_breakfast_right

    n "第二天早晨，尼日斐花园的消息送到了朗伯恩。"
    mb "简病了。"

    show mrs_bennet home directing at sprite_breakfast_left
    mb "不过不用担心，她留在尼日斐。宾利先生一定会亲自关心她。"

    show elizabeth home neutral at sprite_breakfast_right
    e "妈妈，她病了。"

    mb "只是小病。一个人在适当的屋子里生一场小病，有时比健康地待在家里更有前途。"

    n "伊丽莎白没有立刻回答。"
    n "她忽然觉得，朗伯恩的早餐室比昨夜的舞会还要喧闹。"

    menu:
        "听到简病倒后，你决定怎么做？"

        "立刻步行去尼日斐探望。":
            $ jane_health_care += 2
            $ pride += 1
            $ walked_in_mud = True
            show elizabeth home neutral at sprite_breakfast_right
            e "我要去看她。"
            mb "步行？三英里？你的裙子会全是泥！"
            e "比起简的身体，裙摆暂时没有那么重要。"
            jump ch02_country_road_scene

        "先整理衣装，再尽快前往。":
            $ jane_health_care += 1
            $ netherfield_reputation += 1
            show elizabeth home neutral at sprite_breakfast_right
            e "我会去看她。至少让我换一件适合出门的衣服。"
            mb "这才像话。尼日斐的人可都在看着。"
            e "我知道。他们似乎很擅长这件事。"
            jump ch02_country_road_scene

        "先质问母亲是否早料到会这样。":
            $ pride += 1
            $ class_pressure += 1
            show elizabeth home teasing at sprite_breakfast_right
            e "妈妈，您昨晚是不是已经把这场雨也算进了婚姻计划？"
            mb "丽萃，你说得太难听了。"
            e "事实有时比说法更难听。"
            n "她最终还是起身去尼日斐。"
            $ walked_in_mud = True
            $ jane_health_care += 1
            jump ch02_country_road_scene
