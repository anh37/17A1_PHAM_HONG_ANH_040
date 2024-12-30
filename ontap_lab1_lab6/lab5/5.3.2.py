import threading
import time

# Khởi tạo shared resource và lock
counter = 0
counter_lock = threading.Lock()

# Class SimpleTask với phương thức run_task
class SimpleTask:
    def run_task(self):
        global counter
        for _ in range(3):
            time.sleep(2)  # Giả lập một tác vụ mất thời gian
            with counter_lock:  # Sử dụng lock để bảo vệ shared resource
                counter += 1
                print(f"Counter đã tăng lên: {counter}")

# Hàm main để khởi tạo và chạy các threads
def main():
    # Tạo danh sách các threads
    tasks = [threading.Thread(target=SimpleTask().run_task) for _ in range(4)]

    # Khởi chạy tất cả các threads
    for task in tasks:
        task.start()

    # Đợi tất cả các threads hoàn thành
    for task in tasks:
        task.join()

# Chạy chương trình
if __name__ == "__main__":
    main()
