from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def scrape_quotes():

    driver=webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    wait=WebDriverWait(driver,10)

    url="https://quotes.toscrape.com/js/"
    driver.get(url)

    data = []
    pages_to_scrape = 5
    current_page = 1

    while current_page <= pages_to_scrape:

        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))

        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        print(quotes)
        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text
            tags = quote.find_elements(By.CLASS_NAME, "tag")
            tags = [t.text for t in tags]
        

            data.append({
                "quote": text,
                "author": author,
                "tags": tags
            })


        try:
            next_btn = driver.find_element(By.CLASS_NAME, "next")
            next_btn.find_element(By.TAG_NAME, "a").click()

            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))

            current_page += 1

        except:
            break

    df = pd.DataFrame(data)
    df.to_csv("data/raw/quotes_raw.csv", index=False)
    print(len(data))

    driver.quit()

    return df