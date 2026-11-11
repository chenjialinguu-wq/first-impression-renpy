label family_risk_scene:
    scene bg_meryton_ball
    with fade
    show mrs_bennet ball proud at sprite_left
    show elizabeth ball serious at sprite_right
    mb "我就知道！宾利先生一定喜欢简。没有人会请一个自己不喜欢的姑娘跳两支舞。"
    e "妈妈，也许宾利先生的感情还不需要由整个梅里屯共同见证。"
    mb "胡说。若别人不看见，高兴岂不是只剩一半？"
    n "伊丽莎白环顾舞厅。母亲的声音、妹妹们的笑声、旁人的眼光，一切都在提醒她：家庭也是一种公开表演。"
    menu:
        "你先处理哪件事？"
        "劝母亲降低声音。":
            $ watched_family += 1
            show mrs_bennet home directing at sprite_left
            e "妈妈，高兴若太响，容易惊走猎物。"
            mb "你这孩子！我不过是高兴。"
            e "我知道，所以我才希望高兴能活得久一点。"
        "提醒自己不要过早替简安排未来。":
            $ insight += 1
            $ protected_jane += 1
            show elizabeth ball serious at sprite_right
            e "简今晚很开心，这已经足够了。"
            e "我不能像妈妈那样，刚看见一支舞，就替她走完一生。"
        "暂时不插手，只继续观察。":
            $ insight += 1
            show elizabeth ball serious at sprite_right
            n "伊丽莎白没有立刻开口。"
            n "她发现，旁观有时比反驳更能看清一个家庭的轮廓。"
    n "舞会的音乐渐渐变慢。蜡烛烧短，谈话却愈发明亮。"
    jump carriage_home_scene
