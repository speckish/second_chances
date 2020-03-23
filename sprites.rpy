layeredimage quinn:
    yoffset 75
    attribute body default

    group face:
        attribute neutral default
        attribute happy
        attribute sad
        attribute shocked
        attribute angry

    attribute sweat
    attribute blush

layeredimage yuki:
    align (0.0, 1.0)
    ypos 1005
    yoffset 75
    xoffset 150
    # yoffset 80
    group face:
        attribute neutral default
        attribute angry
        attribute happy
        attribute shocked
        attribute sad

    attribute sweat
    attribute blush

layeredimage zethe:
    yoffset 75
    attribute body default

    group face:
        attribute neutral default
        attribute happy
        attribute sad
        attribute shocked
        attribute angry

    attribute sweat
    attribute blush


transform startle():
    linear 0.15 yoffset -50
    linear 0.25 yoffset 0

transform one_two():
    xalign 0.25

transform two_two():
    xalign 0.75

transform seated():
    ypos 1200

transform yell():
    linear 0.25 yoffset 25
    easein_bounce 0.5 yoffset 75


image black = "#000000"
image white = "#ffffff"
