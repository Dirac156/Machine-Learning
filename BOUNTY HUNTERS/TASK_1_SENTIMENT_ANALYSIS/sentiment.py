from textblob import TextBlob

def sentiment(text: str):
    """ perform sentiment analysis """

    testimonial = TextBlob(text)

    sentiment = testimonial.sentiment

    return sentiment.polarity, sentiment.subjectivity
