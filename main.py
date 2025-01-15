from data_handling import load_excel, get_price, save_excel, shift_weeks, compare_to_last_week


# Load the Excel file into a DataFrame
# File path: 'pricetracking_auto.xlsx', Sheet name: 'auto'
df = load_excel('pricetracking_auto.xlsx', 'auto')

# Shift the prices to update week-specific columns for tracking
shift_weeks(df)

# Scrape the latest prices for the products and update the DataFrame
get_price(df)

# Compare the current week's prices to the previous week's and mark promotions
compare_to_last_week(df)

# Save the updated DataFrame back to the Excel file
save_excel(df, 'pricetracking_auto.xlsx', 'auto')
