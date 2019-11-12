#!/usr/bin/env python3

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