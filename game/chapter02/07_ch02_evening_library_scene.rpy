label ch02_evening_library_scene:

    scene bg_netherfield_evening_library
    with fade

    show elizabeth ball serious at sprite_right
    show darcy ball formal at sprite_tall_left

    n "夜晚的尼日斐客厅比白日更安静。"
    n "壁炉、书页、茶杯和烛光，把每一句话都照得格外清楚。"

    cb "一位真正有教养的女子，必须精通音乐、绘画、舞蹈、语言。"
    cb "还要有优雅的举止、得体的谈吐，以及足够的阅读。"

    d "我还会加上一点：她必须通过广泛阅读来提高心智。"

    show elizabeth home teasing at sprite_right
    e "那我真惊讶世上竟还有这样的人。"

    cb "班纳特小姐不相信女子可以如此完善？"

    menu:
        "你如何回应这套‘完美女性’标准？"

        "讽刺：这更像一份清单，不像一个人。":
            $ pride += 2
            $ caroline_rivalry += 2
            $ darcy_attention += 1
            show elizabeth home teasing at sprite_right
            e "您所说的，是一位女子，还是一份清单？"
            cb "您真爱把严肃话题说成笑话。"
            e "有些严肃话题若太不近人情，只能先被笑话救回来。"
            show darcy ball observing at sprite_tall_left
            n "达西的目光从书页上移开，停留的时间比礼貌所需略长。"

        "认真：才艺不应只用于被人评价。":
            $ insight += 2
            $ darcy_attention += 1
            show elizabeth ball serious at sprite_right
            e "若音乐、绘画、语言和阅读最终只是为了让旁人判断一个女子是否合格，那未免太辛苦了。"
            d "那您认为才艺应当为了什么？"
            e "为了使人更自由，而不是更容易被衡量。"
            show darcy ball observing at sprite_tall_left
            $ darcy_attention += 1

        "克制：保持沉默，观察达西和卡罗琳。":
            $ insight += 2
            $ netherfield_reputation += 1
            $ read_caroline = True
            show elizabeth ball serious at sprite_right
            n "伊丽莎白垂下眼，暂时没有加入。"
            n "卡罗琳在说‘女子’时，眼睛却始终看向达西。"
            n "达西听着她的话，目光却并不总在她身上。"
            e "我想我今晚更适合做听众。"
            cb "听众若足够敏锐，也很危险。"

    cb "达西先生，您不觉得班纳特小姐的想法很特别吗？"

    if darcy_attention >= 4:
        show darcy ball observing at sprite_tall_left
        d "特别之处在于，她似乎不急于取悦任何人。"
        $ caroline_rivalry += 1
        cb "这也可以被称为缺乏温顺。"
        d "或许。也可以被称为诚实。"
    else:
        show darcy ball formal at sprite_tall_left
        d "班纳特小姐的表达很有锋芒。"
        cb "锋芒有时会伤到自己。"
        e "也有时只是让旁人知道它不是装饰。"

    n "谈话暂时停住。"
    n "伊丽莎白忽然意识到，尼日斐的客厅比梅里屯的舞池更难穿行。"
    n "舞池里人们看你是否会跳舞；客厅里人们看你是否知道自己该站在哪里。"

    hide elizabeth
    hide darcy
    jump ch02_result
