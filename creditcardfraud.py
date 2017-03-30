# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 16:14:59 2017

@author: Giuseppe
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_creditcard = pd.read_csv('creditcard.csv', ",")
df_creditcard.head()
classes = pd.value_counts(df_creditcard['Class'], sort = True).sort_index()
classes.plot(kind = 'bar')
plt.title("Fraud class histogram")
plt.xlabel("Class")
plt.ylabel("Frequency")