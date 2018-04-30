# -*- coding: utf-8 -*-
"""
This script is for implement a Classifier Algorithm with Cross Validation using the Holdout Method using eigth different
classifiers:
    'LDA' - Linear Discriminant Analysis
    'KNN' - K Nearest Neighbors
    'DTC' - Decision Tree Classifier
    'RFC' - Random Forest Classifier
    'ABC' - AdaBoost Classifier
    'GNB' - Gaussian NaiveBayes
    'QDA' - Quadratic Discriminant Analysis
    'SVC' - Support Vector Classifier
This script must be execute from terminal with the following structure:
python Feature_Selection.py "Data"
    :parameter Data: This parameter is the name of the folder where is located the Input Data for classification.
"""

import numpy as np
import scipy.io as sio
import sys
import multiprocessing
import pickle
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.metrics import confusion_matrix


def classification(classifier, name, x, y):
    """
        This function train a classifier with (x, y) data using a cross validation with the holdout method with a
        relationship of 40% for testing, saving the final trained classifier, the score of the classifier and
        the confusion matrix.
        Args:
            :param classifier:
                Object that contain a classifier element.
            :param name:
                Prefix for the saved data, e.g. LDA_score.npy.
            :param x:
                Matrix of n samples and n features that represent a finite number of classes.
            :param y:
                Array of n samples with the labels for the classification problem.
    """

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.4)

    print ('Training Process ' + name + ' start.')

    classifier.fit(x_train, y_train)
    fileobject = open(name, 'w')
    pickle.dump(classifier, fileobject)
    fileobject.close()

    print ('Calculating Confusion Matrix of:  ' + name)

    temp_len = len(y_test)
    y_result = np.zeros(temp_len)

    for j in range(temp_len):
        y_result[j] = classifier.predict(x_test[j, :].reshape(1, -1))

    cm = confusion_matrix(y_test, y_result)
    cm = cm.astype(dtype='float')
    cm2 = cm

    for j in range(len(cm)):
        cm2[:, j] = (cm[:, j] * 100) / sum(cm[:, j])

    np.save(name + '_cm', cm2)

    print ('Calculating Score of: ' + name)

    score = classifier.score(x_test, y_test)
    print(score)
    np.save(name + '_score', score)

    print ('Process  ' + name + ' finish')

    return


if __name__ == '__main__':

    X_npyfile = sys.argv[1]
    Y_npyfile = sys.argv[2]
    Input = np.load(X_npyfile)
    y = np.load(Y_npyfile)
    Output = np.ravel(y)

    print ('Loading Data set: Done')

    jobs = []

    LDA = multiprocessing.Process(name='LDA',
                                  target=classification,
                                  args=(LinearDiscriminantAnalysis(),
                                        'LDA',
                                        Input, Output))

    KNN = multiprocessing.Process(name='KNN',
                                  target=classification,
                                  args=(KNeighborsClassifier(15),
                                        'KNN',
                                        Input, Output))

    DTC = multiprocessing.Process(name='DTC',
                                  target=classification,
                                  args=(DecisionTreeClassifier(max_depth=128),
                                        'DTC',
                                        Input, Output))

    RFC = multiprocessing.Process(name='RFC',
                                  target=classification,
                                  args=(RandomForestClassifier(max_depth=45,
                                                               max_features=18),
                                        'RFC',
                                        Input, Output))

    ABC = multiprocessing.Process(name='ABC',
                                  target=classification,
                                  args=(AdaBoostClassifier(),
                                        'ABC',
                                        Input, Output))

    GNB = multiprocessing.Process(name='GNB',
                                  target=classification,
                                  args=(GaussianNB(),
                                        'GNB',
                                        Input, Output))

    QDA = multiprocessing.Process(name='QDA',
                                  target=classification,
                                  args=(QuadraticDiscriminantAnalysis(),
                                        'QDA',
                                        Input, Output))

    SV = multiprocessing.Process(name='SV',
                                 target=classification,
                                 args=(SVC(),
                                       'SVC',
                                       Input, Output))

    print('Starting Parallel Processing')

    Process = [LDA, KNN, DTC, RFC, ABC, GNB, QDA, SV]

    for i in Process:
        jobs.append(i)

    for i in Process:
        i.start()

    for i in Process:
        i.join()
