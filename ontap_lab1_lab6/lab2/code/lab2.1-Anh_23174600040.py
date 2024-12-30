import numpy as np


temperatures = np.round(np.random.uniform(low=15, high=35, size=30), 2)  
print("Nhiệt độ hàng ngày trong tháng:", temperatures)


average_temp = np.mean(temperatures)
print(f"Nhiệt độ trung bình trong tháng: {average_temp:.2f} độ C")



max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
max_day = np.argmax(temperatures) + 1  
min_day = np.argmin(temperatures) + 1

print(f"Nhiệt độ cao nhất: {max_temp:.2f} độ C, ngày thứ {max_day}")
print(f"Nhiệt độ thấp nhất: {min_temp:.2f} độ C, ngày thứ {min_day}")


temp_diff = temp_diff = [abs(temperatures[i] - temperatures[i - 1]) for i in range(1, len(temperatures))]
max_diff = np.max(temp_diff)
max_diff_day = np.argmax(temp_diff) + 1  

print(f"Sự chênh lệch nhiệt độ lớn nhất: {max_diff:.2f} độ C, giữa ngày {max_diff_day} và {max_diff_day + 1}")



days_above_20 = np.where(temperatures > 20)[0] + 1  
print(f"Những ngày có nhiệt độ trên 20 độ C: {days_above_20}")


selected_days = [5, 10, 15, 20, 25]
selected_temperatures = temperatures[np.array(selected_days) - 1]  
print(f"Nhiệt độ ngày 5, 10, 15, 20, 25: {selected_temperatures}")


above_avg_temps = temperatures[temperatures > average_temp]
print(f"Nhiệt độ các ngày trên trung bình: {above_avg_temps}")


even_days_temps = temperatures[1::2]  
odd_days_temps = temperatures[0::2]   

print(f"Nhiệt độ các ngày chẵn: {even_days_temps}")
print(f"Nhiệt độ các ngày lẻ: {odd_days_temps}")


file_path = 'C:/laptrinhaaa/python learn on class/Python learn ver3/1_on tap cuoi ky/lab2/data/efficiency.txt'
efficiency = np.loadtxt(file_path, dtype=int)


avg_efficiency = np.mean(efficiency)
print(f"Hiệu suất trung bình: {avg_efficiency:.2f}")


max_eff = np.max(efficiency)
min_eff = np.min(efficiency)
max_eff_day = np.argmax(efficiency) + 1
min_eff_day = np.argmin(efficiency) + 1

print(f"Hiệu suất cao nhất: {max_eff}, ngày thứ {max_eff_day}")
print(f"Hiệu suất thấp nhất: {min_eff}, ngày thứ {min_eff_day}")
