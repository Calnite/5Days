default phonebed = False
default bath1 = False
default bath2 = False

############################################################### DAY 4


label day4:
    scene d4_bg
    show d4_bed
    with fade1
    pause 0.5

    "..."

    scene black with fade1
    play sound "cry.wav"
    pause 3

    play music "<loop 0>umbra_draft.mp3" volume 0.15 fadeout 1.5 fadein 1.5

    scene d4_bg
    show d4_bed
    with fade1
    pause 0.5

    "My head hurts."

    if kitchencleaned:
        if attach:
            jump sleepending
        else:
            jump bedroomd4
    else:
        jump sleepending

label sleepending:
    "I should just go back to sleep."

    scene black with fade1
    pause 1.0
    
    nvl clear 
    n "I'm so tired... I should rest. {w=2} {nw}"
    n "...I wish I would never wake up. {w=2} {nw}"
    n "if I do I wish I would wake up next to you. {w=2} {nw}"
    n "I hope this nightmare is over soon. {w=2} {nw}"
    
    show text "Sleeping Ending" with dissolve
    pause 2

    hide text with fade
    pause 1.0

    show text "Thank you for playing!" with dissolve
    pause 2

    hide text with fade
    pause 1.0

    scene main_menu with dissolve1
    return 


label bedroomd4:
    play sound "blanket.mp3" fadein 1.5
    scene d4_bg
    show d4_bedroom_1
    show d4_bedroom_2
    show d4_bedroom_3
    with fade1

    pause 0.75

    "Why did I wake up..."
    "There's nothing left. No one left."
    "I'm all alone..."

    $ pcchecked = False
    $ ate = False
    $ bathvisited = False
    $ phonebed = False

    jump menu4

label menu4:
    menu:
        "Check my PC" if not pcchecked:
            $ phonebed = True
            $ actions_taken.append("d4_pcchecked")
            
            "You left me so suddenly... and took everything with you."
            "No matter what I do...I'm so lonely without you."
            jump pcd4

        "Eat something" if not ate:
            $ phonebed = True
            $ actions_taken.append("d4_ate")
            if kitchen2:
                "Fine..."
                jump kitchend4

            elif kitchen1:
                "I don't think I have food in the kitchen."
                $ kitchen2 = True
                jump menu4
            
            else:
                "Not hungry."
                $ kitchen1 = True
                jump menu4
            
        "Go wash up" if not bathvisited:
            $ actions_taken.append("d4_bathvisited")
            $ phonebed = True
            if bath2:
                "Fine..."
                jump bathroomd4

            elif bath1:
                "I should just go to sleep."
                $ bath2 = True
                jump menu4
            
            else:
                "What's the point? I am fine like this."
                $ bath1 = True
                jump menu4

        "Play on the phone in bed" if phonebed: 
            "I will play on the phone for a bit."
            "At least I can do that..."
            jump day5
            


label pcd4:
    $ pcchecked = True
    scene d4_pc
    play sound "chair.mp3"
    with fade1
    pause 0.75   
    play sound "click.mp3" volume 1.5
    

    call screen desktop(4)
    jump expression _return


label d4_game:
    #show infinite_load
    "...it's never going to load."
    call screen desktop(4)
    jump expression _return

label d4_shutdown:
    scene d4_bg
    show d4_bedroom_1
    show d4_bedroom_2
    show d4_bedroom_3
    with fade1
    "I don't feel like doing anything."
    jump menu4

label d4_messages:
    play sound "click.mp3" volume 1.5
    $ reset_chats()
    window hide
    show screen chat_messages_view(4)

    f "Cooked instant noodles and there was somehow" (c="grizzley rizzly bear")
    f "A BUG IN THE BOILING POT"
    f "I was hungry af..." 
    f "so i dumped the bug and water down the drain n ate the noodles"
    f "If i die it was bc of the bug"
    y "lmao" (c="grizzley rizzly bear")
    f "Heyy, what's up?"
    y "nothing"
    f "Cool"
    f "You won't believe what happen!" 
    f "I bought light sensitive color powder for my project"
    f "n I accidentally let it go under the sun."
    f "LIGHT REACTIVE EVEN IN POWDER FORM"
    f "I'm so stupid... now I have to go buy new one...TmT"
    f "Hope you are doing well!"
    f "Text me back if you can!"

    f "There is this one book i want on that overstock website"  (c="grizzley rizzly bear")
    f "and i've literally missed it TWICE already by a few minutes..."
    f "hey, getting very worried..."
    f "please respond"

    m "Are you coming home for the holidays?" (c="Mom")
    y "no I will be at #### house" (c="Mom")
    m "Alright then, you guys have fun!"
    m "Love and kisses!"
    m "Hey, you should pick up the phone when I call you."
    m "Call me."
    m "Do you want me to bring you more food today?"
    m "I will bring anyways, check your mailbox."
    m "Did you check your mailbox?"
    m "I made your favorite dish ♥"
    m "Love and kisses!"
    m "Honey, pick up the phone."
    
    l "I'm sorry for yelling at you yesterday... I'm not feeling well."  (c="Pookie")
    l "I'm not making excuses of course, I'm really sorry."
    l "Please pick up my calls :("
    y "I miss you." (c="Pookie")
    y "I wish you would reply to me."
    
    pause 20 ## 10 seconds to explore

    "..."

    hide screen chat_messages_view

    scene d4_bg
    show d4_bedroom_1
    show d4_bedroom_2
    show d4_bedroom_3
    with fade1

    jump menu4

label kitchend4:
    play sound "door.mp3"
    scene d4_kitchen with fade1

    "This kitchen is really depressing."
    "I'm really not hungry."
    "I just want to sleep."
    
    scene d4_bg
    show d4_bedroom_1
    show d4_bedroom_2
    show d4_bedroom_3
    with fade1

    jump menu4


label bathroomd4:
    play sound "door.mp3"
    scene d4_bg
    show d4_bathroom_1
    show d4_bathroom_2
    show d4_bathroom_3
    with fade1

    pause 0.75
    "It's darker than usual."

    pause 0.75
    scene d4_bg
    show d4_mirror_1
    show d4_mirror_2
    show d4_mirror_3
    with fade1

    pause 0.75
    "The mark will be here forever."
    "Unlike you."
    "I've been fighting so hard, but... I can't bring you back."
    pause 1.0
    "Why am I torturing myself."
    pause 1.0
    "Why are you torturing me."

    jump menu4
