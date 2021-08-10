#! /usr/bin/env python
# part of speech tagging 


import nltk
from nltk.tag import pos_tag
from module.tokenize import tokenize_text
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')

def rewrite_part_speeche(word_tuple: tuple) -> tuple:
    """
    rewrite_part_speeche
    -------------------
    NNP: Noun, proper, singular
    NN: Noun, common, singular or mass
    IN: Preposition or conjunction, subordinating
    VBG: Verb, gerund or present participle
    VBN: Verb, past participle
    ...
    """

    assert len(word_tuple) > 1

    if word_tuple[1] == 'NNP':
        return word_tuple[0], 'Noun, proper, singular'
    elif word_tuple[1] == 'NN':
        return word_tuple[0], 'Noun, common, singular or mass'
    elif word_tuple[1] == 'PDT':
        return word_tuple[0], 'Pre-determiner'
    elif word_tuple[1] == 'NNS':
        return word_tuple[0], 'Noun, common, plural'
    elif word_tuple[1] == 'IN':
        return word_tuple[0], 'Preposition or conjunction, subordinating'
    elif word_tuple[1] == 'PRP$' : 
        return word_tuple[0], 'Pronoun, possessive'
    elif word_tuple[1] == 'VBG':
        return word_tuple[0], 'Verb, gerund or present participle'
    elif word_tuple[1] == 'VBN':
        return word_tuple[0], 'Verb, past participle'
    elif word_tuple[1] == 'VBP':
        return word_tuple[0], 'Verb, past tense'
    elif word_tuple[1] == 'ADJ':
        return word_tuple[0], 'Adjective'
    elif word_tuple[1] == 'JJ':
        return word_tuple[0], 'Adjective or numeral, ordinal'
    elif word_tuple[1] == 'JJR':
        return word_tuple[0], 'Adjective, comparative'
    elif word_tuple[1] == 'JJS':
        return word_tuple[0], 'Adjective, superlative'
    elif word_tuple[1] == 'LS':
        return word_tuple[0], 'List item marker'
    elif word_tuple[1] == 'MD':
        return word_tuple[0], 'Modal auxiliary'
    elif word_tuple[1] == 'ADV' or word_tuple[1] == 'RB':
        return word_tuple[0], 'Adverb'
    elif word_tuple[1] == 'CONJ':
        return word_tuple[0], 'Conjunction'
    elif word_tuple[1] == 'CC':
        return word_tuple[0], 'Conjunction, coordinating'
    elif word_tuple[1] == 'PRON':
        return word_tuple[0], 'Pronoun'
    elif word_tuple[1] == 'PRT':
        return word_tuple[0], 'Particle'
    elif word_tuple[1] == 'DT' or word_tuple[0] == 'DET':
        return word_tuple[0], 'Determiner'
    elif word_tuple[1] == 'CD':
        return word_tuple[0], 'Numeral, cardinal'
    elif word_tuple[1] == 'EX':
        return word_tuple[0], 'Existential there'
    elif word_tuple[1] == 'POS':
        return word_tuple[0], 'Genitive marker'
    elif word_tuple[1] == 'PRP':
        return word_tuple[0], 'Pronoun, personal'
    elif word_tuple[1] == 'RBR':
        return word_tuple[0], 'Adverb, comparative'
    elif word_tuple[1] == 'RBS':
        return word_tuple[0], 'Adverb, superlative'
    elif word_tuple[1] == 'RP':
        return word_tuple[0], 'Particle'
    elif word_tuple[1] == 'TO':
        return word_tuple[0], '"to" as preposition or infinitive marker'
    elif word_tuple[1] == 'UH':
        return word_tuple[0], 'Interjection'
    elif word_tuple[1] == 'VERB' or word_tuple[1] == 'VB':
        return word_tuple[0], 'Verb, base form'
    elif word_tuple[1] == 'VBD':
        return word_tuple[0], 'Verb, past tense'
    elif word_tuple[1] == 'VBG':
        return word_tuple[0], 'Verb, present participle or gerund'
    elif word_tuple[1] == 'VBN':
        return word_tuple[0], 'Verb, present participle or gerund'
    elif word_tuple[1] == 'VBP':
        return word_tuple[0], 'Verb, present tense, not 3rd person singular'
    elif word_tuple[1] == 'VBZ':
        return word_tuple[0], 'Verb, present tense, 3rd person singular'
    elif word_tuple[1] == 'WDT':
        return word_tuple[0], 'WH-determiner'
    elif word_tuple[1] == 'WP':
        return word_tuple[0], 'WH-pronoun'
    elif word_tuple[1] == 'WRB':
        return word_tuple[0], 'WH-adverb'
    else:
        return word_tuple


def part_of_speech(text: str = None):
    """
    part_of_speech
    --------------
    """
    tokens = tokenize_text(text)

    list_part_speech = pos_tag(tokens)

    return [rewrite_part_speeche(word) for word in list_part_speech]
