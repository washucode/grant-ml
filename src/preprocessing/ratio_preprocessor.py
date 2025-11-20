"""

Computes the 5 optimized financial ratios used in grant prediction:
    1. Grant Absorption
    2. Grant Dependency
    3. Budget Stability
    4. Liquidity
    5. Growth-Adjusted Grant Ratio
"""

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class GrantRatioPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        df = X.copy()

        # Ratio 1: Grant Absorption (capacity)
        df["ratio_absorption"] = df["past_grants_total"] / (df["annual_budget"] + 1)

        # Ratio 2: Grant Dependency (financial resilience)
        df["ratio_dependency"] = df["past_grants_total"] / (df["total_revenue"] + 1)

        # Ratio 3: Budget Stability (trend)
        df["ratio_budget_stability"] = df["annual_budget"] / (df["annual_budget_last_year"] + 1)

        # Ratio 4: Liquidity (shock survival)
        df["ratio_liquidity"] = df["cash_reserves"] / (df["monthly_operating_expenses"] + 1)

        # Ratio 5: Growth-Adjusted (equity + innovation lens)
        df["ratio_growth_adjusted"] = df["past_grants_total"] / (
            (df["years_active"] + 1) * (df["annual_budget"] + 1)
        )

        # Normalize bad values
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        df.fillna(0, inplace=True)

        return df
