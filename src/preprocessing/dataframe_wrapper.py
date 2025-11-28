import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class DataFrameWrapper(BaseEstimator, TransformerMixin):
    """
    Wraps a transformer so that ColumnTransformer
    passes a pandas DataFrame slice instead of a NumPy array.
    DataFrameWrapper is a bridge between sklearn’s NumPy-based core 
    and the pandas-based custom transformers.
    """

    def __init__(self, transformer, columns):
        self.transformer = transformer
        self.columns = columns  # list of column names

    def fit(self, X, y=None):
        df = pd.DataFrame(X, columns=self.columns)
        self.transformer.fit(df, y)
        return self

    def transform(self, X):
        df = pd.DataFrame(X, columns=self.columns)
        return self.transformer.transform(df)