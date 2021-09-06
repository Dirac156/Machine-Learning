import spacy
from typing import List
from nltk.tokenize import sent_tokenize

nlp = spacy.load("en_core_web_md")

def find_subject(text: str) -> List[str]:
    """ Find subject of a text """

    # load the text to the modal
    doc=nlp(text)

    # Find the subject
    sub_toks = [tok for tok in doc if (tok.dep_ == "nsubj") ]

    #return the subject
    return sub_toks 


def identify_subject(text: str) -> str:
    """ Identify the subject of a sentence """

    sentences = sent_tokenize(text)
    subject_identified = dict()
    
    # step 1: identify part of speech of each sentence
    # step 2: create a dictionary and add each subject of the sentence as value
    # of the dict key (sentence)

    for sentence in sentences:
        subjects = find_subject(sentence)
        if (subjects is None) or len(subjects) == 0:
            subject_identified[sentence] = ''
        else:
            subject_identified[sentence] = subjects

    # Return the dictionnary
    return subject_identified
