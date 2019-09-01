#!/usr/bin/python
#  -*-  coding: utf-8  -*-

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(data)
print pca.explained_variance_ratio_
first = pca.components_[0]
second = pca.components_[1]
