emoji = {
    ":(" : "🥹",
    ":)" : "😀"
}


while True:
    enter = input("> ")
    icon = enter.split(" ")
    emotion = ""

    for word in icon:
        emotion += emoji.get(word, word) + " "

    print(emotion.strip())
    break
