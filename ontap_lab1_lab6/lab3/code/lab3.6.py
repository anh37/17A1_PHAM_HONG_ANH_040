import pandas as pd


stocks1 = pd.read_csv('lab3/data/stocks1.csv')
stocks2 = pd.read_csv('lab3/data/stocks2.csv')


stocks = pd.concat([stocks1, stocks2])


stocks['date'] = pd.to_datetime(stocks['date'], format='%d-%m-%y')


pivot_table = stocks.pivot_table(
    values='close', 
    index='date', 
    columns='symbol', 
    aggfunc='mean'
)


total_volume = stocks.groupby('symbol')['volume'].sum()
pivot_table.loc['Total Volume'] = total_volume


sorted_pivot_table = pivot_table.loc['Total Volume'].sort_values(ascending=False)


print("5 mã chứng khoán có tổng volume giao dịch cao nhất:")
print(sorted_pivot_table.head())
