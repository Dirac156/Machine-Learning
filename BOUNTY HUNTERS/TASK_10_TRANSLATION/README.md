# Project Title: Traanslate Untranslated/Mistranslated words

## Project Description

This project comporte modules and function to find to correct translation errors.

The project has two version:

1. Version-1:

* spacy, deep_translator and autocorrect: Detect language using spacy library. Turn non-english sentence to english using Google translator then use autocorrect to check for final errors.

2. Version-2:

* nltk, langdetect and deepl: Detect language using langdetect and translate the whole sentence to english if this was not the case. Deepl automaticaly fix errors after translation.

## Run Project

### Requirements

* spacy-nightly
* spacy
* spacy-langdetect
* deep_translator
* nltk
* langdetect

### Download container

* docker pull diracmmd/task_10

* docker run -it diracmmd/task_10

### Expected Output

* Success: 'correct text'

* Error: <Error Message>

### Author

* Dirac Murairi