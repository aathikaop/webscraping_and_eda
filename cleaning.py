import pandas as pd

def clean_quotes(df):

    df = pd.read_csv("data/raw/quotes_raw.csv")

    #remove duplicates
    df=df.drop_duplicates()

    #Convert tags into structured format
    df["tags"] = df["tags"].astype(str)
    df["tags"]=df["tags"].str.replace("[", "").str.replace("]", "")
    df["tags"]=df["tags"].str.replace("'", "").str.strip()

    #Strip extra whitespace
    for col in ["quote", "author", "tags"]:
        df[col] = df[col].astype(str).str.strip()

    #Handle missing values
    df = df.dropna()

    df.to_csv("data/processed/quotes_cleaned.csv", index=False)

    print(df.head())

    return df