import threading
import time

# Shared resource
counter = 0

# Bước 1: Chỉnh sửa phương thức run_task để tăng giá trị của shared resource (counter)
class SimpleTask:
    def __init__(self, name):
        self.name = name

    def run_task(self):
        global counter
        for _ in range(1000):  # Mỗi thread sẽ tăng counter 1000 lần
            counter += 1  # Không sử dụng lock, gây ra race condition

# Bước 2: Khởi tạo nhiều threads và chạy các task trong các thread riêng biệt
def main():
    # Khởi tạo danh sách các threads
    threads = []

    # Tạo và chạy nhiều đối tượng SimpleTask trong các thread
    for i in range(5):  # Tạo 5 threads
        task = SimpleTask(name=f"Thread-{i+1}")
        thread = threading.Thread(target=task.run_task)
        threads.append(thread)
        thread.start()

    # Đợi tất cả các threads hoàn thành
    for thread in threads:
        thread.join()

    # In kết quả cuối cùng của counter
    print(f"Final counter value: {counter}")

# Bước 3: Khởi chạy chương trình
if __name__ == "__main__":
    start_time = time.time()  # Lưu thời gian bắt đầu
    main()
    end_time = time.time()  # Lưu thời gian kết thúc
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
