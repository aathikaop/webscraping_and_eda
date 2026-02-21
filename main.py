from scraping import scrape_quotes
from cleaning import clean_quotes
from EDA import run_eda

def main():
    raw_df = scrape_quotes()
    clean_df = clean_quotes(raw_df)
    run_eda(clean_df)

if __name__ == "__main__":
    main()