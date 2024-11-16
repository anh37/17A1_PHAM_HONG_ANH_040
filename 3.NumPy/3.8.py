# import numpy as np


# with open('C:/laptrinhaaa/python learn on class/Python learn ver3/Btap/3.NumPy/heights.txt', 'r') as file:
#     heights =  [float(value.strip()) for line in file for value in line.split(',') if value.strip()]

# with open('C:/laptrinhaaa/python learn on class/Python learn ver3/Btap/3.NumPy/positions.txt', 'r') as file:
#     positions = [line.strip().split(',') for line in file if line.strip()]


# np_positions = np.array(positions)
# np_heights = np.array(heights)


# print("Bước 1 - Kiểu dữ liệu của np_positions:", np_positions.dtype)
# print("Bước 1 - Kiểu dữ liệu của np_heights:", np_heights.dtype)


# gk_heights = np_heights[np_positions == 'GK']
# if len(gk_heights) > 0:
#     chieu_cao_tb_gk = np.mean(gk_heights)
#     print("/nBước 2 - Chiều cao trung bình của GK:", chieu_cao_tb_gk)
# else:
#     print("/nBước 2 - Không có dữ liệu về GK.")


# non_gk_heights = np_heights[np_positions != 'GK']
# if len(non_gk_heights) > 0:
#     chieu_cao_tb_non_gk = np.mean(non_gk_heights)
#     print("/nBước 3 - Chiều cao trung bình của các vị trí khác (không phải GK):", chieu_cao_tb_non_gk)
# else:
#     print("/nBước 3 - Không có dữ liệu về các vị trí khác ngoài GK.")


# player_dtype = np.dtype([('position', 'U5'), ('height', 'float')])
# players = np.array(list(zip(np_positions, np_heights)), dtype=player_dtype)


# sorted_players = np.sort(players, order='height')
# print("/nBước 5 - Mảng players sau khi sắp xếp theo chiều cao:/n", sorted_players)


# max_height_player = sorted_players[-1]
# min_height_player = sorted_players[0]

# print("/nBước 5 - Vị trí có chiều cao cao nhất:", max_height_player['position'], "với chiều cao:", max_height_player['height'])
# print("Bước 5 - Vị trí có chiều cao thấp nhất:", min_height_player['position'], "với chiều cao:", min_height_player['height'])
import numpy as np

# Đọc dữ liệu chiều cao từ file heights.txt
with open('C:/laptrinhaaa/python learn on class/Python learn ver3/Btap/3.NumPy/heights.txt', 'r') as file:
    heights = [float(value.strip()) for line in file for value in line.split(',') if value.strip()]

# Đọc dữ liệu vị trí từ file positions.txt
with open('C:/laptrinhaaa/python learn on class/Python learn ver3/Btap/3.NumPy/positions.txt', 'r') as file:
    positions = [line.strip() for line in file if line.strip()]  # Đảm bảo là 1D danh sách các chuỗi

# Kiểm tra xem np_positions có phải là mảng 1D không
np_positions = np.array(positions)
np_heights = np.array(heights)

print("Bước 1 - Kiểu dữ liệu của np_positions:", np_positions.dtype)
print("Bước 1 - Kiểu dữ liệu của np_heights:", np_heights.dtype)

# Kiểm tra kích thước của np_positions và np_heights
print(f"Bước 2 - Kích thước của np_positions: {np_positions.shape}")
print(f"Bước 2 - Kích thước của np_heights: {np_heights.shape}")

# Đảm bảo rằng np_positions và np_heights có cùng kích thước
if np_positions.shape[0] != np_heights.shape[0]:
    print("Lỗi: Kích thước của np_positions và np_heights không khớp!")
else:
    # Tính chiều cao trung bình của GK
    gk_heights = np_heights[np_positions == 'GK']
    if len(gk_heights) > 0:
        chieu_cao_tb_gk = np.mean(gk_heights)
        print("\nBước 3 - Chiều cao trung bình của GK:", chieu_cao_tb_gk)
    else:
        print("\nBước 3 - Không có dữ liệu về GK.")

    # Tính chiều cao trung bình của các vị trí khác ngoài GK
    non_gk_heights = np_heights[np_positions != 'GK']
    if len(non_gk_heights) > 0:
        chieu_cao_tb_non_gk = np.mean(non_gk_heights)
        print("\nBước 4 - Chiều cao trung bình của các vị trí khác (không phải GK):", chieu_cao_tb_non_gk)
    else:
        print("\nBước 4 - Không có dữ liệu về các vị trí khác ngoài GK.")

    # Tạo một mảng numpy với dtype cho mỗi người chơi (vị trí và chiều cao)
    player_dtype = np.dtype([('position', 'U5'), ('height', 'float')])
    players = np.array(list(zip(np_positions, np_heights)), dtype=player_dtype)

    # Sắp xếp danh sách players theo chiều cao
    sorted_players = np.sort(players, order='height')
    print("\nBước 5 - Mảng players sau khi sắp xếp theo chiều cao:\n", sorted_players)

    # Vị trí có chiều cao cao nhất và thấp nhất
    max_height_player = sorted_players[-1]
    min_height_player = sorted_players[0]

    print("\nBước 6 - Vị trí có chiều cao cao nhất:", max_height_player['position'], "với chiều cao:", max_height_player['height'])
    print("Bước 6 - Vị trí có chiều cao thấp nhất:", min_height_player['position'], "với chiều cao:", min_height_player['height'])
