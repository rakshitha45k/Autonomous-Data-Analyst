import pandas as pd

def clean_data(df):
    # Make a copy to avoid modifying original
    df = df.copy()

    # Drop rows with missing values
    df = df.dropna()

    # Convert date column
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Remove rows with invalid dates
    df = df.dropna(subset=["date"])

    # Reset index after cleaning
    df = df.reset_index(drop=True)

    return df
