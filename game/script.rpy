


define n = Character(" ", kind=nvl)
define end = Character("", kind=nvl, what_text_align=0.5, what_xalign=0.5)

define fade1 = Fade(1.25, 0.75, 1.25)
define dissolve1 = Dissolve(1.5)

define gui.dialogue_text_outlines = [ (2, "#000005", 0, 0) ]
define gui.dialogue_outline_scaling = "linear"
define gui.charaters_text_outlines = [ (2, "#000005", 0, 0) ]
define gui.characters_outline_scaling = "linear"
style say_label:
    outlines [ ( 2, "#000005", 0, 0) ]
    outline_scaling "linear"

default dreamending = False
default sleeping = False

default kitchencleaned = False
default bathvisited = False
default pcchecked = False
default ate = False

default attach = False
default avoid = False

default actions_taken = []
default seen_todays_messages = False

default f = ChatCharacter("grizzley rizzly bear", icon="images/friend.png", name_color="#403174")
default m = ChatCharacter("Mom", icon="images/mom.png", name_color="#5b8a46")
default l = ChatCharacter("Pookie", icon="images/lover.png", name_color="#8a4660")
default y = ChatCharacter("you", icon="images/you.png", name_color="#000000")
default d = ChatCharacter("date")

label splashscreen:
    scene black
    pause 1.0

    show text "This Visual Novel is not suitable for audiences under 18." with dissolve
    pause 2

    hide text with fade
    pause 1.0

    show text "Content warning: Death, Depression, Self harm, Blood." with dissolve
    pause 2

    hide text with fade
    pause 1.0

    scene main_menu with fade
    return

############################################################### DAY 1

label start:
    stop music
    scene bg with fade1
    n "It's been such a long time...{w=2} {nw}"
    n "How many days has gone by? I can't tell.{w=2} {nw}"
    n "The sky is always dark.{w=2} {nw}"
    n "Usually, I love gloomy weather...{w=2} {nw}"
    n "But lately I can't stand looking at it.{w=2} {nw}"
    n "It wears me out.{w=2} {nw}"

    nvl clear

    end "I still think about you."

    jump day1

label day1:
    play music "<loop 0>umbra.mp3" volume 0.3 fadeout 1.5 fadein 1.5

    scene d1_bg
    show d1_bed
    with fade1
    pause 1

    menu:
        "wake up":
            "I better get up now."
            jump bedroomd1

        "sleep in":
            if dreamending:
                jump dreamending
            elif sleeping:
                jump sleepin2
            else:
                jump sleepin1


label sleepin1:
    "Just five more minutes..."
    $ sleeping = True
    jump day1

label sleepin2:
    "... I want... more time."
    $ dreamending = True
    jump day1

label dreamending:
    scene black with fade1
    pause 1.0

    scene whitebg with fade1
    show her with dissolve1
    pause 1.0

    scene whitebg with dissolve1
    pause 0.5
    nvl clear

    end "{outlinecolor=#000000}Good morning, sleepy head.{/outlinecolor} {w=1.5} {nw}"

    nvl clear

    scene whitebg with dissolve1
    show dreamend1 with dissolve1
    pause 1.0

    scene whitebg with dissolve1
    end "{outlinecolor=#000000}Good morning.{/outlinecolor} {w=1.5} {nw}"

    nvl clear

    scene black with fade1
    pause 1

    show text "Dream Ending" with dissolve
    pause 2

    hide text with fade
    pause 1.0

    show text "Thank you for playing!" with dissolve
    pause 2

    hide text with fade
    pause 1.0

    scene main_menu with dissolve1
    return

label bedroomd1:
    scene d1_bg
    show d1_bedroom_1
    show d1_bedroom_2
    show d1_bedroom_3
    with fade1
    play sound "blanket.mp3"

    pause 0.75
    "I slept terriblely. Must have been the nightmares."
    jump menu

label menu:
    menu:
        "What should I do now?"

        "Check my PC" if not pcchecked:
            $ actions_taken.append("d1_pcchecked")
            jump pcd1

        "Eat something" if not ate:
            $ actions_taken.append("d1_ate")
            jump kitchend1

        "Go wash up" if not bathvisited:
            $ actions_taken.append("d1_bathvisited")
            jump bathroomd1

label pcd1:
    $ pcchecked = True
    scene d1_pc
    play sound "chair.mp3"
    with fade1

    pause 0.75
    "Hm, I should check my messages."
    play sound "click.mp3" volume 1.5

    call screen desktop(1)
    jump expression _return

