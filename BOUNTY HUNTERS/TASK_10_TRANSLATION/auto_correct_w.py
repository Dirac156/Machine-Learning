from autocorrect import Speller


def correct_word(my_words: str) -> str:
    spell = Speller()
    new_text = spell(my_words)

    return new_text
