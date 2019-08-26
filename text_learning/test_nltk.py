#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import stopwords
stopwds = stopwords.words("english")

from sklearn.feature_extraction import stop_words
stopwds = stop_words.ENGLISH_STOP_WORDS

from sklearn.feature_extraction.text import TfidfVectorizer
tfidfVec = TfidfVectorizer( stop_words=stopwds)

#print stopwds
print len(stopwds)



#from nltk.stem.snowball import SnowballStemmer
#stemmer = SnowballStemmer("english")
#wrd = stemmer.stem("responsive")
#print wrd
