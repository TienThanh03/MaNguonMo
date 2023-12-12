import tkinter as tk
from PIL import Image, ImageTk

class HinhHocApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phần Mềm Hỗ Trợ Hình Học")

        self.canvas = tk.Canvas(root, width=500, height=400)
        self.canvas.pack()

        self.label_info = tk.Label(root, text="Chọn một hình học:")
        self.label_info.pack()

        self.btn_tam_giac = tk.Button(root, text="Tam Giác", command=self.draw_tam_giac)
        self.btn_tam_giac.pack(side=tk.LEFT, padx=10)

        self.btn_chu_nhat = tk.Button(root, text="Hình Chữ Nhật", command=self.draw_chu_nhat)
        self.btn_chu_nhat.pack(side=tk.LEFT, padx=10)

        self.btn_vuong = tk.Button(root, text="Hình Vuông", command=self.draw_vuong)
        self.btn_vuong.pack(side=tk.LEFT, padx=10)

        self.btn_tron = tk.Button(root, text="Hình Tròn", command=self.draw_tron)
        self.btn_tron.pack(side=tk.LEFT, padx=10)

        self.btn_xoa = tk.Button(root, text="Xóa Hình", command=self.clear_canvas)
        self.btn_xoa.pack(side=tk.LEFT, padx=10)

        self.image_label = tk.Label(root)
        self.image_label.pack()

    def draw_tam_giac(self):
        self.clear_canvas()
        self.draw_image("tam_giac.png")
        self.display_formula("Tam giác: A = 0.5 * b * h")

    def draw_chu_nhat(self):
        self.clear_canvas()
        self.draw_image("chu_nhat.png")
        self.display_formula("Hình chữ nhật: A = a * b, P = 2 * (a + b)")

    def draw_vuong(self):
        self.clear_canvas()
        self.draw_image("vuong.png")
        self.display_formula("Hình vuông: A = a^2, P = 4 * a")

    def draw_tron(self):
        self.clear_canvas()
        self.draw_image("tron.png")
        self.display_formula("Hình tròn: A = π * r^2, C = 2 * π * r")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image_label.config(image="")

    def draw_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((200, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.image_label.config(image=img)
        self.image_label.image = img

    def display_formula(self, formula):
        formula_label = tk.Label(self.root, text=formula)
        formula_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = HinhHocApp(root)
    root.mainloop()