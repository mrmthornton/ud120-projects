#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk.corpus import stopwords

stopwds = stopwords.words("english")
#print stopwds
#print len(stopwds)

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
wrd = stemmer.stem("responsive")
print wrd
