import pandas as pd
import tkinter as tk
from tkinter import ttk

def load_data():
    # Link GitHub chứa file CSV
    url = "https://raw.githubusercontent.com/your_username/your_repository/master/your_data.csv"

    # Đọc dữ liệu từ file CSV
    data = pd.read_csv(url)
    return data

def display_students():
    # Xóa dữ liệu cũ trên giao diện
    for row in tree.get_children():
        tree.delete(row)

    # Lấy dữ liệu mới từ file CSV
    data = load_data()

    # Hiển thị danh sách sinh viên trên cây (tree)
    for index, row in data.iterrows():
        tree.insert("", index, values=list(row))

def show_highest_score():
    max_score_student = data.loc[data['Điểm'].idxmax()]
    result_label.config(text=f"Sinh viên có điểm cao nhất: {max_score_student['Tên']} - {max_score_student['Điểm']} điểm")

def show_sorted_students():
    sorted_data = data.sort_values(by='Điểm')
    sorted_students_label.config(text=f"Danh sách sinh viên sắp xếp từ thấp đến cao: {sorted_data.to_string(index=False)}")

def show_grade_students(grade):
    grade_students = data[data['Điểm'] == grade]
    grade_students_label.config(text=f"Danh sách sinh viên có điểm {grade}: {grade_students.to_string(index=False)}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Báo cáo học phần")

# Tạo cây để hiển thị danh sách sinh viên
tree = ttk.Treeview(root, columns=('Tên', 'Điểm'))
tree.heading('#0', text='STT')
tree.heading('#1', text='Tên')
tree.heading('#2', text='Điểm')

# Tạo các nút chức năng
load_button = tk.Button(root, text="Tải dữ liệu", command=display_students)
highest_score_button = tk.Button(root, text="Sinh viên cao nhất", command=show_highest_score)
sorted_students_button = tk.Button(root, text="Sắp xếp điểm", command=show_sorted_students)

grade_students_button_A = tk.Button(root, text="Điểm A", command=lambda: show_grade_students('A'))
grade_students_button_B = tk.Button(root, text="Điểm B", command=lambda: show_grade_students('B'))
grade_students_button_C = tk.Button(root, text="Điểm C", command=lambda: show_grade_students('C'))
grade_students_button_D = tk.Button(root, text="Điểm D", command=lambda: show_grade_students('D'))

result_label = tk.Label(root, text="")
sorted_students_label = tk.Label(root, text="")
grade_students_label = tk.Label(root, text="")

# Đặt các phần tử lên giao diện
tree.pack(pady=10)
load_button.pack()
highest_score_button.pack()
sorted_students_button.pack()
grade_students_button_A.pack()
grade_students_button_B.pack()
grade_students_button_C.pack()
grade_students_button_D.pack()
result_label.pack(pady=10)
sorted_students_label.pack(pady=10)
grade_students_label.pack(pady=10)

# Chạy ứng dụng
root.mainloop()