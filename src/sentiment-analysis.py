import keras
import numpy as np
import pandas as pd
from keras.datasets import imdb
from sklearn.model_selection import train_test_split
import re
most_used_words = {}

# dataset
dataset = pd.read_csv('Airline-Sentiment-2-w-AA.csv', encoding="ISO-8859-1")
print(len(dataset))
texts = dataset['text']
classifications = dataset['airline_sentiment']
text_training, text_test, class_training, class_test = train_test_split(texts,classifications, test_size=0.25)
palavras_filtradas = []
for text in texts:
	palavras = text.split()
	for palavra in palavras:
		x = re.findall("[^a-zA-Z]+", palavra)
		if x == []:
			palavras_filtradas.append(palavra.upper())
			try:
				if most_used_words[palavras_filtradas[-1]]:
					most_used_words[palavras_filtradas[-1]]+=1
			except:
				most_used_words[palavras_filtradas[-1]]=1


most_used_words = sorted(most_used_words.items(), key = lambda x : x[1], reverse = True)
while len(most_used_words) > 5000:
	most_used_words.pop()

print(classifications)
print(most_used_words)

# def most_frequent(List): 
#     return max(set(List), key = List.count) 

# def remove_values_from_list(the_list, val):
#    return [value for value in the_list if value != val]
  
# while len(most_used_words) < 10000:
# 	mais_frequente = most_frequent(palavras_filtradas)
# 	count = palavras_filtradas.count(mais_frequente)
# 	if not most_used_words[mais_frequente]:
# 		most_used_words[mais_frequente] = 0
# 	else:
# 		most_used_words[mais_frequente]+=1
# 	# most_used_words.append([mais_frequente, count])
# 	# palavras_filtradas = remove_values_from_list(palavras_filtradas, mais_frequente)
# 	print(mais_frequente, count)


# print(most_used_words)
	
# a = {}
# try:
#   if a["A"]:
#   	a["A"]+=1
# except:
#   a["A"]=0

# print(a["A"])


