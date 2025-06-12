
default w = Character("?", what_color="#40be20", ctc="ctc_animation", ctc_position="fixed")

default expressed = False

############################################################### DAY 3


label day3:
    $ seen_todays_messages = False
    play music "<loop 0>foam.wav" volume 0.6 fadeout 2 fadein 2

    scene d3_bed
    with fade1
    pause 3

    jump bedroomd3

label bedroomd3:
    play sound "blanket.mp3" fadein 1.5
    scene d3_bedroom
    with fade1

    pause 0.5
    if washed:
        "If... I could go back in time, would it have changed anything?"
        "Maybe it's just my curse."
    else:
        "My hand... I'm an idiot."
        "I should have controlled my temper. I didn't have to lash out like that."
    
    $ pcchecked = False
    $ ate = False
    $ bathvisited = False

    jump menu3

label menu3:
    menu:
        "Check my PC" if not pcchecked:
            $ actions_taken.append("d3_pcchecked")
            $ pcchecked = True
            jump pcd3

        "Eat something" if not ate:
            $ actions_taken.append("d3_ate")
            $ ate = True
            jump kitchend3

        "Go wash up" if not bathvisited:
            $ bathvisited = True
            $ actions_taken.append("d3_bathvisited")
            "Ugh, my head is not in the right space."
            jump bathroomd3


label pcd3:
    $ pcchecked = True
    scene d3_pc
    play sound "chair.mp3"
    with fade1
    call screen desktop(3)
    jump expression _return

label d3_messages_cancel:
    $ pcchecked = True
    scene d3_pc
    call screen desktop(3)
    jump expression _return

label d3_browser:
    show d3_browser:
        xalign 0.5
        yalign 0.3
    "...Ugh."
    hide d3_browser
    call screen desktop(3)
    jump expression _return

label d3_game:
    #show infinite_load
    "I shouldn't have bought this game..."
    call screen desktop(3)
    jump expression _return

label d3_shutdown:
    "The last time we talked... I should have been nicer to you."
    "You didn't deserve it."
    scene d3_bedroom
    with fade1
    jump menu3

label d3_messages:
    play sound "click.mp3" volume 1.5
    $ reset_chats()
    window hide
    show screen chat_messages_view(3)
    $ day0word = "older messages"
    $ day1word = "##/##/##"
    $ day2word = "##/##/##"
    $ day3word = "new messages"

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

    d "[day3word]" (c="grizzley rizzly bear")
    f "There is this book i want on the overstock website" (c="grizzley rizzly bear")
    f "and it keep selling out!!!" 
    f "i've literally missed it TWICE already by a few minutes..."

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
    d "[day3word]" (c="Mom")
    m "How are you feeling, honey?" (c="Mom")
    m "Did you finish your leftovers? Do you want me to bring you some more?"

    d "[day0word]" (c="Dove")
    l "I'm sorry for yelling at you yesterday... I'm not feeling well."  (c="Dove")
    l "I'm not making excuses of course, I'm really sorry."
    l "Please pick up my calls :("
    y "I miss you." (c="Dove")
    y "I wish you would reply to me."
label d3_post_messages:
    pause 30

    menu:
        "Continue reading":
            jump d3_messages

        "Close Chat":
            hide screen chat_messages_view
            call screen desktop(3)
            jump expression _return

    jump menu3


label bathroomd3:
    play sound "door.mp3" fadein 1.5
    if washed:
        scene d3_bathroom with fade1
        pause 0.75

    else:
        scene d3_bathroomcracked with fade1
        pause 0.75
        "The bathroom smells of bleach and regret. I scrubbed away the blood but not the memories."


    if not avoid and attach:
        menu:
            "Throw it away":
                $ avoid = True
                "... There's no need to keep a brush."
                "But my hand shakes as I drop it in the trash."
                "This isn't betrayal... is it?"

            "Leave it there":
                $ attach = True
                "I won't throw your things away.{w=0.5}\nBesides... what if you need it when you come back?"
                "I'll keep everything exactly as you left it.\nJust in case."

    elif washed:
        "I should fix the light soon... or at least call someone to do it."
    else:
        "The mirror... it's cracked.{w=0.5}\n...of course it is."
        "Why did I do that..."


    menu:
        "Look at the mirror":
            if washed:
                scene d3_mirror with fade1
                pause 0.5
                "A stranger wearing my face."

            else:
                scene d3_mirrorcracked with fade1
                pause 0.5
                "Why are you judging me?"
            
            "If I had just said something different that day.{w=0.5}\n If I had noticed something...anything."
            "No...I have noticed.{w=0.5}\nI should have done something."
            "Maybe I could have saved myself, too."
            "If I could see your face and hear your voice {w=0.5} just one more time."
            "...I miss you."
            "I love you."

            scene d3_bedroom
            with fade1
            pause 0.5

            jump menu3

        "Wash up":
            play sound "tapwater.wav"
            scene d3_sink with fade
            pause 0.5
            if washed:
                "Refreshing myself should help me feel better."

            else:
                "It's kinda difficult to wash up with my hand like this."

            jump menu3


label kitchend3:
    play sound "door.mp3" fadein 1.5
    scene d3_kitchen with fade1
    pause 0.5
    
    "If I eat like a living person... maybe I'll start feeling alive again."

    if not kitchencleaned:
        "I didn't clean the shards yesterday."
        "Why am I like this..."
        menu:
            "Clean it":
                "I should clean it..."
                play sound "glassclean.mp3"
                "The trash bin swallows what's broken. If only my emotions could be disposed of so easily."
                $ kitchencleaned = True

            "Leave it":
                "I should clean it... But what's the point? More things will keep breaking."

    else:
        "I'm almost out of food..."
    
    play sound "doorbell.mp3" volume 0.2
    pause 1.0
    "Someone's at the door..."

    jump doord3

label doord3:
    play sound "door.mp3" fadein 1.5
    scene d3_door
    with fade1
    pause 0.5

    show d3_doorout with fade
    pause 0.5
    "..."
    w "Hey!"
    "Hello?"
    w "It's been a while since I heard from you, so I came to check up."
    w "How are you doing?"
    menu:
        "I'm managing":
            "I'm... managing."
            w "Good to hear..."
            w "Have you been to work then? Are you working from home?"
            "...oh I- {w=0.5} {nw}"
            w "Huh? Don't tell me you are missing work."
            w "Christ, it's been weeks!"
            "{i}...Weeks?{/i}"
            w "If you are fine now, you shouldn't miss work."
            "..."
            "You don't have to worry about that."
            w "How long are you going to keep being lazy?"
            "Leave..."
            w "What? I came out here to check up on you, and this is my thank?"
            w "...you are such a {w=0.5} {nw}"
            "{cps=0}LEAVE!!! {w=1} {nw}" with hpunch


        "I'm not feeling well":
            "I'm not feeling well, actually...\nThe past few days haven't been good."
            w "Oh come on... It's been a few weeks already."
            "{i}...Weeks?{/i}"
            w "I think you are just dragging this out..."
            "..."
            w "You can't keep dwelling on it. It's like you are not even trying!"
            "What? You don't get to say that. How would you know?"
            w "I have been pretty understanding so far, but... weeks?"
            "Understanding?\nThen why don't you understand that I'm trying?"
            "You don't get to say when I should stop feeling."
            "It doesn't work like that..."
            "You don't understand me because you didn't put yourself in my shoes."
            w "What are you talking about? I have lost someone too.\nIt's not unique to you."
            "You should leave."
            $ expressed = True

    stop music fadeout 2
    scene black with fade1
    jump day4
