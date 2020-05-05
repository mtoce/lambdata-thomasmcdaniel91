import pandas as pd


def add_column(X, list_name, new_name):
    '''
    Takes input of a dataframe, a list and a column name as a string and appends
    it to the dataframe.
    '''
    X = X.copy()
    X[new_name] = pd.Series(list_name)
    return X


