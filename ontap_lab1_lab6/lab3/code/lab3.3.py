import pandas as pd

# Đọc file stocks1.csv và stocks2.csv vào DataFrame
stocks1 = pd.read_csv('lab3/data/stocks1.csv')
stocks2 = pd.read_csv('lab3/data/stocks2.csv')

# Bước 2: Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2])

# Bước 3: Chuyển đổi cột 'date' thành kiểu datetime
stocks['date'] = pd.to_datetime(stocks['date'], format='%d-%m-%y')

# Bước 4: Tính giá trung bình (open, high, low, close) cho mỗi ngày và từng symbol
average_prices = stocks.groupby(['date', 'symbol'])[['open', 'high', 'low', 'close']].mean().reset_index()

# Bước 5: Xuất kết quả ra file stocks.csv
average_prices.to_csv('lab3/data/stocks.csv', index=False)

print("File stocks.csv đã được tạo thành công!")
