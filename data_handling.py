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
    return int(cleaned_price)


def get_price(df):

    for i in range(0, len(df)):
        last_cpl = df.iat[i-1, 0]
        cpl = df.iat[i, 0]
        name = df.iat[i, 1]
        uid = df.iat[i, 2]

        if pd.isna(uid):
            continue
        else:
            try:
                uid = int(uid)
            except ValueError:
                uid = str(uid)

        if last_cpl != cpl:
            save_excel(df, 'pricetracking_auto.xlsx', 'auto')

        print(f"CPL: {cpl} | Product name: {name}", end=" | ")

        try:
            value = clean_scraped_data(scraper(cpl, uid))
        except ValueError:
            value = 0

        print(f"Price: {value}")

        df.iat[i, 3] = value


def shift_weeks(df):
    df[["PRICE (W-2)", "PROMO PRICE (W-2)"]] = np.nan

    df["PRICE (W-2)"] = df["PRICE (W-1)"]
    df["PROMO PRICE (W-2)"] = df["PROMO PRICE (W-1)"]
    df["PRICE (W-1)"] = df["PRICE (W)"]
    df["PROMO PRICE (W-1)"] = df["PROMO PRICE (W)"]

    df[["PRICE (W)", "PROMO PRICE (W)"]] = np.nan


def compare_to_last_week(df):
    for i, row in df.iterrows():
        current_price = row['PRICE (W)']
        last_week_price = row['PRICE (W-1)']

        if current_price == 0:
            continue

        if current_price < last_week_price:
            df.at[i, 'PROMO PRICE (W)'] = current_price
            df.at[i, 'PRICE (W)'] = last_week_price
