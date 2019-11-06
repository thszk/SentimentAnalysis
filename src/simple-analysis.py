#!/usr/bin/env python3

# libs
import nltk
from textblob import TextBlob
from newspaper import Article

# returns the sentiment of text
def analysis(obj):
  sentiment = obj.sentiment.polarity
  # print(sentiment)
  if sentiment == 0:
    print('Neutro')
  elif sentiment > 0:
    print('Positivo')
  else:
    print('Negativo')

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
    analysis(obj)
  except:
    # if not possible translate
    print('Translation failed!')
else:
  analysis(obj)