import pandas as pd


stocks1 = pd.read_csv("lab3/data/stocks1.csv")


print("5 dòng đầu tiên của stocks1:")
print(stocks1.head())


print("\nKiểu dữ liệu của mỗi cột trong stocks1:")
print(stocks1.dtypes)


print("\nThông tin tổng quan của stocks1:")
print(stocks1.info())
