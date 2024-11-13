from data_handling import load_excel, get_price, save_excel


df = load_excel('pricetracking_auto.xlsx', 'auto')
get_price(df)
save_excel(df, 'pricetracking_auto.xlsx', 'auto')
