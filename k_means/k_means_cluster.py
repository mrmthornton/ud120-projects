#!/usr/bin/python 
# -*- coding: utf-8 -*-

""" 
    Skeleton code for k-means clustering mini-project.
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*", linewidths=0.25)
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use can be any key in the person-level dictionary (salary, director_fees, etc.)
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"
features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

#scale features "salary" and "exercised_stock_options"
from sklearn.preprocessing import MinMaxScaler

salary_mmscaler = MinMaxScaler()
#fin_data = [[elem[0]] for elem in finance_features] # include previously NaN values
fin_data = [[elem[0]] for elem in finance_features if elem[0] != 0] # ignore previously NaN values
scaled_salary = salary_mmscaler.fit_transform(fin_data)
print salary_mmscaler.transform([[200000.0]])

eso_mmscaler = MinMaxScaler()
#eso_data = [[elem[1]] for elem in finance_features] # include previously NaN values
eso_data = [[elem[1]] for elem in finance_features if elem[1] != 0] # ignore previously NaN values
scaled_eso = eso_mmscaler.fit_transform(eso_data)
print eso_mmscaler.transform([[1000000.0]])


### print min max for features
print "min of exercised stock options", min([data_dict[name][feature_2] for name in data_dict])
print "max of exercised stock options", max([elem[1] for elem in finance_features])

print "min of salary", min([data_dict[name][feature_1] for name in data_dict])
print "max of salary", max([elem[0] for elem in finance_features])


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 'for f1, f2, _ in finance_features:'
### (as it's currently written, the line below assumes 2 features)
for f1, f2, _ in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred

from sklearn.cluster import KMeans
kluster = KMeans(n_clusters=2)
kluster.fit(finance_features)
pred = kluster.predict(finance_features)


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=True, name="clusters3.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
