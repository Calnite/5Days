
############################################################### DAY 3


label bedd3:
    play music "<loop 0>bedbug.wav" volume 0.2 fadeout 1.5 fadein 1.5

    scene d3_bg
    show d3_bed
    with fade1

    menu:
        "wake up":
            
            "I shouldn't be so lazy."
            jump bedroomd3
            

        "sleep in":
            
            "Just five more minutes..." 
            jump bedd3

label bedroomd3:
    play sound "blanket.mp3" fadein 1.5
    scene d3_bg
    show d3_bedroom_1
    show d3_bedroom_2
    show d3_bedroom_3
    with fade1

    pause 0.75
    "My hand...  {w=0.5} I'm an idiot."

    menu:
        "Check my PC":      
            "If I could just go back... if I could just fix everything..."
            "I'd do anything."

            play sound "chair.mp3" fadein 1.5 
            scene d3_bg
            show d3_pc_1
            show d3_pc_3
            with fade1
            
            pause 0.75
            "Let's check my messages."
            play sound "click.mp3" volume 1.5
            show d3_pc_2
            
            pause 0.75
            "The last time we chatted...{w=0.5} I should have written a better message."
            "I sound like an asshole. I should have been nicer to you."
            "... You didn't deserved it."
            scene d3_bg
            show d3_bedroom_1
            show d3_bedroom_2
            show d3_bedroom_3
            with fade1

            pause 0.75
            "If I had just said the right thing, would it have changed anything?"
            jump bathroomd3


        "Go wash up":
                    
            "Ugh, my head is not in the right space."
            jump bathroomd3



label bathroomd3:
    play sound "door.mp3" fadein 1.5
    scene d3_bg
    show d3_bathroom_1
    show d3_bathroom_2
    show d3_bathroom_3
    with fade1

    pause 0.75
    "It's still there."

    menu:
        "Look closer":
            "Why did I do that... I will get a scar from this."
            scene d3_bg
            show d3_mirror_1
            show d3_mirror_2
            show d3_mirror_3
            with fade1

            "If I had just said something different that day. If I had noticed something..."
            "Anything, that could have saved you."
            "No..."
            "I have noticed..."
            "I should have done something."
            "Maybe I could have saved myself too."
            jump doord3


        "Wash up":
            "...ok?"

            jump doord3


label doord3:
    play sound "door.mp3" fadein 1.5
    scene d3_bg
    show d3_door_1
    show d3_door_2
    show d3_door_3
    with fade1

    pause 0.75
    "Just one more time."
    "If I could see your face and hear your voice {w=0.5} just one more time."
    "..."
    "I loved you so much."

    jump bedd4
   
    
