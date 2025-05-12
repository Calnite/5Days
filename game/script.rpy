

#init -3:
    #default current_room = None # This variable controls what list to get buttons from
    #default pnc_flags = {} # This variable controls various creator-defined flags that control the state of a given point'n'click segment
## these are set in point_and_click.rpy and should not be repeated

screen pnc_screen(room="left"):

    style_prefix "pnc"

    for i in eval(f"{room}_buttons"):
        if (i[3] is None) or (eval(i[3])):
            imagebutton auto "point_and_click/image/" + str(i[0]) + "_%s.png" pos i[1] action Return(i[2])

style pnc_image_button:
    anchor (0.5, 0.5)

define diss = {"screens" : Dissolve(0.15)} # this allows the textbox to be hidden and shown without any pause


define fade1 = Fade(1.5, 1.0, 1.5)
define dissolve1 = Dissolve(2)

default optionD = False
default optionTwo = False

define gui.dialogue_text_outlines = [ (2, "#000005", 0, 0) ]
define gui.dialogue_outline_scaling = "linear"
define gui.charaters_text_outlines = [ (2, "#000005", 0, 0) ]
define gui.characters_outline_scaling = "linear"

default dreamending = False
default sleeping = False

default actions_taken = []
## added to prevent errors on ifs in menus, such as "if not pcchecked" which
## crashes the game since pcchecked isn't defined ahead of time.

default l = ChatCharacter("lover", icon="images/lover.png")
default f = ChatCharacter("friend", icon="images/friend.png")
default m = ChatCharacter("mom", icon="images/mom.png")
default y = ChatCharacter("you", icon="images/you.png")

############################################################### DAY 1


label start:
    play music "<loop 0>umbra.mp3" volume 0.25 fadeout 1.5 fadein 1.5

    scene d1_bg
    show d1_bed
    with fade1
    pause 1

    menu:
        "wake up":

            "I better get up now."
            jump bedroomd1

        "sleep in":
            if dreamending:
                jump dreamending
            elif sleeping:
                jump sleepin2
            else:
                jump sleepin1


label sleepin1:
    "Just five more minutes..."
    $ sleeping = True
    jump start

label sleepin2:
    "... I want... more time."
    $ dreamending = True
    jump start

label dreamending:
    scene white with fade1
    show her with dissolve1
    pause 1

    "Good morning, sleepy head."

    show white with dissolve1
    pause 0.5

    scene white with dissolve1
    show dreamend1 with dissolve1
    pause 1

    scene white with dissolve1
    "Good morning."

    pause 0.5

    show d5_outdoor with dissolve1
    return


label bedroomd1:
    play sound "blanket.mp3" fadein 1.5
    scene d1_bg
    show d1_bedroom_1
    show d1_bedroom_2
    show d1_bedroom_3
    with fade1

    pause 0.75
    "I slept terriblely."
    "Must have been the nightmares."
    jump menu


label menu:
    menu:
        "What should I do now?"

        "Check my PC" if not "d1_pcchecked" in actions_taken:
            $ actions_taken.append("d1_pcchecked")
            jump pcd1

        "Eat something" if not "d1_ate" in actions_taken:
            $ actions_taken.append("d1_ate")
            jump kitchend1

        "Go wash up" if not "d1_bathvisited" in actions_taken:
            $ actions_taken.append("d1_bathvisited")
            "I might need it."
            jump bathroomd1

label pcd1:
    play sound "<silence 1.0>"
    queue sound "chair.mp3" fadein 1.5
    scene d1_pc_1
    with fade1

    pause 0.75
    "Hm, I should check my messages."

    call screen desktop(1)
    jump expression _return

label d1_game:
    #show infinite_load
    "...It's not loading."
    call screen desktop(1)
    jump expression _return

label d1_shutdown:
    "...Nevermind."
    jump doord1

label d1_messages:
    play sound "click.mp3" volume 1.5
    $ reset_chats() ## this gets everything set up correctly, but since you don't want any new messages to show up, only call it on day 1.
    window hide
    show screen chat_messages_view(1)
    y "hey can we talk?" (c="lover")
    f "what's up?" (c="friend")
    y "nothing" (c="friend")
    f "cool"
    m "Love and kisses!" (c="mom")
    m "Are you coming home for the holdidays?"
    m "Call me."
    pause 10 ## 10 seconds to explore
    "Still no reply."
    "I just need to wait. Any moment...{w=0.5} you'll reply or call me"
    "like you always did."
    "I should check again tomorrow. I can wait."
    hide screen chat_messages_view
    scene d1_bg
    show d1_bedroom_1
    show d1_bedroom_2
    show d1_bedroom_3
    with fade1




label bathroomd1:
    play sound "door.mp3" fadein 1.5
    scene d1_bg
    show d1_bathroom_1
    show d1_bathroom_2
    show d1_bathroom_3
    with fade1

    pause 0.75
    "My bathroom barely has any light."

    menu:
        "Look closer":
            "...it's just me."
            scene d1_bg
            show d1_mirror_1
            show d1_mirror_2
            with fade1

            pause 0.75
            "Oh...  {w=0.5} is it really me?"
            "I don't know."
            jump bathroomd1

        "Wash up":
            "Washed my face and brushed my teeth."
            "All done."

            jump doord1


label doord1:
    play sound "door.mp3" fadein 1.5
    scene d1_bg
    show d1_door_1
    show d1_door_2
    show d1_door_3
    with fade1

    pause 0.75
    "I don't need to go out today."
    "I can play some games."
    "Maybe I will get a text tonight... or a knock on the door..."
    "and I'll hear your voice."

    jump bedd2
