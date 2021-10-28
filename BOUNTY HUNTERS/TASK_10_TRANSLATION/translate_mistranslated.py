from deep_translator import GoogleTranslator
import spacy
from spacy_langdetect import LanguageDetector
from spacy.language import Language

nlp = spacy.load("en_core_web_md")


def create_lang_detector(nlp, name):
    return LanguageDetector()


def translate_untranslated(text):
    """ """
    Language.factory("language_detector", func=create_lang_detector)

    nlp.add_pipe('language_detector', last=True)

    doc = nlp(text)

    lang_dic = doc._.language
    lang = lang_dic["language"]

    translated_text = text
    # check the whole text
    if (lang != "en" and lang != 'UNKNOWN'):
        translated_text = GoogleTranslator(source="auto", target='en').translate(text=text)

    # check sentences
    doc = nlp(translated_text)
    new_sentences = []
    for i, sent in enumerate(doc.sents):
        lang_dic = sent._.language
        lang = lang_dic["language"]
        if (lang != "en" and lang != 'UNKNOWN'):
            sent_translated = GoogleTranslator(source=lang, target='en').translate(text=sent)
            new_sentences.append(str(sent_translated))
        else:
            new_sentences.append(str(sent))
    final_translated = " ".join(new_sentences)

    return final_translated


def translate(text: set) -> str:

    return translate_untranslated(text)

    