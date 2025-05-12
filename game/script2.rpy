
############################################################### DAY 2


label bedd2:
    play music "<loop 0>non-euclidean_cycle.wav" volume 0.1 fadeout 1.5 fadein 1.5

    scene d2_bg
    show d2_bed
    with fade1

    menu:
        "wake up":

            "..."
            jump bedroomd2


        "sleep in":

            "Just five more minutes..."
            jump bedd2

label bedroomd2:
    play sound "blanket.mp3" fadein 1.5
    scene d2_bg
    show d2_bedroom_1
    show d2_bedroom_2
    show d2_bedroom_3
    with fade1

    pause 0.75
    "My head...  {w=0.5} make it stop."

    menu:
        "Check my PC":
            "Nothing I really wanna see."

            play sound "chair.mp3" fadein 1.5
            scene d2_bg
            show d2_pc_1
            show d2_pc_3
            with fade1

            pause 0.75
            "Let's check my messages."
            call screen desktop(2)
            jump expression _return

        "Go wash up":

            "Maybe I will feel better after."
            jump bathroomd2


label d2_messages:
    window hide
    show screen chat_messages_view(2)
    pause 5 ## only 5 seconds to explore, since there's nothing new to see.
    "Of course... no reply. Why am I getting my hopes up."
    "We used to be in contact everyday.{w=0.5} Now I'm just staring at our conversations."
    "No fair."
    hide screen chat_messages_view
    scene d2_bg
    show d2_bedroom_1
    show d2_bedroom_2
    show d2_bedroom_3
    with fade1

    pause 0.75
    "What's the point."
    jump bathroomd2

label d2_game:
    #show infinite_load
    "...It's not loading."
    call screen desktop(2)
    jump expression _return

label d2_shutdown:
    "...Nevermind."
    jump doord1

    play sound "click.mp3" volume 1.5
    show screen chat_messages_view(2)

label bathroomd2:
    play sound "door.mp3" fadein 1.5
    scene d2_bg
    show d2_bathroom_1
    show d2_bathroom_2
    show d2_bathroom_3
    with fade1

    pause 0.75
    "The light is irritating."

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
            "Oh, fuck me."
            "Now I have to clean up the shards."

            scene d2_blood
            with fade1

            pause 0.75
            "Why am I so stupid."
            "It's all my fault."

            jump doord2


        "Wash up":
            "Cold water."
            "Didn't help."

            jump bathroomd2


label doord2:
    play sound "door.mp3" fadein 1.5
    scene d2_bg
    show d2_door_1
    show d2_door_2
    show d2_door_3
    with fade1

    pause 0.75
    "I hate this."
    "I hate that you broke the promise."
    "I hate that you left me all by myself."
    "I hate that I feel so alone."
    "..."
    "I hate you."
    pause 0.75

    jump bedd3
