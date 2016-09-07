#!/usr/bin/env python

import numpy as np
from sklearn import linear_model
from sklearn import tree
from sklearn import svm
from sklearn import metrics

FEATURE_NUMBER = 9

# Read train and test data
with open("../data/cancer.csv", "r") as f:
    train_dataset = np.loadtxt(f, delimiter=",")
    labels = train_dataset[:, FEATURE_NUMBER]
    features = train_dataset[:, 0:FEATURE_NUMBER]

with open("../data/cancer_test.csv", "r") as f:
    test_dataset = np.loadtxt(f, delimiter=",")
    test_labels = test_dataset[:, FEATURE_NUMBER]
    test_features = test_dataset[:, 0:FEATURE_NUMBER]

# Define the model
classifier = tree.DecisionTreeClassifier()
#classifier = svm.SVC(C=1, kernel='linear')

# Train the model
print("Start to train")
model = classifier.fit(features, labels)
print("Start to validate")
predict_labels = model.predict(test_features)
#fpr, tpr, thresholds = metrics.roc_curve(test_labels, predict_labels)
auc = metrics.roc_auc_score(test_labels, predict_labels)
accuracy = metrics.accuracy_score(test_labels, predict_labels)

# Print the metrics
print("Accuracy: {}, acu: {}".format(accuracy, auc))

