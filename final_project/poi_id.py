#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

#########################################################################
### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

# unused financial features :
''' 'loan_advances', 'expenses', 'other', 'director_fees' '''
# unused email features:
''' 'to_messages', '', 'from_poi_to_this_person', 'from_messages', '''
features_list = ['poi', 'salary', 'bonus', 'total_payments',\
                 'deferral_payments', 'exercised_stock_options',\
                 'restricted_stock', 'restricted_stock_deferred',\
                 'shared_receipt_with_poi', 'total_stock_value',\
                 'deferred_income', 'long_term_incentive'\
                 'email_address', 'from_this_person_to_poi'],\
                 'shared_receipt_with_poi',
features_all = data_dict['METTS MARK'].keys()
enum_all = list(enumerate(features_all))


# list of features_all
''' 
'salary', 'to_messages', 'deferral_payments', 'total_payments', 
'exercised_stock_options', 'bonus', 'restricted_stock', 
'shared_receipt_with_poi', 'restricted_stock_deferred', 
'total_stock_value', 'expenses', 'loan_advances', 'from_messages', 
'other', 'from_this_person_to_poi', 'poi', 'director_fees', 
'deferred_income', 'long_term_incentive', 'email_address', 
'from_poi_to_this_person'
'''

#########################################################################
### Task 2: Remove outliers
import matplotlib.pyplot as plt
data = featureFormat(data_dict, features_list)

return_length = int(len(data)*0.9)
with_outliers = zip(poi, net_worths, (net_worths - predictions)**2)
sort_by_err = sorted(with_error, key = lambda x: x[2])
cleaned_data = sort_by_err[:return_length] #select first 90%

plt.figure(1)
for point in data:
    salary = point[1]
    bonus = point[2]
    total_payments = point[3]
    plt.scatter( salary, bonus )
plt.xlabel("salary")
plt.ylabel("bonus")

plt.figure(2)
for point in data:
    salary = point[1]
    bonus = point[2]
    total_payments = point[3]
    plt.scatter( salary, total_payments )
plt.xlabel("salary")
plt.ylabel("total_payments")

plt.figure(3)
for point in data:
    salary = point[1]
    bonus = point[2]
    total_payments = point[3]
    plt.scatter( bonus, total_payments )
plt.xlabel("bonus")
plt.ylabel("total_payments")

plt.show()

#########################################################################
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

#########################################################################
### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

#########################################################################
### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

#########################################################################
### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)