""" summarize text module """
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def summarize_text(text: str) -> str:
    """ Summarize text using extractive method """

    text_summary = ''

     #step1: Tokenize and remove stop words
    set_stopwords = set(stopwords.words('english'))
    wtokens = word_tokenize(text)

    #step2:  create a frequency table
    frequency_table = dict()

    for word in wtokens:
        word = word.lower()
        if word in set_stopwords:
            continue
        if word in frequency_table:
            frequency_table[word] += 1
        else:
            frequency_table[word] = 1

    #step3: Assign score to each sentecnce depending on the word it contains
    sentences = sent_tokenize(text)
    sentenceValue = dict()
    sumValues = 0
    for sentence in sentences:
        for word, freq in frequency_table.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq
                sumValues += freq

    #step4: find the most important text
    average = int(sumValues / len(sentenceValue))

    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            text_summary += " " + sentence 
    
    return text_summary
