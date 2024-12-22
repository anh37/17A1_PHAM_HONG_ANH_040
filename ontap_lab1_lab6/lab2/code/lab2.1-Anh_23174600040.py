import numpy as np

# 1. Tạo Dữ Liệu Mô Phỏng Nhiệt Độ
temperatures = np.round(np.random.uniform(low=15, high=35, size=30), 2)  # Dữ liệu nhiệt độ 30 ngày
print("Nhiệt độ hàng ngày trong tháng:", temperatures)

# Tính nhiệt độ trung bình trong tháng
average_temp = np.mean(temperatures)
print(f"Nhiệt độ trung bình trong tháng: {average_temp:.2f} độ C")

# 2. Phân Tích Xu Hướng Nhiệt Độ
# Ngày có nhiệt độ cao nhất và thấp nhất
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
max_day = np.argmax(temperatures) + 1  # Thêm 1 vì mảng bắt đầu từ 0
min_day = np.argmin(temperatures) + 1

print(f"Nhiệt độ cao nhất: {max_temp:.2f} độ C, ngày thứ {max_day}")
print(f"Nhiệt độ thấp nhất: {min_temp:.2f} độ C, ngày thứ {min_day}")

# Sự chênh lệch nhiệt độ giữa các ngày
temp_diff = np.abs(np.diff(temperatures))  # Lấy giá trị tuyệt đối của sự khác biệt
max_diff = np.max(temp_diff)
max_diff_day = np.argmax(temp_diff) + 1  # Ngày bắt đầu của sự chênh lệch lớn nhất

print(f"Sự chênh lệch nhiệt độ lớn nhất: {max_diff:.2f} độ C, giữa ngày {max_diff_day} và {max_diff_day + 1}")

# 3. Áp Dụng Fancy Indexing
# Ngày có nhiệt độ cao hơn 20 độ C
days_above_20 = np.where(temperatures > 20)[0] + 1  # Thêm 1 vì ngày bắt đầu từ 1
print(f"Những ngày có nhiệt độ trên 20 độ C: {days_above_20}")

# Nhiệt độ của ngày 5, 10, 15, 20, 25
selected_days = [5, 10, 15, 20, 25]
selected_temperatures = temperatures[np.array(selected_days) - 1]  # Trừ 1 vì mảng bắt đầu từ 0
print(f"Nhiệt độ ngày 5, 10, 15, 20, 25: {selected_temperatures}")

# Nhiệt độ của các ngày trên trung bình
above_avg_temps = temperatures[temperatures > average_temp]
print(f"Nhiệt độ các ngày trên trung bình: {above_avg_temps}")

# Nhiệt độ của các ngày chẵn và lẻ
even_days_temps = temperatures[1::2]  # Chỉ số lẻ (ngày chẵn)
odd_days_temps = temperatures[0::2]   # Chỉ số chẵn (ngày lẻ)

print(f"Nhiệt độ các ngày chẵn: {even_days_temps}")
print(f"Nhiệt độ các ngày lẻ: {odd_days_temps}")

# 4. Đọc và phân tích file efficiency.txt
file_path = 'C:/laptrinhaaa/python learn on class/Python learn ver3/1_on tap cuoi ky/lab2/data/efficiency.txt'
efficiency = np.loadtxt(file_path, dtype=int)

# Trung bình hiệu suất
avg_efficiency = np.mean(efficiency)
print(f"Hiệu suất trung bình: {avg_efficiency:.2f}")

# Ngày có hiệu suất cao nhất và thấp nhất
max_eff = np.max(efficiency)
min_eff = np.min(efficiency)
max_eff_day = np.argmax(efficiency) + 1
min_eff_day = np.argmin(efficiency) + 1

print(f"Hiệu suất cao nhất: {max_eff}, ngày thứ {max_eff_day}")
print(f"Hiệu suất thấp nhất: {min_eff}, ngày thứ {min_eff_day}")
