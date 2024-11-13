from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


def scraper(cpl, uid):
    url_base = 'https://auchan.hu/.p-{}'
    url = url_base.format(uid)

    opt = Options().add_argument('--search-engine-choice-country')
    driver = webdriver.Chrome(options=opt)

    try:
        driver.get(url)
        price_element = driver.find_element(By.XPATH, "//span[@class='FBX6R-Sn']")
        price_element = price_element.text
    except NoSuchElementException:
        print(f"Price not found for UID: {uid}")
        price_element = None
    finally:
        driver.quit()

    return price_element