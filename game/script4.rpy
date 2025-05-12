
############################################################### DAY 4


label bedd4:
    play music "<loop 0>umbra_draft.mp3" volume 0.15 fadeout 1.5 fadein 1.5
    
    scene d3_bg
    show d4_bed
    with fade1

    menu:
        "wake up":
            
            "All this sleeping makes me feel nauseous."
            jump bedroomd4
            

        "sleep in":
            
            "I don't want to get up." 
            jump bedd4

label bedroomd4:
    play sound "blanket.mp3" fadein 1.5
    scene d4_bg
    show d4_bedroom_1
    show d4_bedroom_2
    show d4_bedroom_3
    with fade1

    pause 0.75
    "I don't want to be here anymore. There's nothing left. No one left."

    menu:
        "Check my PC":      
            "There won't be any news."
            
            play sound "chair.mp3" fadein 1.5 
            scene d4_bg
            show d4_pc_1
            show d4_pc_3
            with fade1
            
            pause 0.75
            "..."
            play sound "click.mp3" volume 1.5
            show d4_pc_2
            
            pause 0.75
            "You left me so suddenly... and took everything with you."
            "You left me... so lonely."
            "Why am I torturing myself."
            scene d4_bg
            show d4_bedroom_1
            show d4_bedroom_2
            show d4_bedroom_3
            with fade1

            pause 0.75
            "Why are you torturing me."
            jump bathroomd4

        "Go wash up":
                    
            "What's the point? I am fine like this."
            jump bathroomd4



label bathroomd4:
    play sound "door.mp3" fadein 1.5
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

    jump doord4


label doord4:
    play sound "door.mp3" fadein 1.5
    scene d4_bg
    show d4_door_1
    show d4_door_2
    show d4_door_3
    with fade1

    pause 0.75
    "I feel like I'm suffocating.{w=0.5} If everything could just stop..."
    "Please give me a rest."

    jump day5
