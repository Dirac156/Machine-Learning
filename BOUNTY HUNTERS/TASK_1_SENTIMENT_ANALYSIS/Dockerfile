# base image for our Docker
FROM python:3.9-slim

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader wordnet

COPY . .

CMD [ "python3", "main.py"]
