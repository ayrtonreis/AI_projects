import numpy as np
from sklearn import preprocessing, cross_validation, svm, linear_model, tree, ensemble
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold, train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
import pandas as pd


#global variables
input_file = "input3.csv"
output_file = "output3.csv"


def main():
    table = pd.DataFrame(pd.read_csv(input_file), columns=['A','B','label'])
    X = table[['A', 'B']].as_matrix()   # as_matrix() returns a numpy.ndarray object
    y = table['label'].values   # values returns a numpy.ndarray from a pandas series

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40)

    # Set the parameters by cross-validation
    # tuned_parameters = [{'kernel': ['linear'], 'C':  [0.1, 0.5, 1, 5, 10, 50, 100]},
    #                     {'kernel': ['poly'], 'gamma': [0.1, 1], 'C': [0.1, 1, 3], 'degree': [4, 5, 6]},
    #                     {'kernel': ['rbf'], 'gamma': [0.1, 0.5, 1, 3, 6, 10], 'C':  [0.1, 0.5, 1, 5, 10, 50, 100]}
    #                     ]

    model = ensemble.RandomForestClassifier()
    tuned_parameters = {'max_depth': [i for i in range(1, 50)], 'min_samples_split':  [i for i in range(2, 10)]}

    print("start")

    clf = GridSearchCV(model, tuned_parameters, cv=5, scoring='accuracy')
    clf.fit(X_train, y_train)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
    print()
    print("Grid scores on development set:")
    print()
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    max_mean = 0
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        max_mean = max(max_mean, mean)
        print("%0.3f (+/-%0.03f) for %r"
              % (mean, std * 2, params))
    print()
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()
    y_true, y_pred = y_test, clf.predict(X_test)
    test_acucuracy = accuracy_score(y_true, y_pred)
    print("Max in-sample: ", max_mean)
    print("Test Accuracy: ", test_acucuracy)
    #print(classification_report(y_true, y_pred))
    print()
    print("end")

if __name__ == '__main__':
    main()
