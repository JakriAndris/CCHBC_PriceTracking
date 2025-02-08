import pandas as pd
from webscraper import scraper
import numpy as np


def load_excel(file_path, sheet_name):
    """
    Load an Excel file into a pandas DataFrame.

    Args:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to load.

    Returns:
        DataFrame: Loaded data.
    """
    df = pd.read_excel(file_path, sheet_name)
    return df


def save_excel(df, file_path, sheet_name):
    """
    Save a pandas DataFrame to an Excel file.

    Args:
        df (DataFrame): Data to save.
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to save data in.
    """
    df.to_excel(excel_writer=file_path, sheet_name=sheet_name, index=False)


def clean_scraped_data(price):
    """
    Clean and convert scraped price data into an integer.

    Args:
        price (str or None): Scraped price as a string.

    Returns:
        int: Cleaned price value. Defaults to 0 if invalid.
    """
    if price is None:
        return 0
    cleaned_price = ''.join(c for c in price if c.isdigit())
    return int(cleaned_price)


def get_price(df):
    """
    Scrape and update prices in the DataFrame for each product.

    Args:
        df (DataFrame): Product data containing CPL (source), product name, and UID.
    """
    for i in range(0, len(df)):
        last_cpl = df.iat[i-1, 0]
        cpl = df.iat[i, 0]
        name = df.iat[i, 1]
        uid = df.iat[i, 2]

        # Skip row if UID is missing
        if pd.isna(uid):
            continue
        else:
            try:
                uid = int(uid)
            except ValueError:
                uid = str(uid)

        # Save data to Excel if the CPL changes
        if last_cpl != cpl:
            save_excel(df, 'pricetracking_auto.xlsx', 'auto')

        print(f"CPL: {cpl} | Product name: {name}", end=" | ")

        try:
            # Scrape and clean the price data
            value = clean_scraped_data(scraper(cpl, uid))
        except ValueError:
            value = 0

        if value == 0:
            print(f"Price: {value}")

        # Update the price in the DataFrame
        df.iat[i, 3] = value


def shift_weeks(df):
    """
    Shift weekly price data to maintain historical tracking.

    Args:
        df (DataFrame): Product data containing weekly price columns.
    """
    # Initialize new columns for two-week-old data
    df[["PRICE (W-2)", "PROMO PRICE (W-2)"]] = np.nan

    # Shift data from current and previous weeks to older columns
    df["PRICE (W-2)"] = df["PRICE (W-1)"]
    df["PROMO PRICE (W-2)"] = df["PROMO PRICE (W-1)"]
    df["PRICE (W-1)"] = df["PRICE (W)"]
    df["PROMO PRICE (W-1)"] = df["PROMO PRICE (W)"]

    # Clear the current week's columns for new data
    df[["PRICE (W)", "PROMO PRICE (W)"]] = np.nan


def compare_to_last_week(df):
    """
    Compare current week's prices with last week's prices and identify promotions.

    Args:
        df (DataFrame): Product data containing price columns for current and previous weeks.
    """
    for i, row in df.iterrows():
        current_price = row['PRICE (W)']
        last_week_price = row['PRICE (W-1)']

        # Skip rows where the current price is unavailable
        if current_price == 0:
            continue

        # Mark as a promotion if the current price is lower than last week's price
        if current_price < last_week_price:
            df.at[i, 'PROMO PRICE (W)'] = current_price
            df.at[i, 'PRICE (W)'] = last_week_price
