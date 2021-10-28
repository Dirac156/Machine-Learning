import text2emotion

def get_emotion_from_text(text: str):
    """ get emotion from text and return a list of emotions mentionned in text """

    emotion = text2emotion.get_emotion(text)

    return emotion
