label ch02_drawing_room_scene:

    scene bg_netherfield_drawing_room
    with fade

    show elizabeth ball serious at sprite_right
    show bingley ball smile at sprite_left

    b "班纳特小姐，您能来，简小姐一定很高兴。她若有什么需要，请务必告诉我。"
    e "谢谢您，宾利先生。她最需要的是安静、温暖，以及不要被当成一桩令人满意的巧合。"
    b "我想我明白您的意思。"

    hide bingley

    n "宾利离开后，客厅里的温度似乎立刻变了。"
    n "卡罗琳·宾利坐在壁炉旁，语气温柔，目光却比窗外的雨更冷。"

    cb "班纳特小姐，您是步行来的？"

    if walked_in_mud:
        cb "三英里的路。这样的热心，真令人……印象深刻。"
        h "还有裙摆。也很令人印象深刻。"
    else:
        cb "这一路想必不轻松。乡间道路总是不太顾及淑女的鞋。"

    menu:
        "面对宾利姐妹对你仪容和出身的审视，你如何回应？"

        "礼貌忍耐，把注意力放回简。":
            $ netherfield_reputation += 1
            $ jane_health_care += 1
            show elizabeth ball serious at sprite_right
            e "若姐姐能因此安心，我并不介意道路难走。"
            cb "您真是情深。"
            e "亲情若还需要被称赞，未免太可怜。"

        "机智回击她们对泥泞裙摆的关注。":
            $ pride += 2
            $ caroline_rivalry += 2
            $ netherfield_reputation -= 1
            show elizabeth home teasing at sprite_right
            e "泥点至少证明我走过一段路。"
            e "有些人的礼貌看起来干净，却未必经过任何地方。"
            n "壁炉里的火轻轻响了一声。卡罗琳的笑容也轻轻收紧了。"

        "沉默观察卡罗琳的语气。":
            $ insight += 2
            $ class_pressure += 1
            show elizabeth ball serious at sprite_right
            n "伊丽莎白没有立刻回应。"
            n "她发现卡罗琳的每一句关心，都像在寻找一个可以称量她的刻度。"
            $ read_caroline = True
            e "您很关心我的路途。"
            cb "我只是惊讶。"
            e "我看出来了。"

    n "这时，达西先生放下手中的书。"

    if prejudice >= 4:
        n "伊丽莎白几乎立刻预料到他会站在宾利姐妹那一边。"
    else:
        n "伊丽莎白注意到，他并没有像卡罗琳那样看她的裙摆。"

    show darcy ball observing at sprite_tall_left
    d "班纳特小姐走了很远的路。"

    show elizabeth ball serious at sprite_right
    e "是的，达西先生。三英里。听上去比实际走起来短。"

    d "但动机似乎比路更清楚。"
    $ darcy_attention += 1

    if prejudice >= 4:
        e "您这话听起来像赞许，也像审查。"
        d "也许只是陈述。"
    else:
        e "那我希望它至少没有弄脏您对我的判断。"
        show darcy ball formal at sprite_tall_left
        d "判断若只看裙摆，确实不值得太在意。"
        $ darcy_attention += 1

    hide darcy
    hide elizabeth
    jump ch02_evening_library_scene
