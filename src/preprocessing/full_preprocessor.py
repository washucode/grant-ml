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
from sklearn.impute import SimpleImputer
from sklearn.feature_extraction.text import TfidfVectorizer

from .text_cleaner import TextCleaner
from .numeric_cleaner import NumericCleaner
from .ratio_preprocessor import GrantRatioPreprocessor


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
        ("scaler", StandardScaler())
    ])

    # 2. Text processing pipeline
    text_pipeline = Pipeline([
        ("cleaner", TextCleaner(text_columns)),
        ("tfidf", TfidfVectorizer(
            max_features=5000,
            ngram_range=(1, 2),
            stop_words="english"
        ))
    ])

    # 3. Ratio pipeline
    ratio_pipeline = Pipeline([
        ("ratio_gen", GrantRatioPreprocessor()),
        ("imputer", SimpleImputer(strategy="median")),   # clean unsafe values
        ("scaler", StandardScaler())
    ])

    # 4. Master ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, numeric_columns),
            ("text", text_pipeline, text_columns),
            ("ratios", ratio_pipeline, numeric_columns)  # ratios use numeric columns
        ],
        remainder="drop"
    )

    return preprocessor
