# base image for our Docker
FROM python:3.9-slim

WORKDIR /

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
RUN pip3 install spacy==3.1.4
RUN pip3 install spacy-nightly==3.0.0rc5
RUN pip3 install spacy-langdetect==0.1.2
RUN python3 -m spacy download en_core_web_sm
RUN pip3 install deep_translator==1.5.4
RUN pip3 install autocorrect==2.5.0
RUN pip3 install langdetect==1.0.7
RUN pip3 install click==7.0
RUN pip3 install Exit

COPY . .

CMD [ "python3", "main.py"]
