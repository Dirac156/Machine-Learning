from deep_translator import DeepL
from langdetect import detect
from nltk import sent_tokenize

def detect_language(text):
    """ """
    lang = detect(text)
    return lang


def translate_untranslated_p(text):
    """ """
    lang = detect_language(text)
    # check the whole text
    if (lang != "en" and lang != 'UNKNOWN'):
        translated_text = DeepL("your_api_key").translate(text)

    # check sentences

    new_sentences_list = sent_tokenize(text)
    new_sentences = []

    for sent in new_sentences_list:
        lang = detect_language(sent)
        if (lang != "en" and lang != 'UNKNOWN'):
            translated_text = DeepL("your_api_key").translate(sent)
            new_sentences.append(str(translated_text))
        else:
            new_sentences.append(str(sent))

    final_translated = " ".join(new_sentences)

    return final_translated

def translate_p(text: set) -> str:

    return translate_untranslated_p(text)
