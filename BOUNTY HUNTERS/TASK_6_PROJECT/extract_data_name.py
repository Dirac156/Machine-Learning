# import spacy
import spacy
 
# load spacy model
nlp = spacy.load('en_core_web_sm')
 

def extract_data(text: str):
    doc = nlp(text)

    people = [(el, el.label_) for el in doc.ents if el.label_ == 'PERSON']

    projectName = None

    return people
