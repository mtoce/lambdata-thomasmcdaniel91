import pandas

def pretty_nulls(dataframe):
    '''
    turns null values into a dict and prints out the null().sum() values
    in a nice worded format.
    '''
    nulls = dict(dataframe.isnull().sum())

    for k, v in nulls.items():
        print('The column ' + str(k) + ' has ' + str(v) + ' null values.')