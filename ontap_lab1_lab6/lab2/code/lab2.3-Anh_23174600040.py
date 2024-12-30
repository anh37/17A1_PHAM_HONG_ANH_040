import numpy as np


with open('./lab2/data/efficiency.txt', 'r') as file:
    efficiency = [int(line.strip()) for line in file]

with open('./lab2/data/shifts.txt', 'r') as file:
    shifts = [line.strip() for line in file]


np_shifts = np.array(shifts, dtype='U10')
print("Kiểu dữ liệu của np_shifts:", np_shifts.dtype)


np_efficiency = np.array(efficiency, dtype=float)
print("Kiểu dữ liệu của np_efficiency:", np_efficiency.dtype)


morning_efficiency = np_efficiency[np_shifts == 'Morning']
print("Hiệu suất trung bình của ca 'Morning':", np.mean(morning_efficiency))


non_morning_efficiency = np_efficiency[np_shifts != 'Morning']
print("Hiệu suất trung bình của các ca khác:", np.mean(non_morning_efficiency))


workers = np.zeros(len(np_shifts), dtype={
    'names': ('shift', 'efficiency'),
    'formats': ('U10', 'float')
})
workers['shift'] = np_shifts
workers['efficiency'] = np_efficiency


sorted_workers = np.sort(workers, order='efficiency')
print("Mảng workers sau khi sắp xếp:")
print(sorted_workers)

highest_efficiency_shift = sorted_workers[-1]['shift']
lowest_efficiency_shift = sorted_workers[0]['shift']
print("Ca làm việc có hiệu suất cao nhất:", highest_efficiency_shift)
print("Ca làm việc có hiệu suất thấp nhất:", lowest_efficiency_shift)
