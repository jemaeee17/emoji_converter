def emoji_converter(enter):
    words = enter.split(" ")
    emoji = {
        ":(": "🥹",
        ":)": "😀"
    }
    emotion = ""
    for word in words:
        emotion += emoji.get(word, word) + " "
    return emotion


enter = input("> ")
print(emoji_converter(enter))




