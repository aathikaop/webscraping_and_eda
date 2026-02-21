import pandas as pd
import matplotlib.pyplot as plt

def run_eda(df):

    df = pd.read_csv("data/processed/quotes_cleaned.csv")

    #Dataset Overview
    num_of_quotes=len(df)
    print("total quotes:",num_of_quotes)

    unique_authors = df["author"].nunique()
    print("total unique authors:", unique_authors)

    #Author Analysis
    top_authors = df["author"].value_counts().head(5)
    print("top 5 authors:",top_authors)

    top_authors.plot(kind="bar")
    plt.title("Top Authors")
    plt.show()

    #Quote Length Analysis
    df["quote_length"] = df["quote"].str.len()

    df["quote_length"].plot(kind="hist", bins=20)
    plt.title("Quote Length Distribution")
    plt.show()

    longest = df.loc[df["quote_length"].idxmax()]
    shortest = df.loc[df["quote_length"].idxmin()]

    print("Longest quote:", longest["quote"])
    print("Shortest quote:", shortest["quote"])

    return df