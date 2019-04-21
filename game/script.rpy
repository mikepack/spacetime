define m = Character("Max")

label start:

    "Bang! You awaken in a dark alley, covered in some kind of goo. Your head is throbbing."

    "What is this place? You look around, only to find foreign objects."

    "Off in the distance are faint utterings of words you don't understand."

    menu:

        "What do you do?"

        "Look around.":
            jump start_look_around

        "Get up.":
            jump start_get_up

    label start_look_around:

        "It's a dark, desolate place. Cryptic neon carvings litter the walls."

        jump end

    label start_get_up:

        "You stand. As you come to your feet, you briefly float above the pavement. The gravity seems less than usual."

        jump end

    label end:

        "Continue the story..."

    return
