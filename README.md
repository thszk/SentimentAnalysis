# Sentiment Analysis

This program was created to provide a graphical interface for Python Sentiment Analysis implementations.


## Web Usage

For a better experience is recommended to use the site to prevent issues of installation and configurations.

Available in: https://web-sentiment-analysis.herokuapp.com/


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


## References

In the development process the following materials were consulted:

[Figure Eight](https://www.figure-eight.com/data-for-everyone/) website contain an list of open data sets

[Airline data set](https://d1p17r2m4rzlbo.cloudfront.net/wp-content/uploads/2016/03/Airline-Sentiment-2-w-AA.csv), here you can download the data set used in project

[Multiple buildpacks for an App](https://devcenter.heroku.com/articles/using-multiple-buildpacks-for-an-app)

[Heroku's support for Python dependencies via pip](https://devcenter.heroku.com/articles/python-pip)

[How to read csv files](https://www.programiz.com/python-programming/reading-csv-files)

[TextBlob library](https://textblob.readthedocs.io/en/dev/classifiers.html#classifying-text)