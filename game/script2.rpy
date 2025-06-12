default kitchen1 = False
default kitchen2 = False
default washed = False

default td = Character("?", what_color="#FFA500", ctc="ctc_animation", ctc_position="fixed")

############################################################### DAY 2


label day2:
    $ seen_todays_messages = False
    play music "<loop 0>noneuclidean.wav" volume 0.5 fadeout 2 fadein 2
    scene d2_bed with fade

    pause 0.5
    show d2_bed2
    pause 0.2
    show d2_bed3
    pause 0.01
    show d2_bed4
    pause 0.1
    jump bedroomd2

label bedroomd2:
    scene d2_bedroom with fade1
    play sound "breath.wav" volume 0.5
    pause 0.75
    "..."
    "Even in my sleep, you haunt me."

    pause 0.75

    "Exhaustion weighs me down like wet concrete, but closing my eyes means facing the images burned into my eyelids."
    $ pcchecked = False
    $ ate = False
    $ bathvisited = False

    jump menu2

label menu2:
    if ate:
        menu:
            "Check my PC" if not pcchecked:
                $ actions_taken.append("d2_pcchecked")
                jump pcd2

            "Go wash up" if not bathvisited:
                $ actions_taken.append("d2_bathvisited")
                "Maybe the water will wash away... something. Anything."
                jump bathroomd2

    else:
        menu:
            "Check my PC" if not pcchecked:
                $ actions_taken.append("d2_pcchecked")
                jump pcd2

            "Eat something" if not ate or kitchen1 or kitchen2:
                "The thought of food makes my stomach turn. Everything tastes like ash anyway."
                $ kitchen1 = True
                jump menu2
            
            "Try to eat something" if kitchen1 and if not ate:
                "I don't want to go to the kitchen."
                $ kitchen2 = True
                jump menu2

            "You have to eat" if kitchen2:
                "Damn, alright!"
                $ ate = True
                jump kitchend2

            "Go wash up" if not bathvisited:
                $ actions_taken.append("d2_bathvisited")
                "Maybe the water will wash away... something. Anything."
                jump bathroomd2


label pcd2:
    $ pcchecked = True
    scene d2_pc
    play sound "chair.mp3"
    with fade1
    call screen desktop(2)
    jump expression _return

label d2_messages_cancel:
    $ pcchecked = True
    scene d2_pc
    call screen desktop(2)
    jump expression _return

label d2_browser:
    show d2_browser:
        xalign 0.5
        yalign 0.3
    "...Stupid, did you forget you didn't pay the bills?"
    hide d2_browser
    call screen desktop(2)
    jump expression _return

label d2_game:
    #show infinite_load
    "Argh, why is it not loading?!"
    call screen desktop(2)
    jump expression _return

label d2_shutdown:
    "No new notifications from you. Just this... endless waiting for a reply that will never come."
    scene d2_bedroom with fade1
    jump menu2

label d2_messages:
    play sound "click.mp3" volume 1.5
    $ reset_chats()
    window hide
    show screen chat_messages_view(2)
    $ day0word = "older messages"
    $ day1word = "##/##/##"
    $ day2word = "new messages"

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
    d "[day2word]" (c="grizzley rizzly bear")
    f "You won't believe what happen!" (c="grizzley rizzly bear")
    f "I bought light sensitive color powder for my project, I accidentally let it go under the sun."
    f "LIGHT REACTIVE EVEN IN POWDER FORM"
    f "I'm so stupid... now I have to go buy new one...TmT"

    d "[day0word]" (c="Mom")
    m "Are you coming home for the holidays?" (c="Mom")
    y "no I will be at ####'s house"  (c="Mom")
    m "Alright then, you guys have fun!"
    m "Love and kisses!"
    d "[day1word]"
    m "Hey, you should pick up the phone when I call you."
    m "Call me."
    d "[day2word]" (c="Mom")
    m "Remember to get out of bed and try to get some fresh air."(c="Mom")

    d "[day0word]" (c="Dove")
    l "I'm sorry for yelling at you yesterday... I'm not feeling well."  (c="Dove")
    l "I'm not making excuses of course, I'm really sorry."
    l "Please pick up my calls :("
    y "I miss you." (c="Dove")
    y "I wish you would reply to me."
label d2_post_messages:
    pause 30

    menu:
        "Continue reading":
            jump d2_messages

        "Close Chat":
            hide screen chat_messages_view
            call screen desktop(2)
            jump expression _return

    jump menu2

label bathroomd2:
    play sound "door.mp3"
    scene d2_bathroom with fade1

    pause 0.75

    if not avoid or attach:
        "Your toothbrush is still here. Your shampoo bottle still half-empty."
        menu:
            "Throw them away":
                $ avoid = True
                "... There's no need to keep a brush."
                "But my hand shakes as I drop it in the trash."

            "Leave them there":
                $ attach = True
                "I won't throw your things away.\nBesides... what if you need them when you come back?"
                "I'll keep everything exactly as you left it.\nJust in case."

    else:
        "My bathroom's light is flickering.{w=0.5}\nYou keep reminding me to fix it."
        

    $ bathvisited = True
    menu:
        "Look closer":
            scene d2_mirror
            with fade1

            pause 0.75
            "This isn't how our story was supposed to go."
            "You promised we'd be together forever. You promised."
            "How could you leave me here alone?"
            "{cps=50}No..."
            "{cps=0}{color=#f00}HOW DARE YOU.{/color} {w=1}{nw}"

            play sound "glass.mp3"
            show d2_mirrorcracked
            with hpunch
            pause 0.75
            "ARGH"
            "It hurts...{w=0.5}\nI can still feel after all."

            scene d2_blood
            with fade1

            pause 0.75
            "Just break everything will you...{w=0.5}\n I'm so stupid. Deserved."
            "I'm so tired of this. I keep messing everything up."
            

        "Wash up" if not washed:
            play sound "tapwater.wav"
            scene d2_sink with fade
            pause 0.5
            "The water runs cold. Just like everything else in this apartment."
            "I scrub my face, but these emotions won't wash away."
            "I'm still tired."

            $ washed = True

    scene black with fade1
    "Maybe if I sleep now, I'll wake up to find this was all a terrible dream."
    stop music fadeout 2
    jump day3


label kitchend2:
    play sound "door.mp3"
    scene d2_kitchen with fade1
    pause 0.5

    "There are glass shards on the floor."

    menu:
        "Clean it":
            "I should clean it..."
            play sound "glassclean.mp3"
            "The trash bin swallows what's broken. If only my emotions could be disposed of so easily."
            $ kitchencleaned = True

        "Leave it":
            "I should clean it... But what's the point? More things will keep breaking."

    "Hunger is like a punishment for being alive."
    $ ate = True

    jump menu2


    
