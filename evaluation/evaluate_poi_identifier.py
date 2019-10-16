#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.

"""     output label        Features  -->
                   |        |
                   |        |-->                      """
features_list = ["poi", "salary"]

# featureFormat() and targetFeatureSplit are from 'Tools'
data = featureFormat(data_dict, features_list)
# If for using py3, add -->        sort_keys = '../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)

from sklearn.cross_validation import train_test_split
data_train, data_test, labels_train, labels_test = \
                train_test_split(features, labels, test_size=0.30, random_state=42)

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()

#dtc.fit(features,labels)
#accuracy = dtc.score(features,labels)
dtc.fit(data_train, labels_train)
accuracy = dtc.score(data_test, labels_test)

print(accuracy)


