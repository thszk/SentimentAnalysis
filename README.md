# Sentiment Analysis

This program was created to provide a graphical interface for Python Sentiment Analysis implementations.


## Web Usage

For a better experience is recommended to use the site to prevent issues of installation and configurations.

Available in: https://web-sentiment-analysis.herokuapp.com/


### About the Website

The home page contains a brief description of the usage.

In the upper right corner is an information icon where you can see the developers and github where the source code is located.

In the upper left corner there is a menu that has two options, Simple Analysis and Naive B. Classifier.

In the Simple Analysis a Python program was created that basically analyzes a feeling contained in any sentence, using the polarization of the words that form the sentence. The library used was TextBlob that performs sorting based on its own word vector. The code from this feature has been available in ```src / simple-analysis.py```. This page contains a brief deion about it, and below it has two example buttons, these examples show a phrase that will appear inside the Input label and its classification will be within the Output label. If the user wants to add his own sentence, there is a textfield named "Enter the phrase" that receive a text to be classified. The text can be written in any language as long as it is recognized by the google translator. After entering the text, there is a button named "Analyze" that parses that text. Next to this button has a "Clear" button to clear the entered text, input and output results.

The Naive B. Classifier implements a sentence analysis of the Twitter discussion dataset about airline, using the Naive Bayes Classification technique implemented by the TextBlob library. This technique is a probabilistic classifier, which carries the name "naive" because do the analysis disregarding the correlation between words of the text or phrase, for example, if a car labeled "Gol" and also described as "Black", the algorithm doesn't care about the relationship between the two words since the analysis is done independently. In this page you will find a brief description, below this, there are 3 examples that can be tested by clicking on they. This implementation is available in ```src / airline-training.py``` and ```src / airline-analysis.py```, where the first file is responsible for classifier training and the second for analysis. The input text can be written only in English.


## Local Usage

To use this website in localhost is necessary to install the dependencies below:

- Node.js v10.x or later (With npm v6.x or later)
- python v3.7.3 (Usually already installed on linux distros)
- pip v18.1
- nltk v3.4.5
- textblob v0.15.3


### Installation:

Run the script from root project directory to install the dependencies: ```$ sudo src/resources/install-dependencies.sh```.

OR

If you prefer, execute the commands bellow in terminal to install the dependencies individually:

```
  $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
  $ sudo apt install -y nodejs
  $ sudo apt install python3-pip -y
  $ pip3 install newspaper3k
  $ pip3 install nltk
  $ pip3 install textblob
```


### Execution

After installing all dependencies, you need to run the commands below from root project directory:

To install Node.js dependencies:

```
  $ npm install
```

To start server:

```
  $ npm run start
```

To open the site, click on link in terminal or access ``` http://localhost:3333/ ``` in the browser.


## Developers

Thiago Suzuqui Lodi | contact: ra165478@ucdb.br

André Luiz Santana Treu Afonso | contact: ra166034@ucdb.br

João Luiz Aguiar Takayama | contact: ra165631@ucdb.br


## Directory structure

```
SentimentAnalysis/
│
├── node_modules/ - created after run $ npm install, this directory contains dependencies and cache from the Node.js
│
├── src/
│   ├── resources/
│   │   ├── Airline-Sentiment-2-w-AA.csv - dataset file
│   │   ├── install-dependencies.sh - dependencies installation script
│   │   └── nbclassifier - file to store python objects
│   │
│   ├── airline-analysis.py - airline sentiment analysis
│   ├── airline-training.py - training file to the airline sentiment analysis
│   └── simple-analysis.py - simple sentiment analysis
│
├── views/
|   ├── pages/
│   │   ├── airlineAnalysis.ejs - these files will be injected by the server in the layout.ejs
│   │   ├── freeText.ejs
│   │   └── home.ejs
│   │
│   └── layout.ejs - contains the main HTML from the site
│
├── index.js - entry point from the application
├── package-lock.json - version control from the Node.js dependencies
├── package.json - contains information about the Node.js project, necessary dependencies and npm scripts
└── requirements.txt - additional libs installed by the heroku server
```


## References

In the development process the following materials were consulted:

[Figure Eight](https://www.figure-eight.com/data-for-everyone/) website contain an list of open data sets

[Airline data set](https://d1p17r2m4rzlbo.cloudfront.net/wp-content/uploads/2016/03/Airline-Sentiment-2-w-AA.csv), here you can download the data set used in project

[Multiple buildpacks for an App](https://devcenter.heroku.com/articles/using-multiple-buildpacks-for-an-app)

[Heroku's support for Python dependencies via pip](https://devcenter.heroku.com/articles/python-pip)

[How to read csv files](https://www.programiz.com/python-programming/reading-csv-files)

[TextBlob library](https://textblob.readthedocs.io/en/dev/classifiers.html#classifying-text)