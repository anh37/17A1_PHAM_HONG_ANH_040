import pandas as pd

# Bước 1: Đọc file stocks1.csv và stocks2.csv vào DataFrame
stocks1 = pd.read_csv('lab3/data/stocks1.csv')
stocks2 = pd.read_csv('lab3/data/stocks2.csv')

# Bước 2: Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2])

# Bước 3: Chuyển đổi cột 'date' thành kiểu datetime
stocks['date'] = pd.to_datetime(stocks['date'], format='%d-%m-%y')

# Bước 4: Tạo MultiIndex cho DataFrame stocks bằng cột 'date' và 'symbol'
stocks.set_index(['date', 'symbol'], inplace=True)

# Bước 5: Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume trung bình
grouped = stocks.groupby(['date', 'symbol'])[['open', 'high', 'low', 'close', 'volume']].mean()

# Bước 6: Sắp xếp dữ liệu theo ngày và mã chứng khoán
grouped_sorted = grouped.sort_index()

# Bước 7: Hiển thị kết quả cho 5 ngày đầu tiên
print("Kết quả tính giá và volume trung bình cho 5 ngày đầu tiên:")
print(grouped_sorted.head())
