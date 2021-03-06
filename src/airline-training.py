#!/usr/bin/env python3

# This code was designed to train the Naive Bayes Classifier with texts from airline dataset
# and save the trained object on file in resources/ directory to be used from airline-analysis.py code.

# libs
import csv
import nltk
import pickle
from textblob.classifiers import NaiveBayesClassifier

# vars
dataset = []
training = []

# settings
nltk.download('punkt')

# read csv file
with open('src/resources/Airline-Sentiment-2-w-AA.csv', 'r', encoding="ISO-8859-1") as csvFile:
	reader = csv.reader(csvFile)
	# append rows in dataset array
	for row in reader:
		dataset.append((row[14],row[5]))

# close csv file
csvFile.close()

# create training array
for i in range(1000):
	training.append(dataset[i])

# training
classifier = NaiveBayesClassifier(training)

# save NB classifier object in text file
with open('src/resources/nbclassifier', 'wb') as file:
  pickle.dump(classifier, file)
