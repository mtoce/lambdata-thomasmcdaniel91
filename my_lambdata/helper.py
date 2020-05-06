import pandas as pd
df = pd.read_csv(r"C:\Users\Thomas\Datasets\Islander_data.csv")
names = list(df['last_name'])


class Additions():
    def __init__(self, df, list_name, new_col_name):
        self.df = df
        self.list_name = list_name
        self.new_col_name = new_col_name

    def exten_df(self, df, list_name, new_col_name):
        X = df.copy()
        X[new_col_name] = pd.Series(list_name)
        return X

if __name__ == "__main__":
    new_df = Additions(df, names, 'last')
    new_df = new_df.exten_df(df, names, 'last')
    print(new_df.head())