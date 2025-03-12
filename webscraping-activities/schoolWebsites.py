from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

all_schools_websites = []

path = "C:/Users/HP/Downloads/chromedriver-win64/chromedriver.exe"

service = Service(path)
driver = webdriver.Chrome(service=service)

driver.set_page_load_timeout(120)

try: 
    url = 'https://education.gov.ng/federal-unity-colleges/'
    driver.get(url) 

    while True: 
        time.sleep(5)

        tables = driver.find_elements(By.XPATH, '//tbody')
        for table in tables:
            rows = table.find_elements(By.TAG_NAME, "tr")

            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")

                if len(cells)>=1:
                    
                    school_display = cells[0].text.strip()
                    website_column = cells[1].find_elements(By.TAG_NAME, "a")
                    school_website = website_column[0].get_attribute("href") if website_column else None # [web.get_attribute("href") for web in website_column]

                    all_schools_websites.append([school_display, school_website])

        next_button = WebDriverWait(driver,10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Next']"))
            )

        # if next_button.is_enabled()==True: 
        if "disabled" in next_button.get_attribute("class"):
            break  
        else:
            next_button.click()
            time.sleep(5)

finally:
    driver.quit()
        
df = pd.DataFrame(all_schools_websites, columns=['school', 'website'])

df.to_csv("C:\\Users\\HP\\Desktop\\feddy-db\\webscraping-activities\\fgc-websites.csv", index=False, encoding="utf-8")