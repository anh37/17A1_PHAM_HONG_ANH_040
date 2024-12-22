import pandas as pd

# Đọc dữ liệu từ file CSV
stocks1 = pd.read_csv('lab3/data/stocks1.csv')

# Bước 1: Kiểm tra xem có dữ liệu Null trong dữ liệu không
print("Thông tin tổng quan trước khi xử lý Null:")
print(stocks1.isnull().sum())

# Bước 2: Thay thế dữ liệu Null ở cột 'high' bằng giá trị trung bình của cột 'high'
high_mean = stocks1['high'].mean()
stocks1['high'].fillna(high_mean, inplace=True)

# Bước 3: Thay thế dữ liệu Null ở cột 'low' bằng giá trị trung bình của cột 'low'
low_mean = stocks1['low'].mean()
stocks1['low'].fillna(low_mean, inplace=True)

# Bước 4: Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Null
print("\nThông tin tổng quan sau khi xử lý Null:")
print(stocks1.isnull().sum())

# Xem một vài dòng dữ liệu để kiểm tra
print("\nDữ liệu mẫu sau khi xử lý:")
print(stocks1.head())
