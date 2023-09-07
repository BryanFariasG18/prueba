from selenium import webdriver
from selenium.webdriver.common.by import By
from db import MongoDriver

driver = webdriver.Chrome()
driver.get("https://bestcell.com.ec/")

search_box = driver.find_element(by=By.CSS_SELECTOR, value="#TextBuscar")
search_box.send_keys("Tp-Link")

search_button = driver.find_element(by=By.CSS_SELECTOR, value="#BBuscarGeneral")
search_button.click()

product_cards = driver.find_elements(By.CSS_SELECTOR, "body > div > div.container > section.py-3 > div > div > div.col-lg-9.order-1.order-lg-2.mb-5.mb-lg-0 > div:nth-child(2) > div.col-xl-4.col-lg-4.col-sm-6.mb-3")

mongodb = MongoDriver()

for card in product_cards:
    try:
        title = card.find_element(By.CSS_SELECTOR, "div > div.m-0.p-0.bg-white > h2 > b > b > b > a").text
        price = card.find_element(By.CSS_SELECTOR, "div > div.m-0.p-0.bg-white > b > b > b > p.m-0.p-0 > b > span").text
        print(title)
        print(f"${price}")

        producto_actual = {
            "title": title,
            "price": price
        }

        mongodb.insert_record(record=producto_actual, username="Tp-Link")

        print("++++++++++++++++++++++++++++++++")
    except Exception as e:
        print(e)
        print("++++++++++++++++++++++++++++++++")

driver.close()

