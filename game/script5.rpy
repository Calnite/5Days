define mom = Character("Mom")

############################################################### DAY 5


label day5:
    play music "<loop 0>umbra_draft.mp3" volume 0.15 fadeout 1.5 fadein 1.5
    
    scene d5_bed
    with fade1

    play sound "doorbell.mp3" volume 0.2
    "Someone's at the door... again"

    menu:
        "Check it out.":
            "I should prolly see who it is."
            jump momsending

        "Ignore":
            "I don't expect any guess."
            "I'm to tired, I will sleep in a little."
            jump missedmsgending

label momsending:
    play sound "door.mp3"

    scene d5_outdoor with fade1

    mom "Oh my god."
    mom "I keep calling you and you didn't pick up."
    mom "You friends also told me you didn't replied."
    mom "Don't ghost us like this."
    mom "You friends are worried!"
    mom "...I was so worried."
    "..."
    mom "How are you doing, honey."

    scene black with fade1
    pause 1

    show text "True Ending" with dissolve
    pause 2

    hide text with fade
    pause 1.0

    show text "Thank you for playing!" with dissolve
    pause 2

    hide text with fade
    pause 1.0

    scene main_menu with dissolve1
    return


label missedmsgending:
    scene d5_bedroom_3 
    show d5_bedroom_2
    show  d5_bedroom_1
    with fade1
    "I slept in..."
    "I should charge my phone. It's been a few days since I check it."
    "Let's open the window to let in some fresh air in."

    play sound "phone.mp3"
    "..."
    "Who is calling now."

    scene phone with fade
    pause 1.0
    "...mom"
    play sound "hey.mp3" volume 3
    pause 1.0

    scene black with fade1
    pause 1

    show text "The Phone call Ending" with dissolve
    pause 2

    hide text with fade
    pause 1.0

    show text "Thank you for playing!" with dissolve
    pause 2

    hide text with fade
    pause 1.0

    scene main_menu with dissolve1
    return

return
