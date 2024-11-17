from data_handling import load_excel, get_price, save_excel, shift_weeks, compare_to_last_week


df = load_excel('pricetracking_auto.xlsx', 'auto')
shift_weeks(df)
get_price(df)
compare_to_last_week(df)
save_excel(df, 'pricetracking_auto.xlsx', 'auto')
