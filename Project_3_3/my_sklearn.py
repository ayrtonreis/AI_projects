import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.model_selection import KFold, train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
import pandas as pd


#global variables
input_file = "input3.csv"
output_file = "output3.csv"





def main():
    table = pd.DataFrame(pd.read_csv(input_file), columns=['A','B','label'])
    X = table[['A', 'B']].as_matrix()   # as_matrix() returns a numpy.ndarray object
    y = table['label'].values   # values returns a numpy.ndarray from a pandas series

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.40)

    C =  [0.1, 0.5, 1, 5, 10, 50, 100]

    for c in C:
        classifier = svm.SVC(kernel='linear', C=c)

        scores = cross_val_score(classifier,X,y,cv=5,scoring='accuracy')

        print(scores)
        print("mean: ", scores.mean())
        print("done")

    #classifier.fit(X_train, y_train)

    # cross_val =StratifiedKFold(n_splits=5)
    # train_index, test_index = next(iter(cross_val.split(X, y)))
    #
    #
    # cross_val.split(X_test, y_test)

    # count = 0
    # for element in y_train:
    #     if element == 1:
    #         count+=1
    # count = count/len(y_train)

if __name__ == '__main__':
    main()
