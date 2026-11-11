label ch02_invitation_scene:

    scene bg_longbourn_morning_rain
    with fade

    show mrs_bennet home excited at sprite_breakfast_left
    show jane ball neutral at sprite_breakfast_center
    show elizabeth home neutral at sprite_breakfast_right

    mb "简，尼日斐花园来信了！"
    j "给我的？"
    mb "当然是给你的。宾利小姐请你今日去与她共进晚餐。"

    show elizabeth home teasing at sprite_breakfast_right
    e "听起来不像普通邀请，更像妈妈等待已久的战报。"

    show mrs_bennet home directing at sprite_breakfast_left
    mb "丽萃，别说俏皮话。简必须去，而且要骑马去。"

    show elizabeth home neutral at sprite_breakfast_right
    e "天看起来要下雨。"

    mb "正因为要下雨，才更该骑马。若雨下大了，她就只能留在尼日斐。"

    j "妈妈，这样似乎不太合适。"
    mb "合适？亲爱的，命运从不等人把鞋带系好。"

    menu:
        "你如何看待母亲让简雨天骑马去尼日斐？"

        "反对：这对简的身体太冒险。":
            $ jane_health_care += 1
            $ pride += 1
            show elizabeth home neutral at sprite_breakfast_right
            e "妈妈，若她因此受寒，宾利先生的晚餐又有什么用？"
            mb "丽萃，你总喜欢把好事说得像灾难。"
            e "有些灾难正是被人当作好事安排出来的。"

        "温和提醒简小心，尊重她自己的决定。":
            $ sister_bond += 1
            $ jane_health_care += 1
            show elizabeth home neutral at sprite_breakfast_right
            e "简，若你愿意去，至少多带一件披肩。"
            j "我会小心的。你别担心。"
            e "我会尽量少担心，但不保证成功。"

        "保持旁观，观察母亲的盘算。":
            $ insight += 1
            show elizabeth home teasing at sprite_breakfast_right
            e "我开始理解妈妈所谓的‘顺其自然’了：先把人推到雨里，再让自然发生作用。"
            mb "你这孩子！"

    n "简最终还是去了。"
    n "雨声在她离开之后变得更密，像是专为班纳特太太的计划作证。"

    hide jane
    hide elizabeth
    hide mrs_bennet

    jump ch02_jane_ill_scene
