# Bước 1: Khởi tạo class SimpleTask
class SimpleTask:
    def __init__(self):
        # Phương thức khởi tạo (constructor) của class
        pass
    
    # Bước 2: Phương thức để thực hiện nhiệm vụ
    def run_task(self):
        # In dãy số từ 1 đến 10
        for i in range(1, 11):
            print(i)

# Bước 3: Khởi tạo đối tượng và chạy phương thức
if __name__ == "__main__":
    # Tạo đối tượng từ class SimpleTask
    task = SimpleTask()
    
    # Gọi phương thức run_task để thực hiện nhiệm vụ
    task.run_task()
