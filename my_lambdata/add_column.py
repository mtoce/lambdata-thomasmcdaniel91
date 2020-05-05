import pandas as pd


def add_column(X, y, y_name):
    '''


    '''
    if X.shape[0] == len(y):
        Y = pd.Series(y)
        X[y_name] = Y
        return X
