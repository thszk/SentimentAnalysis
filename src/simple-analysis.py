#!/usr/bin/env python3

import nltk
from textblob import TextBlob
from newspaper import Article

# Get the article
# url = 'https://everythingcomputerscience.com/'
# article = Article(url)

# # Do some NLP
# article.download() # Downloads the link’s HTML content
# article.parse() # Parse the article
# nltk.download('punkt') # 1 time download of the sentence tokenizer
# article.nlp()

# text = article.summary
# print(text)
line = ""
while True:
  try:
    line = line + "\n" + input()
  except EOFError:
    break

obj = TextBlob(line)
language = obj.detect_language()
if language != "en":
  obj = obj.translate(from_lang= language, to='en')

# returns the sentiment of text
# by returning a value between -1.0 and 1.0
sentiment = obj.sentiment.polarity
# print(sentiment)

if sentiment > 0:
  print('Positivo')
else:
  print('Negativo')

# print("arquivo em python")