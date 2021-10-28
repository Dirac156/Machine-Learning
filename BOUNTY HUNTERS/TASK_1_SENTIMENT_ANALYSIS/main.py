from module.read_file import read_text_file
from sentiment import sentiment
from emotion import get_emotion_from_text

text = read_text_file("./text.txt")
result_sentiment = sentiment(text)

result_emotion = get_emotion_from_text(text)

print("Emotions")
print(result_emotion)

print("polarity: ")
print("{:02f}".format(result_sentiment[0]))

print("subjectivity: ")
print("{:02f}".format(result_sentiment[1]))
