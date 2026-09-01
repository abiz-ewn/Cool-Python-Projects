words = ["Apple", "Banana", "Fly", "Rhythm", "Orange", "Kiwi", "Grapes"]

for word in words:
    for letter in word:
        if letter.lower() in "aeiou":
            print(f"{word} has a vowel letter")
            break
    else:
        print(f"{word} has no vowel letters")