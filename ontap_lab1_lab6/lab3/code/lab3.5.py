import pandas as pd


stocks1 = pd.read_csv('lab3/data/stocks1.csv')
stocks2 = pd.read_csv('lab3/data/stocks2.csv')


stocks = pd.concat([stocks1, stocks2])


stocks['date'] = pd.to_datetime(stocks['date'], format='%d-%m-%y')


stocks.set_index(['date', 'symbol'], inplace=True)


grouped = stocks.groupby(['date', 'symbol'])[['open', 'high', 'low', 'close', 'volume']].mean()


grouped_sorted = grouped.sort_index()


print("Kết quả tính giá và volume trung bình cho 5 ngày đầu tiên:")
print(grouped_sorted.head())
