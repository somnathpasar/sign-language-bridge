phrases = {

    "HELP":
    "Please help me",


    "WATER":
    "I need water",


    "PAIN":
    "I am in pain",


    "A":
    "A",


    "B":
    "B"
}


def get_phrase(sign):

    return phrases.get(
        sign,
        sign
    )