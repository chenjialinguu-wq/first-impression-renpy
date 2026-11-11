label breakfast_scene:
    scene bg_longbourn_breakfast
    with fade
    show mrs_bennet home excited at sprite_breakfast_left
    show elizabeth home neutral at sprite_breakfast_right
    n "朗伯恩的早晨原本可以很安静。"
    n "如果班纳特太太没有在早餐前听说尼日斐花园租出去的话。"
    mb "你们听说了吗？尼日斐花园终于租出去了！"
    show elizabeth home teasing at sprite_breakfast_right
    e "母亲，您看起来像是已经替那位先生完成了订婚、婚礼和婚后生活的全部安排。"
    mb "伊丽莎白，不要拿正经事开玩笑。那位宾利先生一年有四五千镑！"
    show mr_bennet home neutral at sprite_breakfast_center
    mr "五千镑。这个数字听起来比许多人的德行都可靠。"
    show elizabeth home neutral at sprite_breakfast_right
    e "父亲，您这是在赞美金钱，还是在讽刺我们？"
    mr "我从不讽刺我的女儿们。"
    mr "我只是偶尔允许事实替我说话。"
    show mrs_bennet home directing at sprite_breakfast_left
    mb "班纳特先生，你必须去拜访宾利先生。你若不去，我们怎么认识他？"
    mb "若我们不认识他，他怎么会爱上简？若他不爱上简，我们一家将来怎么办？"
    hide mr_bennet home neutral
    show jane ball neutral at sprite_breakfast_center
    j "妈妈……"
    menu:
        "你如何回应母亲的热情？"
        "妈妈，您甚至还没见过他。":
            $ pride += 1
            $ insight += 1
            show elizabeth home teasing at sprite_breakfast_right
            e "我从未想到收入还能替人品作证。"
            mr "丽萃，你这话很危险。若人品不再由收入证明，那许多绅士就要失业了。"
        "若他真如传闻那样可亲，简或许会喜欢他。":
            $ sister_bond += 1
            $ protected_jane += 1
            show elizabeth home neutral at sprite_breakfast_right
            e "若他真诚、温和，又懂得欣赏简，那倒也不是坏事。"
            j "丽萃，别这样说。我们还不知道宾利先生是什么样的人。"
            e "正因为不知道，才值得稍微期待一下。"
        "五千镑一年，确实值得全郡认真对待。":
            $ insight += 1
            show elizabeth home teasing at sprite_breakfast_right
            mb "你看！连丽萃都懂这个道理。"
            e "我只是承认，金钱有时能让陌生人的缺点暂时变得模糊。"
    hide jane ball neutral
    n "班纳特太太已经把这场舞会看作命运的开端。"
    n "伊丽莎白则还不知道，真正会改变她判断的，并不是宾利先生。"
    jump carriage_scene
