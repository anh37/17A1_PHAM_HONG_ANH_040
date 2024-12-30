import threading
import time

# Bước 1: Chuyển đổi Class SimpleTask để chạy trong một thread
class SimpleTask:
    def __init__(self, name):
        self.name = name

    def run_task(self):
        # In dãy số từ 1 đến 10 (hoặc bất kỳ nhiệm vụ nào)
        for i in range(1, 11):
            print(f"Task {self.name} - Number: {i}")
            time.sleep(0.1)  # Giả lập một tác vụ mất thời gian (tạm dừng 0.1 giây)

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

    print("All tasks are completed.")

# Bước 3: Khởi chạy chương trình
if __name__ == "__main__":
    start_time = time.time()  # Lưu thời gian bắt đầu
    main()
    end_time = time.time()  # Lưu thời gian kết thúc
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
