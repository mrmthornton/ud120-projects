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


data = featureFormat(data_dict, features_list)
#data = featureFormat(data_dict, features_list, sort_keys = True)

################################################################################
### Task 2: Remove outliers

enumerated_feature_list = dict(enumerate(features_list))
index_for = dict((v,k) for k,v in enumerated_feature_list.iteritems())

selection_with_outliers = [[elem[index_for['salary']],
                           elem[index_for['bonus']],
                elem[index_for['salary']] * elem[index_for['bonus']]
        ] for elem in data]

sort_by_feature = sorted(selection_with_outliers, key = lambda x: x[2])

return_length = int(len(data)*0.97)
data_no_outliers = sort_by_feature[:return_length] #select first 90%
print 'number of outliers removed',\
                           len(selection_with_outliers)-len(data_no_outliers)

import matplotlib.pyplot as plt

plt.figure(1)
plt.title('Salary v Bonus')
for point in selection_with_outliers:
    plt.scatter( point[index_for['salary']], point[index_for['bonus']] )
plt.xlabel("salary")
plt.ylabel("bonus")

plt.figure(2)
plt.title('Salary v Bonus removed outliers')
for point in data_no_outliers:
    plt.scatter( point[index_for['salary']], point[index_for['bonus']] )
plt.xlabel("salary")
plt.ylabel("bonus")

plt.show()


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
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

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