define mom = Character("Mom", what_color="#ff8976", ctc="ctc_animation", ctc_position="fixed")

############################################################### DAY 5


label day5:
    play music "<loop 0>umbra_draft.mp3" volume 0.2 fadeout 1.5 fadein 1.5

    scene d5_bed with fade1

    play sound "doorbell.mp3" volume 0.2
    "Someone's at the door... again"

    menu:
        "Check it out.":
            "I should probably see who it is."
            scene d5_bedroom with fade1
            pause 0.5
            jump momsending

        "Ignore":
            "I don't expect any guests."
            "I'm too tired, I will sleep in a little more."
            jump missedmsgending

label dreamending:
    scene black with fade1
    pause 1.0

    scene whitebg with fade1
    show her with dissolve1
    pause 1.0

    scene whitebg with dissolve1
    pause 0.5
    nvl clear

    end "Good morning, sleepy head. {w=1.5} {nw}"

    nvl clear

    scene whitebg with dissolve1
    show dreamend1 with dissolve1
    pause 1.0

    scene whitebg with dissolve1
    end "Good morning.{w=1.5} {nw}"

    nvl clear
    scene black with fade1
    pause 1

    show text "{size=+10}The Dream Ending{/size}\nWhere longing becomes reality" with dissolve
    pause 3

    jump thankyou


label momsending:
    scene d5_door with fade1
    pause 0.5
    play sound "door.mp3"
    scene mom with fade1

    mom "Oh my god."
    mom "Days without answering your phone! Do you know how many worst-case scenarios I imagined?"
    mom "Your friends told me that you didn't respond to their text either."
    pause 1.0
    mom "We thought... we thought we might lose you too."
    "I..."
    mom "..."
    pause 1.0
    mom "...How are you doing, honey?"

    scene whitebg with dissolve1
    nvl clear
    end "All of the words I can't say stick in my throat.{w=1}{nw}"
    end "My heavy body felt much lighter as I collapsed into her arms.{w=2}{nw}"

    show text "{size=+10}Mom's little sunshine Ending{/size}\nThe first fragile steps forward" with dissolve
    pause 3

    jump thankyou

label missedmsgending:
    scene  d5_bedroom with fade1
    "I slept in..."
    "Old habits die hard. But the thought of sleeping forever... isn't as strong as it once was."
    "My phone lies dead in a tangle of sheets. How long has it been?"
    scene phone with fade
    pause 1.0
    "I can't recall the last time I charged my phone."

    scene charging with fade
    "As the battery charges, the mess around me feels more manageable. \nJust dust, just laundry, just... living."

    scene d5_bedroom with fade
    "The list forms in my mind without prompting."
    "I should reply to my mom and friends."
    "My room is a mess, I should clean it up." 
    "And I need to buy groceries."
    "I should take a bath before I go out."
    "So much to do..."

    play sound "phone.mp3"
    "..."

    scene fcall with fade
    pause 1.0
    "...Hello"
    f "Dude! Your mom and I have been trying to reach you for a few days now!"
    f "You can't just disappear like that. Not after... not now."
    "I'm sor-{w=1}{nw}" 
    "No... I'm...still here."
    f "Damn right you better be. And you're coming over for dinner. No arguments."

    scene black with fade1
    pause 1

    show text "{size=+10}The Reconnection Ending{/size}\nThe world hasn't forgotten you" with dissolve
    pause 3

    jump thankyou

label thankyou:
    scene black with fade1
    nvl clear
    pause 1

    end "Thank you for walking this path. \nEach playthrough reveals new fragments of the story.{w=2} {nw}"
    end "Secret under the keyboard{w=3} {nw}"
    
    scene black with fade1
    nvl clear
    scene main_menu with dissolve1
    stop music fadeout 2
    return
