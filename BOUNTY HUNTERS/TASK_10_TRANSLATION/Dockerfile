# base image for our Docker
FROM python:3.9-slim

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download en_core_web_lg

COPY . .

CMD [ "python3", "main.py"]
