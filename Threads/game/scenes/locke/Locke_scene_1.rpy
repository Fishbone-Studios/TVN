init:
    image black = "#000000"

label test:
    scene black
    
    "You had arrived at the college party an hour ago."
    
    "Many other students mill about, some drinking, some eating, most talking."
    
    "You've been here for a couple of hours, you think, and suddenly find yourself alone with a cup in your hand."
    
    show party
    python:
        renpy.play("music/party_noise.wav",channel=7)

    "Hm how many drinks was that now? Was I starting to lose count...?"
    
    "The room was also beginning to spin. Well, maybe not spin, but tilt slightly."

label drink:
    "Okay what should I do now..."
    
    menu:
        "Get another drink":
            "Another drink seems like a good idea!"
            play sound "music/open_beer.wav"
            $ renpy.pause(3.0)
            "Yup, still tastes like beer."
            jump drink
            
        "I think I'd better find a bathroom...":
            "I think now would be a good time to find a bathroom."

    hide party
    show hallway
    
    play sound "music/door_close.wav"
    python:
        renpy.music.stop(channel=7,fadeout=0.1)
        renpy.music.play("music/party_noise_muffled.wav",channel=6,fadein=0.1)
    
    "As I closed the door the music faded and I found myself in a dimly lit hallway."

    "Doors lined each side of the hall until it disappeared around a corner in the back."
    
    "Unfortunately there were no signs signifying what was behind each door."

    "Now which one could be the bathroom...??"

    "Eenie meenie miney... mo!"

    "Picking a door at random I opened it and stepped inside."
    
    python:
        renpy.sound.play("music/steps.wav",channel=3)
    hide hallway with dissolve
    play sound "music/door_close.wav"
    $ renpy.pause(1.0)
    show piano_room
    python:
        renpy.music.stop(channel=6,fadeout=3)
        renpy.music.play("music/locke_solo.mp3",channel=5,fadein=8)
    
    "The sounds of the party faded even more as I stepped into the dimly lit room."
    
    "My feet landed on carpet. Oops! Probably not the bathroom then."
    
    "This room looked a lot nicer than the hallway I had just come from. The walls were adorned by various pictures and paintings."
    
    "Some were obviously photos of the fraternity brothers over various years, but the paintings held the visages of clearly important people."
    
    "As my eyes scanned along the wall I finally noticed a piano in the corner. A figure sat at the bench, their fingers moving along the keys."
    
    "It wasn't until then I noticed the piano music quietly filling the room."
    
    "A lilting melody that was both sad and sweet. It nagged at my mind like I had heard it somewhere before."
    
    "But where...?"
    
    $ renpy.music.stop(channel=5)
    
    show Locke normal with moveinleft
    
    l "Oh! Sorry, I didn't see you there."
                         
return