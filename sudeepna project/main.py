from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

browser = webdriver.Firefox()

browser.get("https://www.daraz.com.np/")

browser.maximize_window()

search_input = browser.find_element(By.XPATH, '//*[@id="q"]')
search_button = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/form/div/div[2]/button')

search_input.send_keys("iphone 15")
sleep(1)
search_button.click()

products = []
for i in range(10):
    print('Scraping page', i+1)
    browser.save_full_page_screenshot(f'screenshot{i}.png')
    product = browser.find_elements(By.XPATH, "//*[@id='id-a-link']")
    for p in product:
        products.append(p.text)
    next_button = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div/div/div[1]/div[3]/div/div/ul/li[9]/a")
    next_button.click()
    sleep(2)

browser.quit()

print(products)

df = pd.DataFrame(products)
print(df)
df.to_csv('products.csv')

