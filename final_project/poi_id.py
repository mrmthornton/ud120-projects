#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

################################################################################
### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

# list of all features
features_all = data_dict['METTS MARK'].keys()
''' 
'salary', 'to_messages', 'deferral_payments', 'total_payments', 
'exercised_stock_options', 'bonus', 'restricted_stock', 
'shared_receipt_with_poi', 'restricted_stock_deferred', 
'total_stock_value', 'expenses', 'loan_advances', 'from_messages', 
'other', 'from_this_person_to_poi', 'poi', 'director_fees', 
'deferred_income', 'long_term_incentive', 'email_address', 
'from_poi_to_this_person'
'''

# un-used financial features :
''' 'loan_advances', 'expenses', 'other', 'director_fees' '''
# un-used email features:
''' 'to_messages', '', 'from_poi_to_this_person', 'from_messages', 
'email_address',  '''

features_list = ['poi', 'salary', 'bonus', 'total_payments',
                 'deferral_payments', 'exercised_stock_options',
                 'restricted_stock', 'restricted_stock_deferred',
                 'shared_receipt_with_poi', 'total_stock_value',
                 'deferred_income', 'long_term_incentive',
                 'from_this_person_to_poi']

data = featureFormat(data_dict, features_list, sort_keys = False)
#data = featureFormat(data_dict, features_list, sort_keys = True)

################################################################################
### Task 2: Remove outliers
# create a dict of value, key to look up the index for a used feature.
enumerated_feature_list = dict(enumerate(features_list))
index_for = dict((v,k) for k,v in enumerated_feature_list.iteritems())




import matplotlib.pyplot as plt

# remove outliers based on "salary"
sort_by_feature = sorted(data, key = lambda x: x[index_for['salary']])
data_no_outliers = sort_by_feature[:]
'''
plt.figure(1)
plt.title('Salary v Bonus')
for point in data:
    plt.scatter( point[index_for['salary']], point[index_for['bonus']])
plt.xlabel("salary")
plt.ylabel("bonus")
'''
# remove outliers based on "bonus"
sort_by_feature = sorted(data_no_outliers, key = lambda x: x[index_for['bonus']])
print(sort_by_feature[-1][index_for['poi']])
data_no_outliers = sort_by_feature[:-1]
'''
plt.figure(2)
plt.title('Salary v Bonus removed outliers')
for point in data_no_outliers:
    plt.scatter( point[index_for['salary']], point[index_for['bonus']] )
plt.xlabel("salary")
plt.ylabel("bonus")
'''
'''
plt.figure(3)
plt.title('Salary v total_payments')
for point in data_no_outliers:
    plt.scatter( point[index_for['salary']], point[index_for['total_payments']] )
plt.xlabel("salary")
plt.ylabel("total_payments")
'''
# remove outliers based on "total payments"
sort_by_feature = sorted(data_no_outliers, key = lambda x: x[index_for['total_payments']])
print(sort_by_feature[-1][index_for['poi']])
data_no_outliers = sort_by_feature[:-1]
'''
plt.figure(4)
plt.title('Salary v total_payments removed outliers')
for point in data_no_outliers:
    plt.scatter( point[index_for['salary']], point[index_for['total_payments']] )
plt.xlabel("salary")
plt.ylabel("total_payments")
'''
'''
plt.figure(5)
plt.title('Salary v total_stock_value')
for point in data_no_outliers:
    plt.scatter( point[index_for['salary']], point[index_for['total_stock_value']] )
plt.xlabel("salary")
plt.ylabel("total_stock_value")
'''
# remove outliers based on "total stock value"
sort_by_feature = \
    sorted(data_no_outliers, key = lambda x: x[index_for['total_stock_value']])
data_no_outliers = sort_by_feature[:]
'''
plt.figure(6)
plt.title('Salary v total_stock_value removed outliers')
for point in data_no_outliers:
    plt.scatter( point[index_for['salary']], point[index_for['total_stock_value']] )
plt.xlabel("salary")
plt.ylabel("total_stock_value")
'''
'''
plt.figure(7)
plt.title('Salary v long_term_incentive')
for point in data_no_outliers:
    plt.scatter( point[index_for['salary']], point[index_for['long_term_incentive']] )
plt.xlabel("salary")
plt.ylabel("long_term_incentive")
'''
sort_by_feature = \
    sorted(data_no_outliers, key = lambda x: x[index_for['long_term_incentive']])
print(sort_by_feature[-1][index_for['poi']])
data_no_outliers = sort_by_feature[:-1]

sort_by_feature = \
    sorted(data_no_outliers, key = lambda x: x[index_for['salary']])
print(sort_by_feature[-1][index_for['poi']])
print(sort_by_feature[-2][index_for['poi']])
data_no_outliers = sort_by_feature[:-2]
'''
plt.figure(8)
plt.title('Salary v long_term_incentive removed outliers')
for point in data_no_outliers:
    plt.scatter( point[index_for['salary']], point[index_for['long_term_incentive']] )
plt.xlabel("salary")
plt.ylabel("long_term_incentive")
'''
'''
plt.figure(9)
plt.title('from_this_person_to_poi v shared_receipt_with_poi')
for point in data_no_outliers:
    plt.scatter( point[index_for['from_this_person_to_poi']], point[index_for['shared_receipt_with_poi']])
plt.xlabel("from_this_person_to_poi")
plt.ylabel("shared_receipt_with_poi")
'''
'''
plt.figure(10)
plt.title('Salary v Bonus removed outliers')
for point in data_no_outliers:
    plt.scatter( point[index_for['salary']], point[index_for['bonus']] )
plt.xlabel("salary")
'''
plt.show()

print 'number of outliers removed',\
                    len(data)-len(data_no_outliers)

################################################################################
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_no_outliers

### Extract features and labels from dataset for local testing
labels, features = targetFeatureSplit(data)

################################################################################
### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

################################################################################
### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/
###                         sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

################################################################################
### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)