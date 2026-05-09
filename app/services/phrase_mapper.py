phrases = {

    "HELP":
    "Please help me",


    "WATER":
    "I need water",


    "PAIN":
    "I am in pain",


    "STAND":
    "I need to stand",


    "SIT":
    "I need to sit",

    "COOL":
    "I am alright",
}


def get_phrase(sign):

    return phrases.get(
        sign,
        sign
    )