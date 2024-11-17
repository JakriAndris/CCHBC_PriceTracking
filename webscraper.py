from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def scraper(cpl, uid):
    cpl_mapping = {
        "Auchan": {
            "url_base": "https://auchan.hu/.p-{}",
            "xpath": "//span[@class='FBX6R-Sn']",
        },
        "Tesco": {
            "url_base": "https://bevasarlas.tesco.hu/groceries/hu-HU/products/{}",
            "xpath": "//span[@data-auto='price-value']",
        },
        "Spar": {
            "url_base": "https://www.spar.hu/onlineshop/p/{}",
            "xpath": "//label[@data-baseprice]",
        },
    }

    cpl_config = cpl_mapping.get(cpl)
    if not cpl_config:
        raise ValueError(f"Unsupported CPL: {cpl}")

    url_base = cpl_config["url_base"]
    xpath = cpl_config["xpath"]

    url = url_base.format(uid)

    driver = webdriver.Chrome()

    try:
        driver.get(url)
        driver.implicitly_wait(5)
        price_element = driver.find_element(By.XPATH, xpath)
        price_element = price_element.text
    except NoSuchElementException:
        print(f"ELement not found for: {uid}")
        price_element = None
    finally:
        driver.quit()

    return price_element
