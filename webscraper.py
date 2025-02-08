from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from time import sleep


def scraper(cpl, uid):
    """
    Scrape price data from an online store.

    Args:
        cpl (str): Store name (e.g., 'Auchan', 'Tesco', 'Spar').
        uid (str or int): Unique identifier for the product.

    Returns:
        str or None: Scraped price as a string, or None if not found.
    """
    driver = webdriver.Chrome()
    cpl_mapping = {
        "Auchan": {
            "url_base": "https://auchan.hu/.p-{}",
            "xpath": "//span[@class='FBX6R-Sn']",
        },
        "Tesco": {
            "url_base": "https://bevasarlas.tesco.hu/groceries/hu-HU/products/{}",
            "xpath": "//p[contains(@class, 'eNIEDh')]",
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

    try:
        # Load the product page and retrieve price data
        sleep(2)
        driver.get(url)
        driver.delete_all_cookies()
        driver.implicitly_wait(10)
        price_element = driver.find_element(By.XPATH, xpath)
        price_element = price_element.text
    except NoSuchElementException:
        print(f"ELement not found for: {uid}")
        price_element = None
    finally:
        driver.quit()

    return price_element
