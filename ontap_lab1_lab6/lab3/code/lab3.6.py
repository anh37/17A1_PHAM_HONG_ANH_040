import pandas as pd

# Bước 1: Đọc file stocks1.csv và stocks2.csv vào DataFrame
stocks1 = pd.read_csv('lab3/data/stocks1.csv')
stocks2 = pd.read_csv('lab3/data/stocks2.csv')

# Bước 2: Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2])

# Bước 3: Chuyển đổi cột 'date' thành kiểu datetime
stocks['date'] = pd.to_datetime(stocks['date'], format='%d-%m-%y')

# Bước 4: Tạo Pivot Table từ DataFrame stocks
pivot_table = stocks.pivot_table(
    values='close', 
    index='date', 
    columns='symbol', 
    aggfunc='mean'
)

# Bước 5: Thêm một cột tính tổng volume giao dịch cho mỗi mã chứng khoán (symbol)
total_volume = stocks.groupby('symbol')['volume'].sum()
pivot_table.loc['Total Volume'] = total_volume

# Bước 6: Sắp xếp Pivot Table dựa trên tổng volume giao dịch, từ cao xuống thấp
sorted_pivot_table = pivot_table.loc['Total Volume'].sort_values(ascending=False)

# Bước 7: Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất
print("5 mã chứng khoán có tổng volume giao dịch cao nhất:")
print(sorted_pivot_table.head())
