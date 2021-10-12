# base image for our Docker
FROM python:3.9-slim

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m nltk.downloader maxent_ne_chunker
RUN python3 -m nltk.downloader words
RUN python3 -m nltk.downloader treebank
RUN python3 -m nltk.downloader maxent_treebank_pos_tagger
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader averaged_perceptron_tagger
RUN python3 -m spacy download en_core_web_sm

COPY . .

CMD [ "python3", "main.py"]
