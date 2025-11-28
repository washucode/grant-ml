"""
full_preprocessor.py

This module combines:
 - NumericCleaner
 - TextCleaner
 - GrantRatioPreprocessor
into a unified scikit-learn ColumnTransformer
that becomes the foundation of the ML pipeline.
"""

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

# to fix jissing numeric data with median,mean/most frequent / 0
from sklearn.impute import SimpleImputer

#to convert text to nuric features that model can understand TF-IDF
#Term frequency -inverse document frequency
from sklearn.feature_extraction.text import TfidfVectorizer

from .text_cleaner import TextCleaner
from .numeric_cleaner import NumericCleaner
from .ratio_preprocessor import GrantRatioPreprocessor
from .dataframe_wrapper  import DataFrameWrapper


def build_preprocessor(numeric_columns, text_columns):
    """
    Returns a complete preprocessing module that:
     - cleans numeric data
     - cleans text
     - computes ratios
     - vectorizes text
     - scales numeric features
    """

    # 1. Numeric processing pipeline
    numeric_pipeline = Pipeline([
        ("cleaner", NumericCleaner(numeric_columns)),
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()) #ensures values are in the same domain
    ])
    # 2. Ratio pipeline
    ratio_pipeline = Pipeline([
        ("ratio_gen", GrantRatioPreprocessor()),
        ("imputer", SimpleImputer(strategy="median")),   # clean unsafe values
        ("scaler", StandardScaler())
    ])
    # 3. Text processing pipeline
    text_pipeline = Pipeline([
        ("cleaner", TextCleaner(text_columns)),
        ("tfidf", TfidfVectorizer( 
            max_features=5000,
            ngram_range=(1, 2),
            stop_words="english"
        ))
    ])

    

    # 4. Master ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", DataFrameWrapper(numeric_pipeline, numeric_columns),numeric_columns),
            ("ratios",  DataFrameWrapper(ratio_pipeline, numeric_columns),numeric_columns),  # ratios use numeric columns
            ("text", DataFrameWrapper(text_pipeline, text_columns),text_columns)
            
        ],
        remainder="drop"
    )

    return preprocessor
