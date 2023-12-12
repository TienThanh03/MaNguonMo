import tkinter as tk
from tkinter import messagebox
import numpy as np

def solve_equations():
    mangA = []
    mangB = []
    
    # Lấy các giá trị từ các ô nhập liệu và xây dựng ma trận hệ số và vector hằng số
    for i in range(soPhuongTrinh):
        mangC = []
        for j in range(soAn):
            mangC.append(float(oNhapBien[i][j].get()))
        mangA.append(mangC)
        mangB.append(float(oNhapHangSo[i].get()))
    
    # Giải hệ phương trình sử dụng NumPy
    giaTriBien = np.array(mangA)
    giaTriHang = np.array(mangB)
    
    # Kiểm tra xem số phương trình và số ẩn có khớp nhau không
    try:
        if len(mangA) == len(mangA[0]) == len(mangB):
            ketQua = np.linalg.solve(giaTriBien, giaTriHang)
            # Hiển thị kết quả
            hienThiKetQua = "Kết quả:\n"
            for i in range(len(ketQua)):
                hienThiKetQua += f"Biến {i+1}: {ketQua[i]}\n"
            result_label.config(text=hienThiKetQua)
        else:
            result_label.config(text="Lỗi: Số phương trình và số ẩn không khớp")
    except:
        messagebox.showerror("Xay ra loi vui long thu lai!")
def nhapDuLieu():
    global soPhuongTrinh, soAn
    soPhuongTrinh = int(entry_phuong_trinh.get())
    soAn = int(entry_an.get())
    
    # Xóa các widget cũ nếu có
    for row in range(len(oNhapBien)):
        for entry in oNhapBien[row]:
            entry.destroy()
        oNhapHangSo[row].destroy()
    
    # Xóa nội dung label kết quả
    result_label.config(text="")
    
    # Tạo lại các ô nhập liệu dựa trên số phương trình và số ẩn mới
    oNhapBien.clear()
    oNhapHangSo.clear()
    for i in range(soPhuongTrinh):
        row = []
        for j in range(soAn):
            entry = tk.Entry(root)
            entry.grid(row=i, column=j)
            row.append(entry)
        oNhapBien.append(row)
        
        entry = tk.Entry(root)
        entry.grid(row=i, column=soAn)
        oNhapHangSo.append(entry)
        tk.Label(root, text='=').grid(row=i, column=soAn+1)
        
# Tạo giao diện
root = tk.Tk()
root.title("Giải hệ phương trình tuyến tính")

# Nhập số lượng phương trình và số ẩn từ người dùng
tk.Label(root, text="Nhập số phương trình: ").grid(row=0, column=0)
entry_phuong_trinh = tk.Entry(root)
entry_phuong_trinh.grid(row=0, column=1)

tk.Label(root, text="Nhập số ẩn: ").grid(row=1, column=0)
entry_an = tk.Entry(root)
entry_an.grid(row=1, column=1)

# Nút tạo ô nhập liệu dựa trên số phương trình và số ẩn nhập vào
create_button = tk.Button(root, text="Tạo ô nhập liệu", command=nhapDuLieu)
create_button.grid(row=2, columnspan=2)

# Nút giải phương trình
solve_button = tk.Button(root, text="Giải", command=solve_equations)
solve_button.grid(row=3, columnspan=2)

# Label để hiển thị kết quả
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

oNhapBien = []
oNhapHangSo = []
soPhuongTrinh = 0
soAn = 0

root.mainloop()
