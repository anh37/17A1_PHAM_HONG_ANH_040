import numpy as np
import csv

# 1. Đọc dữ liệu từ file CSV
file_path = 'C:/laptrinhaaa/python learn on class/Python learn ver3/1_on tap cuoi ky/lab2/data/diem_hoc_phan.csv'
data = []

with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Bỏ qua header
    for row in reader:
        data.append([row[0], row[1]] + list(map(float, row[2:])))

# Chuyển dữ liệu thành mảng NumPy
data_array = np.array(data, dtype=object)

# 2. Quy đổi điểm số sang điểm chữ
def convert_to_letter_grade(score):
    if 8.5 <= score <= 10:
        return 'A'
    elif 8.0 <= score < 8.5:
        return 'B+'
    elif 7.0 <= score < 8.0:
        return 'B'
    elif 6.5 <= score < 7.0:
        return 'C+'
    elif 5.5 <= score < 6.5:
        return 'C'
    elif 5.0 <= score < 5.5:
        return 'D+'
    elif 4.0 <= score < 5.0:
        return 'D'
    else:
        return 'F'

# Áp dụng quy đổi điểm chữ
letter_grades = np.vectorize(convert_to_letter_grade)
grades_array = letter_grades(data_array[:, 2:].astype(float))

# 3. Chia tách dữ liệu theo học phần
hp1 = data_array[:, 2].astype(float)
hp2 = data_array[:, 3].astype(float)
hp3 = data_array[:, 4].astype(float)

# 4. Phân tích dữ liệu từng học phần
def analyze_subject(subject_scores, subject_name):
    total = np.sum(subject_scores)
    average = np.mean(subject_scores)
    std_dev = np.std(subject_scores)
    print(f"Học phần {subject_name}:\n  Tổng điểm: {total}\n  Điểm trung bình: {average:.2f}\n  Độ lệch chuẩn: {std_dev:.2f}\n")

print("Phân tích từng học phần:\n")
analyze_subject(hp1, "HP1")
analyze_subject(hp2, "HP2")
analyze_subject(hp3, "HP3")

# 5. Phân tích điểm tổng hợp
def analyze_letter_grades(grades):
    unique, counts = np.unique(grades, return_counts=True)
    grade_distribution = dict(zip(unique, counts))
    print("Phân bố điểm chữ:")
    for grade, count in grade_distribution.items():
        print(f"  {grade}: {count} sinh viên")

all_grades = grades_array.flatten()
print("Phân tích điểm tổng hợp:\n")
analyze_letter_grades(all_grades)

# Fancy Indexing - Lấy điểm các sinh viên theo một số điều kiện
print("\nĐiểm các sinh viên có điểm HP1 trên trung bình:")
print(data_array[hp1 > np.mean(hp1)])

print("\nĐiểm các sinh viên có điểm HP2 dưới 5:")
print(data_array[hp2 < 5])
