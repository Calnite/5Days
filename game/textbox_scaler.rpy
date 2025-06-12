###############################################################################################################
### TEXTBOX SCALER ############################################################################################
###############################################################################################################
#
# Thanks for downloading my Textbox Scaler plugin for Ren'Py! ( https://kigyo.itch.io/textbox-scaler-for-renpy )
#
# Below, I'll walk you through what you need to do to set this functionality up in your own project!
# If you run into any difficulties, I'm always happy to help in the Itch.io comments!
#
# If you like this tool, consider dropping a donation: https://ko-fi.com/kigyodev
# Credit to "KigyoDev" would also be appreciated!
#
# Thank you, and may this tool make your game more accessible & easier to read on various monitors! :D
# - KigyoDev
#
###############################################################################################################


###############################################################################################################
## 1. Variables ###############################################################################################
###############################################################################################################
## 
## First, we have to change two gui variables into preferences so we can adjust them during the game.
## We will also want to save the default values separately so we can reference those later.
## 
## NOTE: To prevent conflicts, comment out [gui.text_size] and [gui.dialogue_width] in [gui.rpy]!

# The wiggle room variable, my favorite. It makes sure your rooms wiggle.
# (Okay, but seriously, I'll explain this one in more detail later.)
define the_wiggle_room = 15

# This is just a sample default value. The number should match what was previously [gui.text_size]
define default_text_size = 33
define gui.text_size = gui.preference("size", default_text_size)

# This is just a sample default value. 
# The number should match what was previously [gui.dialogue_width], MINUS the value of [the_wiggle_room]
# E.g. if your previous width was 1150, enter 1135
define default_textbox_width = 1101
define gui.dialogue_width = gui.preference("dialogue_width", default_textbox_width + the_wiggle_room)

# If this works with how your UI is set up, you can adjust NVL text width the same way.
# Otherwise, uncomment the lines below or set up your own additional preference variables!
# NOTE: If there is enough demand, I will add this as part of the tutorial. Let me know on Itch.io!
define gui.nvl_text_width = gui.preference("dialogue_width", default_textbox_width + the_wiggle_room)
define gui.nvl_thought_width = gui.preference("dialogue_width", default_textbox_width + the_wiggle_room)

# Here, you can adjust the range of available text sizes
# Make sure the minimum is still readable, and that the maximum size doesn't overflow!
define text_size_minimum = default_text_size-5
define text_size_maximum = default_text_size+7

# A persistent variable that will make this whole thing a lot smoother. I recommend not touching this!
default persistent.text_size = gui.text_size


###############################################################################################################
## 2. Preferences #############################################################################################
###############################################################################################################
##
## We'll be adding a text size slider that lets players adjust the size of dialogue text!
##   Make sure [gui.text_size] is only used for your dialogue, since scaling UI and other text will likely have unintended consequences.
##   A quick tip would be to search for [gui.text_size] and replace it with [default_text_size] where needed.
##   In particular, keep an eye on [gui.choice_button_text_size] which is set to [gui.text_size] by default!
##
## Uncomment the code below and place it in your preferences screen:

#vbox:
#    style_prefix "slider"
#    bar value FieldValue(persistent, "text_size", min=text_size_minimum, max=text_size_maximum, step=1.0, style=u'slider')


###############################################################################################################
## Optional: Mock Textbox #####################################################################################
###############################################################################################################
## 
###############################################################################################################
## IMPORTANT NOTE:                                                                                           ##
##   Changing a gui preference requires [gui.rebuild] to be run, which causes the game to freeze briefly.    ##
##   This is unavoidable, but this plugin makes sure it's only run once:                                     ##
##   When closing the game menu, and only IF the text size has changed.                                      ##
###############################################################################################################
##
## Due to the rebuild problem, I heavily recommend providing a mock textbox that lets players preview the text
## before finalizing their decision.
##
## Here's a great tutorial by Papaya: 
## https://papeetamakaan.wordpress.com/2022/05/23/renpy-tricks-textbox-options-text-speed-preview-mock-textbox/


###############################################################################################################
## 3.a Rebuilding the GUI #####################################################################################
###############################################################################################################
##
## The last step is to insert the following (uncommented) code at the top of your preferences screen, directly under [tag menu]!

#if persistent.text_size != gui.preference("size"):
#    $ text_scale_function = int((default_textbox_width/default_text_size)*persistent.text_size + the_wiggle_room/(persistent.text_size/default_text_size))
#
#    on "replaced" action [Hide("mock_text"), gui.SetPreference("dialogue_width", text_scale_function, rebuild=False), gui.SetPreference("size", int(persistent.text_size))]
#    on "hide" action [Hide("mock_text"), gui.SetPreference("dialogue_width", text_scale_function, rebuild=False), gui.SetPreference("size", int(persistent.text_size))]
#    key ["game_menu", "pad_b_press"] action [Hide("mock_text"), gui.SetPreference("dialogue_width", text_scale_function, rebuild=False), gui.SetPreference("size", int(persistent.text_size)), Return()]
#
#else:
#    on "replaced" action Hide("mock_text")
#    key ["game_menu", "pad_b_press"] action [Hide("mock_text"), Return()]


###############################################################################################################
## 3.b Rebuilding the GUI #####################################################################################
###############################################################################################################
##
## If you're not using a mock textbox, you can also use this shorter block instead:

#if persistent.text_size != gui.preference("size"):
#    $ text_scale_function = int((default_textbox_width/default_text_size)*persistent.text_size + the_wiggle_room/(persistent.text_size/default_text_size))
#
#    on "replaced" action [gui.SetPreference("dialogue_width", text_scale_function, rebuild=False), gui.SetPreference("size", int(persistent.text_size))]
#    on "hide" action [gui.SetPreference("dialogue_width", text_scale_function, rebuild=False), gui.SetPreference("size", int(persistent.text_size))]
#    key ["game_menu", "pad_b_press"] action [gui.SetPreference("dialogue_width", text_scale_function, rebuild=False), gui.SetPreference("size", int(persistent.text_size)), Return()]


###############################################################################################################
## Optional: Fine-tuning ######################################################################################
###############################################################################################################
##
## The previous step introduced the [text_scale_function], which keeps your dialogue width proportional to the text size.
## This will work in the majority of cases, but individual words might still be cut off differently. 
## 
## In case you want to adjust it, here's what each part of the [text_scale_function] does:
## 
##   (default_textbox_width/default_text_size)
##          --> This is the ratio of your default text size and default textbox width
##
##   (default_textbox_width / default_text_size) * persistent.text_size
##          -->  Now, we multiply the ratio with the newly selected text size
##
##   + the_wiggle_room / (persistent.text_size / default_text_size)
##          -->  Some fonts will scale differently. This wiggle room portion adds a variable width (more width if text is smaller than the default & less if it's bigger).
##               I recommend testing a few different lines of dialogue with both the minimum and maximum text size settings and adjusting [the_wiggle_room] as needed.
##               It's purely trial-and-error. Depending on how your font behaves, you can also change the [+] to a [-]!


###############################################################################################################
## License ####################################################################################################
###############################################################################################################

# Copyright 2025 KigyoDev

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions 
# of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO 
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

###############################################################################################################











