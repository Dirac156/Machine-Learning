#!/usr/bin/env python


from nltk.tokenize import word_tokenize
from typing import List


def tokenize_text(text: str = None) -> List[str]:
    """
    tokenize_text
    -------------
    """
    if text is None:
        raise ValueError('the text input cannot be Null')
        
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()]
        
    return tokens
