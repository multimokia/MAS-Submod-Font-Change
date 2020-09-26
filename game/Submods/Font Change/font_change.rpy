init -990 python in mas_submod_utils:
    fc_submod = Submod(
        author="multimokia",
        name="Font Change",
        description="A submod that changes the font of dialogues into Monika's font.",
        version="3.0.2",
        version_updates={
            "multimokia_font_change_v3_0_1": "multimokia_font_change_v3_0_2"
        }
    )

label multimokia_font_change_v3_0_1(version="v3_0_1"):
    return

label multimokia_font_change_v3_0_2(version="v3_0_2"):
    $ store.mas_utils.trydel(renpy.config.gamedir + "/Submods/Font Change/mod_assets")
    return

init -989 python in fc_utils:
    import store

    #Register the updater if needed
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod=store.mas_submod_utils.fc_submod,
            user_name="multimokia",
            repository_name="MAS-Submod-Font-Change",
            tag_formatter=lambda x: x[x.index('_') + 1:],
            update_dir="",
            attachment_id=None,
        )

#START: Styledefs
#Create these styles to be used later
init -1:
    style journal_monika is normal:
        font "mod_assets/font/m1_fixed.ttf"
        size 34

    style journal_monika_slow is default_monika:
        font "mod_assets/font/m1_fixed.ttf"
        size 34


#START: Overrides
init -1 python:
    gui.history_text_xpos += 3
    gui.history_text_ypos -= 5
    # gui.text_xpos = 268
    gui.text_ypos = 43

    style.hyperlink_text.font = "mod_assets/font/m1_fixed.ttf"
    style.hyperlink_text.size = 34

    style.history_name_text.font = "mod_assets/font/m1_fixed.ttf"
    style.history_name_text.size = 35

    style.history_text.font = "mod_assets/font/m1_fixed.ttf"
    style.history_text.size = 35

init 6 python:
    #These are used in place of the ones in script-ch30.rpy so we get our custom font
    def mas_enableTextSpeed():
        """
        Enables text speed
        """
        style.say_dialogue = style.journal_monika
        store.mas_globals.text_speed_enabled = True

    def mas_disableTextSpeed():
        """
        Disables text speed
        """
        style.say_dialogue = style.journal_monika_slow
        store.mas_globals.text_speed_enabled = False
