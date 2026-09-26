def clean_word(word):
    return "".join(character for character in word.lower() if character.isalpha())
