# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 18:57:16 2022

@author: pchri
"""

import numpy as np
import matplotlib as mpl
import pandas as pd
import sklearn as skl

#load dataset
url = r'C:\Users\pchri\Downloads\sonar.all-data.csv'
dataset = pd.read_csv(url, header=None)
dataset = dataset.drop(dataset.index[0])

#shape
print(dataset.shape)

#types
pd.set_option('display.max_rows', 500)
print(dataset.dtypes)

#head
pd.set_option('display.width', 100)
print(dataset.head(20))

#descriptions, change precision to 3 places
pd.set_option('precision', 3)
print(dataset.describe())

#class distribution
print(dataset.groupby(60).size())

#histograms
dataset.hist(sharex=False, sharey=False, xlabelsize=1, ylabelsize=1)
pyplot.show()