label d1_messages_cancel:
    $ pcchecked = True
    scene d1_pc
    call screen desktop(1)
    jump expression _return

label d1_browser:
    play sound "click.mp3" volume 1.5
    show d1_browser
    "...It's not loading."
    hide d1_browser
    call screen desktop(1)
    jump expression _return

label d1_game:
    play sound "click.mp3" volume 1.5
    #show infinite_load
    "...It's not loading."
    call screen desktop(1)
    jump expression _return

label d1_shutdown:
    "...Nevermind. {w=2} {nw}"
    scene d1_bg
    show d1_bedroom_1
    show d1_bedroom_2
    show d1_bedroom_3
    with fade1
    jump menu

label d1_messages:
    play sound "click.mp3" volume 1.5
    $ reset_chats() ## this gets everything set up correctly, but since you don't want any new messages to show up, only call it on day 1.
    window hide
    show screen chat_messages_view(1)
    $ day0word = "2 days ago"
    $ day1word = "yesterday"
    d "[day1word]" (c="grizzley rizzly bear")
    f "Cooked instant noodles and there was somehow" (c="grizzley rizzly bear")
    f "A BUG IN THE BOILING POT"
    f "I was hungry af..."
    f "so i dumped the bug and water down the drain n ate the noodles"
    f "If i die it was bc of the bug"
    y "lmao" (c="grizzley rizzly bear")
    f "Heyy, what's up?"
    y "nothing"
    f "Cool"

    d "[day0word]" (c="Mom")
    m "Are you coming home for the holidays?" (c="Mom")
    y "no I will be at #### house"  (c="Mom")
    m "Alright then, you guys have fun!"
    m "Love and kisses!"
    d "[day1word]"
    m "Hey, you should pick up the phone when I call you."
    m "Call me."

    d "older messages" (c="Pookie")
    l "I'm sorry for yelling at you yesterday... I'm not feeling well."  (c="Pookie")
    l "I'm not making excuses of course, I'm really sorry."
    l "Please pick up my calls :("
    y "I miss you." (c="Pookie")
    y "I wish you would reply to me."
label d1_post_messages:
    pause 30

    "...still no reply."
    "It's okay I can wait... you'll text or  call me."
    "like you always did."
    "I will check again tomorrow."
    hide screen chat_messages_view

    scene d1_bg
    show d1_bedroom_1
    show d1_bedroom_2
    show d1_bedroom_3
    with fade1

    jump menu

label bathroomd1:
    play sound "door.mp3"
    scene d1_bg
    show d1_bathroom_1
    show d1_bathroom_2
    show d1_bathroom_3
    with fade1

    pause 0.75
    "My bathroom's light is not very bright."
    "You keep reminding me to fix it."

    $ bathvisited = True

    menu:
        "You left your toothrush here."
        "Throw it away":
            $ avoid = True
            "... There's no need to keep a spare brush."

        "Leave it there":
            $ attach = True
            "I won't throw your things away."
            "I will keep it for as long as I can."

    menu:
        "Look at the mirror":
            scene d1_bg
            show d1_mirror_1
            show d1_mirror_2
            with fade1
            "...it's just me."
            pause 0.75
            "Oh...  {w=0.5} is it really me?"
            "I don't know."

            scene d1_bg
            show d1_door_1
            show d1_door_2
            show d1_door_3
            with fade1

            jump menu

        "Wash up":
            play sound "brushteeth.wav"
            scene d1_sink with fade
            pause 3

            "All done."

            scene d1_bg
            show d1_door_1
            show d1_door_2
            show d1_door_3
            with fade1

            jump menu

label kitchend1:
    play sound "door.mp3"
    scene d1_kitchen with fade1
    pause 0.75

    "The kitchen smells a bit muffing."
    "I don't know how to get rid of the smell."
    "Anyways my mom's leftover should be in the fridge."

    scene d1_fridge
    play sound "fridge.wav"
    pause 0.75

    "There it is, I hope it didn't spoiled yet."
    "The jar looks molded tho, maybe I should throw it away."

    show d1_fridge2 with dissolve
    pause 0.5
    show d1_jar with dissolve

    "Urgh... it's kinda nasty."
    play sound "suspense.wav"

    pause 1.5
    "... {w=0.1} {nw}"

    show d1_jar2 with hpunch
    pause 0.1
    scene black
    play sound "glassjar.mp3"
    pause 0.5

    stop music
    jump day2
