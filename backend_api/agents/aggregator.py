# agents/aggregation.py

import pandas as pd


def aggregate(df: pd.DataFrame, column: str, agg: str):
    """
    Generic aggregation handler
    """

    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset")

    if agg == "mean":
        return round(df[column].mean(), 3)

    if agg == "sum":
        return int(df[column].sum())

    if agg == "max":
        return df[column].max()

    if agg == "min":
        return df[column].min()

    if agg == "count":
        return int(df[column].count())

    raise ValueError(f"Unsupported aggregation type: {agg}")
