label ch02_bedroom_scene:

    scene bg_netherfield_bedroom
    with fade

    show jane ball neutral at sprite_left
    show elizabeth ball serious at sprite_right

    n "尼日斐花园的女仆将伊丽莎白领进客房。"
    n "简躺在床上，脸色苍白，声音却仍旧温和得像在安慰别人。"

    j "丽萃，你怎么来了？路上一定很不好走。"
    e "路确实不好走。但这不是我不来的理由。"

    j "我只是有些发热。宾利先生非常关心，宾利小姐也很客气。"

    if insight >= 5:
        n "伊丽莎白听见‘客气’二字时，注意到简短暂地停了一下。"
        n "客气有时是一层薄纱，遮住的并不总是善意。"
        $ read_caroline = True

    menu:
        "你如何照顾简？"

        "专心询问她的身体状况。":
            $ jane_health_care += 2
            $ sister_bond += 1
            e "你有没有发冷？头还痛吗？她们有没有请医生？"
            j "你一来，我反而觉得自己病得更严重了。"
            e "那是因为终于有人允许你承认自己难受。"

        "轻声询问宾利是否来看过她。":
            $ sister_bond += 1
            $ insight += 1
            e "宾利先生来过吗？"
            j "来过。他很关切。"
            e "你说‘很关切’时，声音比病情好多了。"
            j "丽萃。"

        "让她先休息，自己去面对客厅。":
            $ jane_health_care += 1
            $ netherfield_reputation += 1
            e "你先睡一会儿。我去楼下，免得她们觉得朗伯恩的人全都不懂规矩。"
            j "别为了我和任何人争执。"
            e "我尽量只在必要的时候争执。"

    n "简很快重新睡去。伊丽莎白替她掖好被角，才转身下楼。"

    hide jane
    hide elizabeth
    jump ch02_drawing_room_scene
