
############################################################### DAY 5


label day5:
    play music "<loop 0>umbra_draft.mp3" volume 0.15 fadeout 1.5 fadein 1.5
    
    scene d3_bg
    show d4_bed
    with fade1

    play sfx doorbell

    "Someone's at the door."

    menu:
        "Check it out.":
            "I should prolly see who it is."
            jump momsending

        "Ignore":
            "I don't expect any guess."
            "I'm to tired, I will sleep in a little."
            jump missedmsgending

label momsending:
    
    play sound "door.mp3" fadein 1.5

    scene maindoor with fade1
    show mom with dissolve

    mom "Oh my god."
    mom "I keep calling you and you didn't pick up."
    mom "You friends also told me you didn't replied."
    mom "Don't ghost us like this."
    mom "You friends are worried!"
    mom "...I was so worried."
    "..."
    mom "How are you doing, honey."

    scene hug with fade1
    pause 1.0

    scene black with fade1


label missedmsgending:
    scene bedroomd5 with fade1
    "I slept in..."
    "I should charge my phone. It's been a few days since I check it."

    scene phonecharge with fade1
    "I should open the window to let in some fresh air."

    scene bedroomd5_light with fade1
    pause 1.0
    play sound "phone.mp3"

    scene phone with fade1
    pause 1.0
    play sound "hello.mp3"
    pause 1.0

    scene black with fade1

return
