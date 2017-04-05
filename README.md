Our aim is to model the features in the given data set and use this model to examine a credit card transaction and classify it to be fraudulent or otherwise and achieve 100% Credit Card Fraud Detection while minimizing the incorrect Fraud predictions.# 2016.M3.TQF-ML.Credit.Card.Fraud

For my final project I choose the credit card fraud detection data set, from :"https://www.kaggle.com/dalpozz/creditcardfraud".

The dataset contains transactions made by credit cards in September 2013, by cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.
It contains only numerical input variables which are the result of a PCA transformation. Due to confidentiality issues, we cannot know the original features and more background information about the data. Features V1, V2, ... V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise. 

My object is focused on detecting which are the main features V(i), that will help us to discover fraudolent transactions, for building a model able to discover the fraudolent transactions with 100% of accuracy. 

The main task here is to found the best model for unbalanced dataset, where there is an overwhelming class.
I'll measure the accuracy using the Area Under the Precision-Recall Curve (AUPRC) and, also, I'll use the Confusion matrix.

My intention is to create classification models using: Logistic Regression, SVMs, Decision trees, K-nearest neighbors. I'll apply cross validation for hyperparameter tuning on each different classification models. I'll use this model to examine a credit card transaction and classify it to be fraudulent or otherwise and achieve 100% Credit Card Fraud Detection while minimizing the incorrect Fraud predictions.

