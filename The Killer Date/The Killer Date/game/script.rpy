# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You")
define m = Character("Max")


# The game starts here.

label start:
    you "I am waiting."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene downtown
    with Dissolve(.5)

    you "Maximillian is coming."
    you "Now is my chance."

    "Someone is coming!!"

    scene black
    "SLAM!!!"

    scene helpful guy
    with Dissolve(.5)

    m "Are you okay?"

    scene downtown blurred

    show max:
        zoom(0.8)

    you "Yes."

    m "My name is Max."

    menu:
        "You are sexy, let's date.":
            jump go_out_with_me

        "I am unnamed grandma.":
            jump lets_date

        "Kill Max.":
            jump kill_1

label lets_date:
    m "Want to date?"

    menu:
        "Yes.":
            you "Yes!"

    scene black

label go_out_with_me:
    m "Ok! Let's have a date."
    
    scene black



scene phone pickup #make a screen with her phone with max saying he'll pick her up
with Dissolve(.5)

scene apartment #needed screen

you "I'm all ready, he should be here any minute"

show  max with fade:
    zoom(.8)


m "Hello sexy lady. Are you ready to go?"

menu:
    "yes diva":
        return

    "not yet":
        jump kill_1

m "lets go baby girl"

return


label kill_1:
    scene Strangulation
    "You kill Max"
    "You Lose :("
    return






