label carriage_scene:
    scene bg_carriage_night
    with fade
    show mrs_bennet home directing at sprite_left
    show jane ball neutral at sprite_center
    show elizabeth ball neutral at sprite_right
    n "夜色降下来时，马车向梅里屯驶去。"
    n "车轮声、裙摆摩擦声、班纳特太太的叮嘱声，一同构成了出门前最后的家庭乐章。"
    mb "简，你今晚一定要多笑。不要太多，显得轻浮；也不要太少，显得冷淡。"
    mb "丽萃，你也是。不要说太多聪明话，男人不总是喜欢女人太聪明。"
    menu:
        "你在马车中如何回应？"
        "若聪明是缺点，我恐怕已经无法补救。":
            $ pride += 1
            $ insight += 1
            show elizabeth ball neutral at sprite_right
            e "有些缺点已经太晚了，母亲。"
            mb "你这孩子，到了舞会上可别这样回答别人。"
        "我会尽量得体，至少不让妈妈太忧心。":
            show elizabeth ball neutral at sprite_right
            e "我会尽量少制造麻烦。"
            mb "这话听着倒还像样。"
        "简今晚只需做自己，已经足够好了。":
            $ sister_bond += 1
            $ protected_jane += 1
            show elizabeth ball neutral at sprite_right
            e "简不用多做什么。她本来就足够好了。"
            j "丽萃……"
            mb "当然，简是很好。不过再多笑一点也不会损害美德。"
    n "伊丽莎白看向窗外。"
    n "她知道今晚会有观察、比较、赞美和闲话。她只是没有想到，自己也会成为别人的一句闲话。"
    jump ball_scene
