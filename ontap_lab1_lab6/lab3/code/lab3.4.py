import pandas as pd


stocks1 = pd.read_csv('lab3/data/stocks1.csv')
stocks2 = pd.read_csv('lab3/data/stocks2.csv')


stocks = pd.concat([stocks1, stocks2])


stocks['date'] = pd.to_datetime(stocks['date'], format='%d-%m-%y')


average_prices = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean().reset_index()


print("5 dòng đầu tiên của kết quả tính giá trung bình:")
print(average_prices.head())


average_prices.to_csv('lab3/data/stocks.csv', index=False)

print("File stocks.csv đã được tạo thành công!")
