label ch02_country_road_scene:

    scene bg_country_road_rain
    with fade

    show elizabeth home neutral at sprite_big_center

    n "通往尼日斐的路比伊丽莎白记忆中更长。"
    n "雨后的乡间小路泥泞而湿冷，篱笆上挂着水珠，远处的庄园在雾气里显得安静而疏离。"

    if walked_in_mud:
        n "她的裙摆很快沾上泥点。"
        n "每一步都让她离简更近，也让她离尼日斐所谓的体面更远。"
    else:
        n "她尽量避开泥水，却很快意识到，通往姐姐病榻的路不可能永远保持整洁。"

    menu:
        "步行途中，你心里最强烈的念头是什么？"

        "只要简需要我，旁人的眼光不重要。":
            $ jane_health_care += 1
            $ pride += 1
            e "若有人觉得三英里的泥路比病中的姐姐更值得注意，那正说明他们的眼睛长错了地方。"

        "尼日斐的人一定会评价我。":
            $ class_pressure += 2
            e "她已经能想象宾利姐妹看见她裙摆时的目光。"
            e "那种目光不会弄脏布料，却能弄脏一个人的心情。"

        "这正是观察尼日斐的好机会。":
            $ insight += 2
            e "一座房子如何接待一个沾泥的访客，往往比它如何接待一位盛装小姐更能说明问题。"

    hide elizabeth
    jump ch02_bedroom_scene
