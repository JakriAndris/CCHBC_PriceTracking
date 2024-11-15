import pandas as pd
from webscraper import scraper


def load_excel(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name)
    return df


def save_excel(df, file_path, sheet_name):
    df.to_excel(excel_writer=file_path, sheet_name=sheet_name, index=False)


def clean_scraped_data(price):
    cleaned_price = ''.join(c for c in price if c.isdigit())
    return int(cleaned_price)


def get_price(df):
    for i in range(0, len(df)):
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

        print(f"CPL: {cpl} | Product name: {name}", end=" | ")

        try:
            value = clean_scraped_data(scraper(cpl, uid))
        except ValueError:
            value = 0

        print(f"Price: {value}")

        df.iat[i, 3] = value
