import pandas as pd


stocks1 = pd.read_csv('lab3/data/stocks1.csv')


print("Thông tin tổng quan trước khi xử lý Null:")
print(stocks1.isnull().sum())


high_mean = stocks1['high'].mean()
stocks1['high'].fillna(high_mean, inplace=True)


low_mean = stocks1['low'].mean()
stocks1['low'].fillna(low_mean, inplace=True)


print("\nThông tin tổng quan sau khi xử lý Null:")
print(stocks1.isnull().sum())


print("\nDữ liệu mẫu sau khi xử lý:")
print(stocks1.head())
