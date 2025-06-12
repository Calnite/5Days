image ctc_animation = Animation("ctc.png", 2, "ctc2.png", 0.15, "ctc3.png", 0.15, "ctc2.png", 0.15, xpos=0.95, ypos=0.95, xanchor=1.0, yanchor=1.0)


define n = Character(" ", kind=nvl, ctc="ctc_animation", ctc_position="fixed")
define end = Character("", kind=nvl, ctc="ctc_animation", ctc_position="fixed", what_text_align=0.5, what_xalign=0.5)
define narrator = Character("", ctc="ctc_animation", ctc_position="fixed")

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

default f = ChatCharacter("grizzley rizzly bear", icon="images/friend.png", name_color="#629ebe")
default m = ChatCharacter("Mom", icon="images/mom.png", name_color="#be5e5e")
default l = ChatCharacter("Dove", icon="images/lover.png", name_color="#8f56aa")
default y = ChatCharacter("you", icon="images/you.png", name_color="#000000")
default d = ChatCharacter("date")

image jarglitch:
    "d1_jar3"
    pause 0.2
    "d1_jar4"
    pause 0.2
    "d1_jar2"
    pause 0.75
    "d1_jar4"


#label splashscreen:
#    return


############################################################### DAY 1

label start:
    scene black with fade1
    pause 1.0

    show text "{size=+10}Content warning:{/size}\nDeath, Depression, Self-harm, Blood." with dissolve
    pause 3

    hide text with fade
    pause 0.5

    show text "This Visual Novel is recommended for audiences above 16. \nFor the best experience, play with headphones at home." with dissolve
    pause 3

    hide text with fade
    pause 0.5
    scene black with fade1

    stop music fadeout 2
    play sound rain fadein 1.5 fadeout 1.5
    scene bg with fade1
    n "It's been such a long time...{w=1}\nHow many days have gone by? I can't tell.{w=3} {nw}"
    n "The sky is always dark.{w=1}\nUsually, I love gloomy weather...{w=3} {nw}"
    n "But lately I can't stand looking at it. It wears me out.{w=3} {nw}"

    nvl clear

    end "I still think about you.{w=2} {nw}"

    jump day1

label day1:
    stop sound fadeout 1.5
    play music "<loop 0>umbra.mp3" volume 0.5 fadeout 2 fadein 2

label morning:
    scene d1_bed with fade1
    pause 1

    menu:
        "wake up":
            "I'd better get up now."
            jump bedroomd1

        "sleep in" if not sleeping or dreamending:
            "The bed is too comfortable..."
            $ sleeping = True
            call morning

        "just five more minutes" if sleeping:
            $ dreamending = True
            $ sleeping = False
            "...maybe I'll wake up to your voice again."
            call morning

        "stay asleep" if dreamending:
            jump dreamending


label bedroomd1:
    scene d1_bedroom with fade1
    play sound "blanket.mp3"

    pause 0.75
    "I slept terribly... The nightmares again."
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
    call screen desktop(1)
    jump expression _return

label d1_messages_cancel:
    play sound "click.mp3" volume 1.5
    $ pcchecked = True
    scene d1_pc
    call screen desktop(1)
    jump expression _return

label d1_browser:
    play sound "click.mp3" volume 1.5
    show d1_browser:
        xalign 0.5
        yalign 0.3
    "...There's no connection. I might have forgotten to pay my bills."
    hide d1_browser
    call screen desktop(1)
    jump expression _return

label d1_game:
    play sound "click.mp3" volume 1.5
    "...It's not loading."
    call screen desktop(1)
    jump expression _return

label d1_shutdown:
    "The last message still reads 'Delivered'"
    "It's okay I can wait... you'll text or call me.\nlike you always did."
    "I will check again later."
    scene d1_bedroom with fade1
    jump menu

label d1_messages:
    play sound "click.mp3" volume 1.5
    $ reset_chats()
    window hide
    show screen chat_messages_view(1)
    $ day0word = "older messages"
    $ day1word = "new messages"

    d "[day0word]" (c="grizzley rizzly bear")
    f "Cooked instant noodles and there was somehow" (c="grizzley rizzly bear")
    f "A BUG IN THE BOILING POT"
    f "I was hungry af..."
    f "so i dumped the bug and water down the drain n ate the noodles"
    f "If i die it was bc of the bug"
    y "lmao" (c="grizzley rizzly bear")
    f "Heyy, what's up?"
    y "nothing"
    f "Cool"
    d "[day1word]"
    f "How are you?"
    f "Text me back if you can!"

    d "[day0word]" (c="Mom")
    m "Are you coming home for the holidays?" (c="Mom")
    y "no I will be at ####'s house"  (c="Mom")
    m "Alright then, you guys have fun!"
    m "Love and kisses!"
    d "[day1word]"
    m "Hey, you should pick up the phone when I call you."
    m "Call me."

    d "[day0word]" (c="Dove")
    l "I'm sorry for yelling at you yesterday... I'm not feeling well."  (c="Dove")
    l "I'm not making excuses of course, I'm really sorry."
    l "Please pick up my calls :("
    y "I miss you." (c="Dove")
    y "I wish you would reply to me."
label d1_post_messages:
    pause 40

    menu:
        "Continue reading":
            jump d1_messages

        "Close Chat":
            hide screen chat_messages_view
            call screen desktop(1)
            jump expression _return

    jump menu

label bathroomd1:
    play sound "door.mp3"
    scene d1_bathroom with fade1
    pause 0.75
    "We spend so much time getting ready together."
    "Your toothbrush is still here. Your shampoo bottle still half-empty."
    $ bathvisited = True

    menu:
        "Throw it away":
            $ avoid = True
            "... There's no need to keep it."
            "But my hand shakes as I drop it in the trash can."

        "Leave it there":
            $ attach = True
            "I won't throw your things away.\nBesides... what if you need them when you come back?"
            "I'll keep everything exactly as you left it.\nJust in case."
    
    menu:
        "Look at the mirror":
            scene d1_mirror
            with fade1
            pause 0.75
            "The stranger staring back has my face...{w=0.5}\nWhen did I become this ghost?"
            "I should wash up..."
            
            scene d1_bathroom with fade1

            play sound "brushteeth.wav"
            scene d1_sink with fade
            pause 3

            "Mechanical motions. Brush. Spit. Rinse. Repeat."
            "I do it because that's what living people do."
            "I'm not a ghost...yet."

        "Wash up":
            play sound "brushteeth.wav"
            scene d1_sink with fade
            pause 3

            "Mechanical motions. Brush. Spit. Rinse. Repeat."
            "I do it because that's what living people do."
            "I'm not a ghost...yet."
    
    jump menu

label kitchend1:
    play sound "door.mp3"
    scene d1_kitchen with fade1
    pause 0.75

    "I don't know how to get rid of the smell."
    "You always hated when I let dishes pile up.{w=0.5}\nNow the mold grows undisturbed."
    "Mom's leftovers should be in the fridge."

    scene d1_fridge
    play sound "fridge.wav"
    pause 0.75

    "Mom's leftovers... from when she visited after...{w=0.5}\nI hope it didn't spoil yet."
    "The jar looks molded, tho. Maybe I should throw it away."

    show d1_fridge2 with dissolve
    pause 0.5
    show d1_jar with dissolve

    "Urgh... Nasty."
    play sound "suspense.wav"

    pause 1.5
    "... {w=0.1} {nw}"
    pause 0.5

    show jarglitch
    pause 0.5
    scene black
    play sound "glassjar.mp3"
    pause 0.5
    stop music fadeout 2
    jump day2
