from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def scraper(cpl, uid):
    url_base = 'https://auchan.hu/.p-{}'
    url = url_base.format(uid)

    driver = webdriver.Chrome()

    try:
        driver.get(url)
        driver.implicitly_wait(3)
        price_element = driver.find_element(By.XPATH, "//span[@class='FBX6R-Sn']")
        price_element = price_element.text
    except NoSuchElementException:
        print(f"ELement not found for: {uid}")
        price_element = None
    finally:
        driver.quit()

    return price_element
