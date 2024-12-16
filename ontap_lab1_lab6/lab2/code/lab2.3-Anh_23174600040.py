import numpy as np

# 1. Đọc dữ liệu từ các tệp
with open('C:/laptrinhaaa/python learn on class/Python learn ver3/1_on tap cuoi ky/lab2/data/efficiency.txt', 'r') as file:
    efficiency = [int(line.strip()) for line in file]

with open('C:/laptrinhaaa/python learn on class/Python learn ver3/1_on tap cuoi ky/lab2/data/shifts.txt', 'r') as file:
    shifts = [line.strip() for line in file]

# 2. Tạo numpy array np_shifts từ list shifts và kiểm tra kiểu dữ liệu
np_shifts = np.array(shifts, dtype='U10')
print("Kiểu dữ liệu của np_shifts:", np_shifts.dtype)

# 3. Tạo numpy array np_efficiency từ list efficiency và kiểm tra kiểu dữ liệu
np_efficiency = np.array(efficiency, dtype=float)
print("Kiểu dữ liệu của np_efficiency:", np_efficiency.dtype)

# 4. Tính hiệu suất sản xuất trung bình của ca 'Morning'
morning_efficiency = np_efficiency[np_shifts == 'Morning']
print("Hiệu suất trung bình của ca 'Morning':", np.mean(morning_efficiency))

# 5. Tính hiệu suất sản xuất trung bình của các ca khác
non_morning_efficiency = np_efficiency[np_shifts != 'Morning']
print("Hiệu suất trung bình của các ca khác:", np.mean(non_morning_efficiency))

# 6. Tạo mảng dữ liệu có cấu trúc workers
workers = np.zeros(len(np_shifts), dtype={
    'names': ('shift', 'efficiency'),
    'formats': ('U10', 'float')
})
workers['shift'] = np_shifts
workers['efficiency'] = np_efficiency

# 7. Sắp xếp mảng workers theo efficiency
sorted_workers = np.sort(workers, order='efficiency')
print("Mảng workers sau khi sắp xếp:")
print(sorted_workers)

highest_efficiency_shift = sorted_workers[-1]['shift']
lowest_efficiency_shift = sorted_workers[0]['shift']
print("Ca làm việc có hiệu suất cao nhất:", highest_efficiency_shift)
print("Ca làm việc có hiệu suất thấp nhất:", lowest_efficiency_shift)
