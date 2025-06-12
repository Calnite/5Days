default phonebed = False
default bath1 = False
default bath2 = False

############################################################### DAY 4

label day4:
    $ seen_todays_messages = False
    scene black with fade1
    pause 0.5
    play sound "cry.wav" volume 0.8 
    pause 3

    play music "<loop 0>bedbug.wav" volume 0.8 fadeout 2 fadein 2

    scene d4_bg
    show d4_bed
    with fade1
    pause 0.5

    "My head hurts."
    "I haven't cried in a while..."

    if kitchencleaned or avoid or expressed:
        
        jump bedroomd4

    else:
        jump dreamending


label bedroomd4:
    play sound "blanket.mp3" fadein 1.5
    scene d4_bedroom with fade1

    pause 0.75
    "What's the point of getting up? Of eating? Of anything?"
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
            "Maybe if I go through the motions... maybe I'll fool myself into caring."
            jump pcd4

        "Eat something" if not ate:
            $ phonebed = True
            $ actions_taken.append("d4_ate")
            if kitchen2:
                "Fine... I'll feed this worthless body."
                jump kitchend4

            elif kitchen1:
                "There's nothing in the kitchen that I want."
                $ kitchen2 = True
                jump menu4

            else:
                "Hunger comes and goes. Like everything else. Meaningless."
                $ kitchen1 = True
                jump menu4

        "Go wash up" if not bathvisited:
            $ actions_taken.append("d4_bathvisited")
            $ phonebed = True
            if bath2:
                "Fine..."
                jump bathroomd4

            elif bath1:
                "Cleanliness feels like a concern for people who still matter."
                $ bath2 = True
                jump menu4

            else:
                "Drown myself in some water more? No, thanks."
                $ bath1 = True
                jump menu4

        "Play on the phone in bed" if phonebed:
            "Maybe endless scrolling will make the hours pass faster."
            jump day5

label pcd4:
    $ pcchecked = True
    scene d4_pc
    play sound "chair.mp3"
    with fade1
    call screen desktop(4)
    jump expression _return

label d4_messages_cancel:
    $ pcchecked = True
    scene d4_pc
    call screen desktop(4)
    jump expression _return

label d4_browser:
    show d4_browser:
        xalign 0.5
        yalign 0.3
    "...There's nothing I want to see anyway."
    hide d4_browser
    call screen desktop(4)
    jump expression _return

label d4_game:
    #show infinite_load
    "...it's never going to load."
    call screen desktop(4)
    jump expression _return

label d4_shutdown:
    scene d4_bedroom with fade1
    "The words blur together. Nothing matters. Nothing helps."
    "I don't feel like doing anything."
    jump menu4

label d4_messages:
    play sound "click.mp3" volume 1.5
    #$ reset_chats()
    window hide
    show screen chat_messages_view(4)
    $ old = "older messages"
    $ day1word = "##/##/##"
    $ day2word = "##/##/##"
    $ day3word = "##/##/##"
    $ day4word = "new messages"

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
    
    d "[day4word]" (c="grizzley rizzly bear")
    f "hey, getting worried..." (c="grizzley rizzly bear")
    f "please respond"

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
    d "[day4word]" (c="Mom")
    m "Honey, pick up the phone."(c="Mom")
    m "I left you your favorite dish at the front door ♥"

    d "[day0word]" (c="Dove")
    l "I'm sorry for yelling at you yesterday... I'm not feeling well."  (c="Dove")
    l "I'm not making excuses of course, I'm really sorry."
    l "Please pick up my calls :("
    y "I miss you." (c="Dove")
    y "I wish you would reply to me."
label d4_post_messages:
    pause 30

    menu:
        "Continue reading":
            jump d4_messages

        "Close Chat":
            hide screen chat_messages_view
            call screen desktop(4)
            jump expression _return

    jump menu4

label kitchend4:
    play sound "door.mp3"
    scene d4_kitchen with fade1

    "The kitchen smells of stale air."
    "I'm to weak to eat anything."

    menu:
        "Take a short nap":
            "I'm tired..."
            "Maybe in dreams I'll find you again."
            scene d4_bg
            show d4_bed
            with fade1
            pause 0.5
            "Just a nap..."

            scene black with fade1
            jump dreamending

        "Eat something":
            "I don't have food left. I don't have the energy to cook."
            menu:
                "Buy something from the store a block away":
                    "It's much cheaper to buy from the store."
                    scene d4_door
                    with fade1
                    "Every step feels like walking through wet cement."
                    "...It will be really quick."
                    play sound "door.mp3"
                    scene takeout with fade1
                    "...What's that?"


                "Order Takeout":
                    "I guess I can treat myself this one time."
                    scene black with fade1
                    pause 0.5
                    play sound "doorbell.mp3" volume 0.2
                    scene takeout with fade1
                    "There are two bags at the front door."
            
            "Did mom bring me some food? I must have missed her message..."
            "..."
            "I should thank her tomorrow...I can't let her see me in this state."

            scene black with fade1
            stop music fadeout 2
            jump day5


label bathroomd4:
    play sound "door.mp3"
    if washed:
        scene d4_bathroom
        pause 0.5
        "It seems like the bathroom is darker than usual."
        scene d4_mirror
        "I'm slowly fading. The grime on my skin matches how I feel inside."
        "I've been fighting so hard, but... I can't bring you back."

    else:
        scene d4_bathroomcracked
        pause 0.5
        "The cracks fracture my reflection - just like my psyche."

        scene d4_mirrorcracked
        "The mark will be here forever."
        "Unlike you."
        "You left me so suddenly... and took everything with you."
        
    "No matter what I do...I'm so lonely without you."
    jump menu4
