Our aim is to model the features in the given data set and use the final model to examine a credit card transaction and classify it to be fraudulent or otherwise. I want to achieve the 100% Credit Card Fraud Detection accuracy, meanwhile minimizing the incorrect Fraud predictions.# 2016.M3.TQF-ML.Credit.Card.Fraud

For my final project I choose the credit card fraud detection data set from [Kaggle](https://www.kaggle.com/dalpozz/creditcardfraud).

The dataset contains transactions made by credit cards in September 2013, by cardholders. This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.
It contains only numerical input variables which are the result of a PCA transformation. Due to confidentiality issues, we cannot know the original features and more background information about the data. Features V1, V2, ... V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise. 

My object is focused on detecting which are the main features V(i), that will help us to discover fraudolent transactions, for building a model able to discover the fraudolent transactions with 100% of accuracy. 

The main task here is to found the best model for unbalanced dataset, where there is an overwhelming class.
I'll measure the accuracy, the Area Under the Receiver operating Characteristic Curve (ROC AUC), also, I'll use the Recall ratio.
Using the confusion matrix we will have an overview of the performance of our model, so we will be able to judge the accuracy and the misclassification error.

My intention is to create classification models using: Logistic Regression, SVMs, K-nearest neighbors. I'll apply GrindSearch cross validation for hyperparameter tuning on each different classification models. I'll use these models to examine a credit card transaction and classify it to be fraudulent or otherwise and achieve 100% Credit Card Fraud Detection while minimizing the incorrect Fraud predictions.

The Undersample framework:

For this porpuse I decided to build a new dataset from the original one, which contains the whole amount of fraudolent transactions and a proportional amount of non-fraudolent transactions randomly choosen. In this way we estimate a model that stresses the features that are most meaningfull for classifing the fraudolent transactions.
I will test the estimated model, in the original dataset, to see if it is able to reach better performance.

Using Cross Validation I want to establish which is the best model, among those proposed, according to the 'Recall' ratio and The 'ROC AUC' ratio.

Using RandomForest I will establish the most meaningfull attributes, I will estimate a model using them, in the Undersample framework.
And I want to see the performance in the original dataset. I'll evaluate the accuracy and the misclassification error.

In conclusion I want to say that, for our porpose, the Logistic regression function is the most trustable model. 
Using the undersample framework we reach better performance, if we consider the misclassification error, but with a lower accuracy of our predictions.
Using the most meaningfull attributes we improve the accuracy of the model but we increase the misclassification error.

Overall I think that the Logistic regression function using the most meaningfull attributes in the undersample framework is the best model for classifing the fraudolent transactions in the original dataset.
