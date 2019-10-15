#!/usr/bin/env python3

import nltk
from textblob import TextBlob
from newspaper import Article

# Get the article
url = 'https://everythingcomputerscience.com/'
article = Article(url)

# Do some NLP
article.download() # Downloads the link’s HTML content
article.parse() # Parse the article
nltk.download('punkt') # 1 time download of the sentence tokenizer
article.nlp()

text = article.summary
print(text)

obj = TextBlob('Joao is a fucking asshole')
# returns the sentiment of text
# by returning a value between -1.0 and 1.0
sentiment = obj.sentiment.polarity
# print(sentiment)

if sentiment == 0:
  print('The text is neutral')
elif sentiment > 0:
  print('The text is positive')
else:
  print('The text is negative')

# print("arquivo em python")