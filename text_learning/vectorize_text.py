#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pickle
import sys

sys.path.append("../tools/")
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""

from_sara = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development
### there are thousands of emails from Sara and Chris, so running over all of them can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you can iterate your modifications quicker
temp_counter = 0
for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        if temp_counter >= 200:
            break
        else:
            path = os.path.join('..', path[:-1])
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            text_parsed = parseOutText(email)
            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            remove_words = ("sara", "shackleton", "chris", "germani",
                            "sshacklensf", "cgermannsf")  # see lesson 12-29, feature selection
            text_no_signature = text_parsed
            for remove_word in remove_words:
                text_no_signature = text_no_signature.replace(remove_word, "")
            ### append the text to word_data
            word_data.append(text_no_signature)
            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            from_data.append(int(name == "chris"))

            email.close()
        #temp_counter += 1 # comment this line out for the full email count

print "emails processed"
#print word_data[152]
from_sara.close()
from_chris.close()

pickle.dump(word_data, open("your_word_data.pkl", "w"))
pickle.dump(from_data, open("your_email_authors.pkl", "w"))

### in Part 4, do TfIdf vectorization here

#from nltk.corpus import stopwords
#stop_words = stopwords.words("english")
from sklearn.feature_extraction import stop_words
stopwds = stop_words.ENGLISH_STOP_WORDS
'''
from sklearn.feature_extraction.text import CountVectorizer
countVec = CountVectorizer(stop_words=stopwds)
vector = countVec.fit_transform(word_data)
all_features = countVec.get_feature_names()
length = len(all_features)
vecToArr = vector.toarray()
print vecToArr.shape

test_transform = countVec.transform(["enron"]).toarray()
print test_transform.shape
print countVec.vocabulary_.get('document')

from sklearn.feature_extraction.text import CountVectorizer
'''

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words=stopwds)
vectorizer.fit_transform(word_data, from_data)
all_features = vectorizer.get_feature_names()
print len(all_features)
print all_features[34597]

pass # a place to stop debugger
