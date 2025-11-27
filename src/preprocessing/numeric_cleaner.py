"""
Cleans nummeric fields for grant ML analuysus
 - convert string to numbers 
 - fill missing values
 - consistence in numeric types
"""


import pandas as pd
import numpy as np
from sklearn.base  import BaseEstimator, TransformerMixin
import re

class NumericCleaner(BaseEstimator, TransformerMixin):
    """
    Converts numeric fields to clean numeric values
    Removes impossinle values and fills missing data
    """

    def __init__(self, numeric_columns):
        self.numeric_columns = numeric_columns
        # Supported currency names (extendable anytime)
        self.currency_words = [
            "kes", "ksh", "kshs", "usd", "eur", "gbp", "ugx", "tzs", "zar",
            "cfa", "etb", "ngn", "rwf", "cad", "aud", "inr", "yen", "jpy"
        ]

        # Currency symbols
        self.currency_symbols = r"[$€£¥]"
    
    def fit(self, X, y=None):
        return self
    
    def _clean_nummeric_text(self,value):
        """
        Removes currency words , symbols , commas etc
        """
        if pd.isna(value):
            return 0
        
        text = str(value).lower()

        #Remove currency words
        for words in self.currency_words:
            text.replace(words,"")
        
        #Remove currencybsymbols using regex

        text = re.sub(self.currency_symbols,"",text)

        #remove comma and brakets
        text = text.replace(",","")
        text.replace("(","").replace(")","")

           # Remove approx words
        text = re.sub(r"(approx|est|estimated)", " ", text)

        # Remove all non-numeric characters except . and -
        text = re.sub(r"[^0-9\.\-]", " ", text)

        # Convert to float
        try:
            return float(text.strip())
        except:
            return 0

    
    def transform(self, X):
        df = X.copy()

        for col in self.numeric_columns:
            if col in df.columns:
                df[col]=df[col].apply(self._clean_nummeric_text)
        
        df[self.numeric_columns]=df[self.numeric_columns].fillna(0)
        return df