
default w = Character("?", what_color="#40be20" )

############################################################### DAY 3


label day3:
    $ seen_todays_messages = False
    play music "<loop 0>bedbug.wav" volume 0.5 fadeout 1.5 fadein 1.5

    scene d3_bg
    show d3_bed
    with fade1
    pause 1.0

    jump bedroomd3

label bedroomd3:
    play sound "blanket.mp3" fadein 1.5
    scene d3_bg
    show d3_bedroom_1
    show d3_bedroom_2
    show d3_bedroom_3
    with fade1

    pause 0.75
    "My hand...  {w=0.5} I'm an idiot."
    "If... I had just did the right thing, would it have changed anything?"
    "Maybe it's just my curse."

    $ pcchecked = False
    $ ate = False
    $ bathvisited = False

    jump menu3

label menu3:
    menu:
        "Check my PC" if not pcchecked:
            $ actions_taken.append("d3_pcchecked")
            $ pcchecked = True
            "The last time we chatted...{w=0.5} I should have been nicer to you."
            "I sound like an asshole... You didn't deserved it."
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

    pause 0.75
    "I should do something productive..."
    play sound "click.mp3" volume 1.5

    call screen desktop(3)
    jump expression _return

label d3_messages_cancel:
    $ pcchecked = True
    scene d3_pc
    call screen desktop(3)
    jump expression _return

label d3_browser:
    show d3_browser
    "...Ugh."
    hide d3_browser
    call screen desktop(3)
    jump expression _return

label d3_game:
    #show infinite_load
    "Argh, why is it not loading?!"
    "Is the wifi here so terrible that I can't even play memories???"
    call screen desktop(3)
    jump expression _return

label d3_shutdown:
    "...Whatever."
    scene d3_bg
    show d3_bedroom_1
    show d3_bedroom_2
    show d3_bedroom_3
    with fade1
    jump menu3

label d3_messages:
    play sound "click.mp3" volume 1.5
    #$ reset_chats()
    window hide
    show screen chat_messages_view(3)
    $ day0word = "4 days ago"
    $ day1word = "3 days ago"
    $ day2word = "2 days ago"
    $ day3word = "yesterday"
    #f "Cooked instant noodles and there was somehow" (c="grizzley rizzly bear")
    #f "A BUG IN THE BOILING POT"
    #f "I was hungry af..."
    #f "so i dumped the bug and water down the drain n ate the noodles"
    #f "If i die it was bc of the bug"
    #y "lmao" (c="grizzley rizzly bear")
    #f "Heyy, what's up?"
    #y "nothing"
    #f "Cool"
    #f "You won't believe what happen!"
    #f "I bought light sensitive color powder for my project"
    #f "n I accidentally let it go under the sun."
    #f "LIGHT REACTIVE EVEN IN POWDER FORM"
    #f "I'm so stupid... now I have to go buy new one...TmT"
    #f "Hope you are doing well!"
    #f "Text me back if you can!"
    d "[day3word]" (c="grizzley rizzly bear")
    f "There is this one book i want on that overstock website" (c="grizzley rizzly bear")
    f "and i've literally missed it TWICE already by a few minutes..."

    #m "Are you coming home for the holidays?" (c="Mom")
    #y "no I will be at #### house" (c="Mom")
    #m "Alright then, you guys have fun!"
    #m "Love and kisses!"
    #m "Hey, you should pick up the phone when I call you."
    #m "Call me."
    #m "Do you want me to bring you more food today?"
    #m "I will bring anyways, check your mailbox."
    d "[day3word]" (c="Mom")
    m "Did you check your mailbox?" (c="Mom")
    m "I made your favorite dish ♥"
    m "Love and kisses!"

    #l "I'm sorry for yelling at you yesterday... I'm not feeling well."  (c="Pookie")
    #l "I'm not making excuses of course, I'm really sorry."
    #l "Please pick up my calls :("
    #y "I miss you." (c="Pookie")
    #y "I wish you would reply to me."
