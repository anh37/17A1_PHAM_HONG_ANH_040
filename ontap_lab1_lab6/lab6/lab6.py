import tkinter as tk
from tkinter import messagebox
import sqlite3

# Kết nối với cơ sở dữ liệu SQLite
conn = sqlite3.connect('lab6/products.db')
c = conn.cursor()

# Tạo bảng sản phẩm nếu chưa có
c.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
''')
conn.commit()

# Hàm để thêm sản phẩm
def add_product():
    name = entry_name.get()
    price = entry_price.get()
    
    if not name or not price:
        messagebox.showwarning("Input Error", "Please fill in all fields")
        return
    
    c.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, float(price)))
    conn.commit()
    
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    load_products()

# Hàm để xóa sản phẩm
def delete_product():
    try:
        selected_product = listbox.curselection()
        if not selected_product:
            messagebox.showwarning("Selection Error", "Please select a product to delete")
            return
        product_id = listbox.get(selected_product[0]).split(' ')[0]
        c.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        load_products()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Hàm để cập nhật sản phẩm
def update_product():
    try:
        selected_product = listbox.curselection()
        if not selected_product:
            messagebox.showwarning("Selection Error", "Please select a product to update")
            return
        
        product_id = listbox.get(selected_product[0]).split(' ')[0]
        new_name = entry_name.get()
        new_price = entry_price.get()
        
        if not new_name or not new_price:
            messagebox.showwarning("Input Error", "Please fill in all fields")
            return
        
        c.execute("UPDATE products SET name = ?, price = ? WHERE id = ?", (new_name, float(new_price), product_id))
        conn.commit()
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        load_products()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Hàm để tải danh sách sản phẩm từ cơ sở dữ liệu
def load_products():
    listbox.delete(0, tk.END)
    c.execute("SELECT * FROM products")
    for product in c.fetchall():
        listbox.insert(tk.END, f"{product[0]} {product[1]} - ${product[2]:.2f}")

# Cấu hình giao diện người dùng
root = tk.Tk()
root.title("Product Management")

# Labels và Entry widgets
label_name = tk.Label(root, text="Product Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_price = tk.Label(root, text="Product Price:")
label_price.pack()

entry_price = tk.Entry(root)
entry_price.pack()

# Listbox để hiển thị sản phẩm
listbox = tk.Listbox(root, height=10, width=50)
listbox.pack()

# Nút để thêm, xóa, cập nhật sản phẩm
btn_add = tk.Button(root, text="Add Product", command=add_product)
btn_add.pack()

btn_update = tk.Button(root, text="Update Product", command=update_product)
btn_update.pack()

btn_delete = tk.Button(root, text="Delete Product", command=delete_product)
btn_delete.pack()

# Tải danh sách sản phẩm ban đầu
load_products()

# Chạy ứng dụng
root.mainloop()

# Đóng kết nối cơ sở dữ liệu khi thoát
conn.close()
