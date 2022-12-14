# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 09:53:31 2018

@author: abb9
"""

import numpy as np
from numpy import genfromtxt
from imblearn.over_sampling import RandomOverSampler 

# Read from the creditcard.csv file
in_data = genfromtxt('creditcard.csv', delimiter=',')
in_data = np.array(in_data)

# Delete the first row of the file
in_data = np.delete(in_data, (0), axis=0)

X = in_data[:,0:30]
y = in_data[:, 30]

X_resampled, y_resampled = RandomOverSampler().fit_sample(X, y)
Resampled_data = np.append(X_resampled, y_resampled.reshape(-1,1), axis=1)

# Uncomment the below line to generate the csv file
#np.savetxt("RandOversampledData.csv", Resampled_data, delimiter=",")