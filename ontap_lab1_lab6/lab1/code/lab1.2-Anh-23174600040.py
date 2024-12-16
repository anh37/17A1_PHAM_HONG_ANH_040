import json

# Đường dẫn đến tập tin JSON
file_path = 'data/users.json'

# Đọc tập tin JSON
def read_json(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)  # Parse nội dung JSON
        return data

# Hiển thị dữ liệu từ tập tin JSON
def display_data(data):
    if data:
        print("Thông tin trong tập tin JSON:")
        for entry in data:
            name = entry.get("name", "Không xác định")
            age = entry.get("age", "Không xác định")
            address = entry.get("address", "Không xác định")
            print(f"Tên: {name}, Tuổi: {age}, Địa chỉ: {address}")

# Sử dụng hàm
json_data = read_json(file_path)
display_data(json_data)
