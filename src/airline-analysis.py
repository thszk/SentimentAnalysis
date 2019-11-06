#!/usr/bin/env python3

# libs
import csv
import nltk
from textblob.classifiers import NaiveBayesClassifier

# vars
dataset = []
train = []

# settungs
nltk.download('punkt')

# get inline parameter
line = ""
while True:
  try:
    line = line + "\n" + input()
  except EOFError:
    break

# read csv file
with open('src/resources/Airline-Sentiment-2-w-AA.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	# append rows in dataset array
	for row in reader:
		dataset.append((row[14],row[5]))

# close csv  file
csvFile.close()

# create training array
for i in range(500):
	train.append(dataset[i])

# training
# print("Treinando...")
classifier = NaiveBayesClassifier(train)

# print("Acuracia:", classifier.accuracy(train))

# classifying
print(classifier.classify(line))