label d3_post_messages:
    pause 20 ## 10 seconds to explore

    "Of course... Why am I getting my hopes up."
    "All you do now is haunt me."

    hide screen chat_messages_view

    scene d3_bg
    show d3_bedroom_1
    show d3_bedroom_2
    show d3_bedroom_3
    with fade1

    jump menu3


label bathroomd3:
    play sound "door.mp3" fadein 1.5
    scene d3_bg
    show d3_bathroom_1
    show d3_bathroom_2
    show d3_bathroom_3
    with fade1

    pause 0.75

    if avoid:
        "I threw away your toothbrush."
        "...I can still take it fro mthe trashcan."
        "It's still not to late..."
        menu:
            "Take it out the trashcan":
                "I will wash it and put it away."
                $ avoid = False

            "Leave it":
                "I shouldn't be so indecisive."

    elif attach:
        "...your toothbrush."
        "I didn't manage to throw it away."
        menu:
            "Throw it away":
                $ avoid = True
                $ attach = False
                "I won't be needing this any more."

            "Put it away":
                "If I can't throw it away I have to put it away."

            "Leave it":
                "I can throw it away later."


    else:
        "..."

    "The mirror... it's cracked."
    "...of course it is."

    menu:
        "Look at the mirror":
            "Why did I have to do that..."
            "I will get a scar."
            scene d3_bg
            show d3_mirror_1
            show d3_mirror_2
            show d3_mirror_3
            with fade1
            pause 0.5
            "If I had just said something different that day. If I had noticed something..."
            "Anything, that could have saved you."
            "No... {w=0.5}I have noticed."
            "I should have done something."
            "Maybe I could have saved myself too."
            "If I could see your face and hear your voice {w=0.5} just one more time."
            "..."
            "I loved you so much."

            scene d3_bg
            show d3_bedroom_1
            show d3_bedroom_2
            show d3_bedroom_3
            with fade1
            pause 0.5

            jump menu3

        "Wash up":
            play sound "tapwater.wav"
            scene d3_sink with fade
            pause 0.5
            "It's kinda difficult to wash up with my hand like this."

            jump menu3


label kitchend3:
    play sound "door.mp3" fadein 1.5
    scene d3_kitchen with fade1
    pause 0.5
    "I'm feeling weak. I must be hungry."
    "Ugh... what a mess."
    "I didn't clean the shards yesterday."
    "Why am I like this..."

    menu:
        "Clean it up":
            "There we go... It's the best I can do right now."
            $ kitchencleaned = True

        "Leave it, I can't clean properly now.":
            "I can clean it later."

    "I'm almost out of food, why didn't I stock up?"

    play sound "doorbell.mp3" volume 0.4
    pause 1.0
    "Someone's at the door..."

    jump doord3

label doord3:
    play sound "door.mp3" fadein 1.5
    scene d3_bg
    show d3_door_1
    show d3_door_2
    show d3_door_3
    with fade1
    pause 0.5

    show d3_doorout with fade
    stop music
    pause 0.5
    "..."
    w "Hey!"
    "Hello?"
    w "It's been a while since I heard from you, so I came to check up."
    w "How are you doing?"
    menu:
        "I'm fine":
            "... I'm fine."
            w "Good to hear..."
            w "Have you been to work then? Are you working from home?"
            "...oh I- {w=0.5} {nw}"
            w "Huh? Don't tell me you are missing work."
            w "It's been a few days already."
            w "You have enough time and you are fine now."
            w "How long are you going to keep being lazy?"
            "..."
            "Leave..."
            w "I came out here to check up on you and this is my thank?"
            w "...you are such a {w=0.5} {nw}"
            "{cps=0}LEAVE!!! {w=1} {nw}" with hpunch

            scene black
            jump day4

        "I'm not feeling well":
            "I'm not feeling well, actually..."
            w "What?"
            "...The past few days hasen't been to good."
            w "Awh cmon, It's been a few days already."
            w "How long are you going to keep being lazy?"
            "..."
            "Leave..."
            w "I came out here to check up on you and this is my thank?"
            w "...you are such a {w=0.5} {nw}"
            "{cps=0}LEAVE!!! {w=1} {nw}" with hpunch

            scene black
            jump day4
