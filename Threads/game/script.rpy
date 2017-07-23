# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



define l = Character('Locke', image = 'Locke' )
define d = Character('Dale', image = 'Dale' )

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "Maybe I can use this to show the thoughts of the character."
    show Locke normal with moveinleft
    
    l "I'm testing writing my first game. I did a powerpoint!! Look at me!"

    l blush "This is okay." with dissolve
    
    show Dale happy at right with dissolve
    
    l "There really isn't much to it."
    
    menu:
        "Choice 1":
            show Locke happy at left with dissolve
            l "Okay"
        "Second Choice":
            "test"

    jump test

    # This ends the game.

    return
