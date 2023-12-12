import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class SignalProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Xử lý Tín hiệu số")

        # Tạo các biến và đối tượng cần thiết
        self.signal_data = np.array([])
        self.sample_rate = 1000

        # Tạo giao diện người dùng
        self.create_widgets()

    def create_widgets(self):
        # Tạo khung chứa các điều khiển
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Tạo các điều khiển và nút
        ttk.Label(control_frame, text="Tín hiệu mẫu:").grid(column=0, row=0, sticky=tk.W)
        ttk.Button(control_frame, text="Hiển thị Tín hiệu Mẫu", command=self.plot_sample_signal).grid(column=1, row=0, sticky=tk.W)

        # Thêm các chức năng mở rộng như thêm nút và điều khiển để thực hiện các phép biến đổi tín hiệu

    def plot_sample_signal(self):
        # Tạo dữ liệu mẫu, ví dụ: tín hiệu sin
        t = np.arange(0, 1, 1/self.sample_rate)
        self.signal_data = np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.normal(size=len(t))

        # Hiển thị tín hiệu bằng đồ thị
        self.plot_signal(self.signal_data, "Tín hiệu Mẫu")

    def plot_signal(self, data, title):
        # Tạo đồ thị
        fig, ax = plt.subplots()
        ax.plot(data)
        ax.set(title=title, xlabel='Thời gian', ylabel='Amplitude')

        # Hiển thị đồ thị trong giao diện tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(column=0, row=1, columnspan=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = SignalProcessingApp(root)
    root.mainloop()