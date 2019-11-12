#!/usr/bin/env python3

# libs
import csv
import nltk
import pickle
from textblob.classifiers import NaiveBayesClassifier

# vars
dataset = []
training = []

# settungs
nltk.download('punkt')

# read csv file
with open('src/resources/Airline-Sentiment-2-w-AA.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	# append rows in dataset array
	for row in reader:
		dataset.append((row[14],row[5]))

# close csv  file
csvFile.close()

# create training array
for i in range(1500):
	training.append(dataset[i])

# training
classifier = NaiveBayesClassifier(training)

# save NB classifier object in text file
with open('src/resources/nbclassifier', 'wb') as file:
  pickle.dump(classifier, file)

# print("Acuracia:", classifier.accuracy(training))