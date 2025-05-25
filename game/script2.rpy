default kitchen1 = False
default kitchen2 = False

default washed = False

############################################################### DAY 2


label day2:
    play music "<loop 0>noneuclidean.wav" volume 0.5 fadeout 1.5 fadein 1.5

    scene d2_bg
    show d2_bed
    with fade
    
    pause 0.5
    show d2_bed2
    pause 0.2
    show d2_bed3 with vpunch
    pause 0.05
    play sound "breath.wav" 
    show d2_bed4 
    pause 0.1
    jump bedroomd2

label bedroomd2:
    scene d2_bg
    show d2_bedroom_1
    show d2_bedroom_2
    show d2_bedroom_3
    with fade1

    pause 0.75
    "..."
    "Even in my sleep I can't have a break."

    pause 0.75

    "I'm so tired, but I can't sleep."
    "I don't wanna do anything."
    $ pcchecked = False
    $ ate = False
    $ bathvisited = False

    jump menu2

label menu2:
    menu:
        "Check my PC" if not pcchecked:
            $ actions_taken.append("d2_pcchecked")
            jump pcd2

        "Eat something" if not ate:
            $ actions_taken.append("d2_ate")
            if kitchen2:
                "Aaah what the fuck! {w=0.5}{nw}"
                jump kitchend2

            elif kitchen1:
                "I don't want to go to the kitchen."
                $ kitchen2 = True
                jump menu2
            
            else:
                "Not hungry."
                $ kitchen1 = True
                jump menu2
            

        "Go wash up" if not bathvisited:
            $ actions_taken.append("d2_bathvisited")
            "Right."
            "Maybe I will feel better."
            jump bathroomd2


label pcd2:
    $ pcchecked = True
    scene d2_pc
    play sound "chair.mp3"
    with fade1

    pause 0.75   
    play sound "click.mp3" volume 1.5

    call screen desktop(2)
    jump expression _return


label d2_game:
    #show infinite_load
    "Argh, why is it not loading?!"
    "Is the wifi here so terrible that I can't even play memories???"
    call screen desktop(2)
    jump expression _return

label d2_shutdown:
    scene d2_bg
    show d2_bedroom_1
    show d2_bedroom_2
    show d2_bedroom_3
    with fade1
    jump menu2

label d2_messages:
    play sound "click.mp3" volume 1.5
    $ reset_chats()
    window hide
    show screen chat_messages_view(2)

    f "Cooked instant noodles and there was somehow" (c="grizzley rizzly bear")
    f "A BUG IN THE BOILING POT"
    f "I was hungry af..." 
    f "so i dumped the bug and water down the drain n ate the noodles"
    f "If i die it was bc of the bug"
    y "lmao" (c="grizzley rizzly bear")
    f "Heyy, what's up?"
    y "nothing"
    f "Cool"

    f "You won't believe what happen!" (c="grizzley rizzly bear")
    f "I bought light sensitive color powder for my project, I accidentally let it go under the sun."
    f "LIGHT REACTIVE EVEN IN POWDER FORM"
    f "I'm so stupid... now I have to go buy new one...TmT"
    f "Hope you are doing well!"
    f "Text me back if you can!"

    m "Are you coming home for the holidays?" (c="Mom")
    y "no I will be at #### house"  (c="Mom")
    m "Alright then, you guys have fun!"
    m "Love and kisses!"
    m "Hey, you should pick up the phone when I call you."
    m "Call me."
    m "Do you want me to bring you more food today?"
    m "I will bring anyways, check your mailbox."
    
    l "I'm sorry for yelling at you yesterday... I'm not feeling well."  (c="Pookie")
    l "I'm not making excuses of course, I'm really sorry."
    l "Please pick up my calls :("
    y "I miss you." (c="Pookie")
    y "I wish you would reply to me."
    
    pause 20 ## 10 seconds to explore

    "Of course... Why am I getting my hopes up."
    "All you do now is haunt me."

    hide screen chat_messages_view

    scene d2_bg
    show d2_bedroom_1
    show d2_bedroom_2
    show d2_bedroom_3
    with fade1

    jump menu2

label bathroomd2:
    play sound "door.mp3"
    scene d2_bg
    show d2_bathroom_1
    show d2_bathroom_2
    show d2_bathroom_3
    with fade1

    pause 0.75

    menu:
        "Look closer":
            scene d2_bg
            show d2_mirror_1
            show d2_mirror_2
            with fade1

            pause 0.75
            "..."
            "Why did this happen?"
            "This isn't fair! We made a promise."
            "How could you leave me here?"
            "{cps=50}No..."
            "{cps=0}{color=#f00}HOW DARE YOU.{/color} {w=1}{nw}"

            play sound "glass.mp3"
            show d2_mirror_3
            with hpunch 
            pause 0.75
            "Ugh...  {w=0.5} that hurts."
            "Now I have to clean up the shards."

            scene d2_blood
            with fade1

            pause 0.75
            "Just break everything. Of course, why not?"

            scene d2_bg
            show d2_bathroom_1
            show d2_bathroom_2
            show d2_bathroom_3
            with fade1
            pause 0.5
            "Maybe I should try to go back to sleep."
            "And wake up in a better mood..."
            
            stop music
            jump day3

        "Wash up" if not washed:
            play sound "tapwater.wav"
            scene d1_sink with fade
            pause 0.5
            "Didn't help at all."


            $ washed = True
            jump bathroomd2


label kitchend2:
    play sound "door.mp3"
    scene d2_kitchen with fade1
    pause 0.5

    "There's glass shards on the floor."
    "Whatever, I will clean it later."

    $ ate = True
    
    jump menu2
