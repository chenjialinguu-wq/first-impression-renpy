# 《第一印象》手机横屏 UI 适配
# 文件：game/mobile_ui.rpy
# 用途：让 Android 手机横屏试玩时文字、选项和对话框更易读、易点。
# 不改变剧情逻辑。

init -1 python:
    try:
        gui.text_size = 27
        gui.name_text_size = 34
        gui.interface_text_size = 25
        gui.button_text_size = 25
        gui.label_text_size = 30
        gui.notify_text_size = 23
        gui.textbox_height = 170
        gui.name_xpos = 250
        gui.name_ypos = 8
        gui.dialogue_xpos = 250
        gui.dialogue_ypos = 60
        gui.dialogue_width = 790
    except Exception:
        pass

init 10 python:
    style.say_dialogue.size = 27
    style.say_dialogue.line_spacing = 4
    style.say_label.size = 34
    style.say_label.bold = True
    style.choice_button_text.size = 28
    style.choice_button_text.line_spacing = 4
    style.menu_choice_button_text.size = 28
    style.menu_choice_button_text.line_spacing = 4
    style.choice_button.xminimum = 860
    style.choice_button.yminimum = 58
    style.choice_button.xpadding = 28
    style.choice_button.ypadding = 14
    style.button_text.size = 25
    style.default.size = 27

screen choice(items):
    style_prefix "choice"
    vbox:
        xalign 0.5
        ypos 150
        spacing 16
        for i in items:
            textbutton i.caption action i.action

screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            spacing 18
            textbutton _("回退") action Rollback()
            textbutton _("历史") action ShowMenu('history')
            textbutton _("快进") action Skip()
            textbutton _("自动") action Preference("auto-forward", "toggle")
            textbutton _("保存") action ShowMenu('save')
            textbutton _("读取") action ShowMenu('load')
            textbutton _("设置") action ShowMenu('preferences')

style quick_button is default
style quick_button_text is default

style quick_button:
    ypadding 4
    xpadding 8

style quick_button_text:
    size 18
    color "#d8d8d8"
    hover_color "#ffffff"
    selected_color "#ffffff"
