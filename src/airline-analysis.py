#!/usr/bin/env python3

# This code was designed to analyze the sentiments of airline discussions on Twitter
# the trained object is read from exported file by airline-training.py code.

# libs
import pickle

# load  NB classifier object in text file
with open('src/resources/nbclassifier', 'rb') as file:
	classifier = pickle.load(file)

# get inline parameter
line = ""
while True:
  try:
    line = line + "\n" + input()
  except EOFError:
    break

# classifying
print(classifier.classify(line))