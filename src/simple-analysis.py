#!/usr/bin/env python3

# libs
import nltk
from textblob import TextBlob

# returns the sentiment of text
def analyze(obj):
  sentiment = obj.sentiment.polarity
  # print(sentiment)
  if sentiment == 0:
    print('Neutral')
  elif sentiment > 0:
    print('Positive')
  else:
    print('Negative')

# read inline parameter
line = ""
while True:
  try:
    line = line + "\n" + input()
  except EOFError:
    break

obj = TextBlob(line)

# detect input language
language = obj.detect_language()

# translate if necessary
if language != "en":
  try:
    obj = obj.translate(from_lang= language, to='en')
    analyze(obj)
  except:
    # if not possible translate
    print('Translation failed!')
else:
  analyze(obj)