"""
This module defines a custom text cleaning

Prepares text for TF or embedding models
"""


import re
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords
import nltk

#Download stopwords

nltk.download("stopwords", quiet=True)
STOPWORDS = set(stopwords.words("english"))

class TextCleaner(BaseEstimator,TransformerMixin):
    """
    Custom text cleaner for grant-related narrative fields
    """
    def __init__(self, text_columns):
        """
        parameters: text columns(list): list of column names containing text
        """
        self.text_columns = text_columns
    
    def fit(self, X, y=None):
        #no transformation needed
        return self
    
    def _clean_text(self,text):
        """
        clean text string remove noise, lower remove stopwords
        """
        if pd.isna(text):
            return ""
        
        #remove non alpha characters
        # text = re.sub(r"[^a-zA-Z0-9\s]"," ",text)
        text = re.sub(r"[^a-zA-Z0-9]"," ",text)
        #lowecase
        text = text.lower()

        #tokenize and remove stopwords
        tokens = [t for t in text.split() if t not in STOPWORDS]

        return " ".join(tokens)
    
    def transform(self, X):
        """
        Apllies cleaning to specified text columns
        output is a dataframe of cleaned text
        """
        df = X.copy()

        for col in self.text_columns:
            df[col] = df[col].astype(str).apply(self._clean_text)

        return df
