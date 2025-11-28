"""
This module defines a custom text cleaning

Prepares text for TF or embedding models
"""


import re
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are available
nltk.download("stopwords", quiet=True)
STOPWORDS = set(stopwords.words("english"))

class TextCleaner(BaseEstimator, TransformerMixin):
    """
    Cleans and combines multiple text columns into a single processed text field.
    """

    def __init__(self, text_columns):
        self.text_columns = text_columns

    def fit(self, X, y=None):
        return self

    def _clean_text(self, text):
        """Clean individual text strings."""
        if pd.isna(text):
            return ""

        # Remove all non-alphanumeric characters
        text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
        text = text.lower()

        # Tokenize + remove stopwords
        tokens = [t for t in text.split() if t not in STOPWORDS]

        return " ".join(tokens)

    def transform(self, X):
        """Clean all text columns, then combine them into one."""
        df = pd.DataFrame(X).copy()

        # Clean each column
        for col in self.text_columns:
            df[col] = df[col].astype(str).apply(self._clean_text)

        # Combine all columns into ONE text string per row
        df["combined_text"] = df[self.text_columns].apply(
            lambda row: " ".join(row.values.astype(str)), axis=1
        )

        # Return ONLY the combined text (TF-IDF needs a 1D array-like)
        return df["combined_text"]


