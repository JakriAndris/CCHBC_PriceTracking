import pandas as pd
from webscraper import scraper
import numpy as np


def load_excel(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name)
    return df


def save_excel(df, file_path, sheet_name):
    df.to_excel(excel_writer=file_path, sheet_name=sheet_name, index=False)


def clean_scraped_data(price):
    if price is None:
        return 0

    cleaned_price = ''.join(c for c in price if c.isdigit())

    if cleaned_price:
        return int(cleaned_price)
    else:
        return 0


def get_price(df):
    for i in range(0, len(df)):
        cpl = df.iat[i, 0]
        uid = df.iat[i, 2]

        if pd.isna(uid):
            continue
        else:
            try:
                uid = int(uid)
            except ValueError:
                uid = str(uid)

        value = clean_scraped_data(scraper(cpl, uid))
        df.iat[i, 3] = value


def shift_weeks(df):
    df[["PRICE (W-2)", "PROMO PRICE (W-2)"]] = np.nan

    df["PRICE (W-2)"] = df["PRICE (W-1)"]
    df["PROMO PRICE (W-2)"] = df["PROMO PRICE (W-1)"]
    df["PRICE (W-1)"] = df["PRICE (W)"]
    df["PROMO PRICE (W-1)"] = df["PROMO PRICE (W)"]

    df[["PRICE (W)", "PROMO PRICE (W)"]] = np.nan
