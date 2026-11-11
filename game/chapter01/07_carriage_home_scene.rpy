label carriage_home_scene:

    scene bg_carriage_night
    with fade

    show jane ball neutral at sprite_left
    show elizabeth ball serious at sprite_right

    j "丽萃，也许达西先生只是害羞，或是不习惯这样的场合。"

    if joked_at_darcy:
        e "简，你总是善于替别人寻找美德。哪怕那个人把美德藏得非常彻底。"
    elif public_retort:
        e "如果他是不习惯，那他今晚选择了一种很有效的方式让别人也不习惯。"
    else:
        e "也许吧。可害羞和傲慢，落到被轻慢的人耳中，声音实在相似。"

    j "我只是不愿轻易判断一个人。"

    show elizabeth ball serious at sprite_right
    e "而我有时太愿意判断。"
    e "这大概就是我们为何能做姐妹：你替世界辩护，我替世界提问。"

    menu:
        "你如何向简评价达西？"

        "他骄傲、无礼，而且自以为是。":
            $ prejudice += 2
            $ sister_bond += 1
            show elizabeth ball serious at sprite_right
            e "我并不急于讨厌一个人。但达西先生今晚显然很愿意帮我节省时间。"
            j "丽萃……"

        "他令人不快，但也许还值得观察。":
            $ insight += 2
            $ prejudice -= 1
            $ sister_bond += 1
            show elizabeth ball serious at sprite_right
            e "他令人不快。但也许，我还没有看见全部。"
            j "你这样说，我反而放心些。"

        "我不在乎他怎么看我。":
            $ pride += 2
            $ prejudice += 1
            show elizabeth home teasing at sprite_right
            e "一个傲慢男人的判断，并不会改变我是谁。"
            j "我希望你真这样想。"
            e "我至少会努力这样说。"

    n "马车驶入朗伯恩时，夜色已经沉下来。"
    n "简带着温柔的喜悦沉默，伊丽莎白则带着一句话反复醒着。"

    jump chapter_result
