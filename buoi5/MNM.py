# tạo giao diện chọn các chức năng và thêm làm mờ và cắt góc trên của ảnh và lưu ảnh 
# import cv2
# import numpy as np

# img= cv2.imread('pic2.jpeg')
# cv2.imshow('Original',img)

# #generating the kernels
# kernel1= np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
# kernel2= np.array([[1,1,1],[1,-7,1],[1,1,1]])
# kernel3= np.array([[-1,-1,-1,-1,-1],
#                   [-1,2,2,2,-1],
#                   [-1,2,8,2,-1],
#                   [-1,2,2,2,-1],
#                   [-1,-1,-1,-1,-1]])  /8.0

# #applying different kernels to the input image
# out1= cv2.filter2D(img, -1 , kernel1)
# out2= cv2.filter2D(img, -1 , kernel2)
# out3= cv2.filter2D(img, -1 , kernel3)
# cv2.imshow("Sharpenning ",out1)          # làm sắc nét
# cv2.imshow('Excessive sharpening',out2)  # làm sắc nét quá mức
# cv2.imshow('Edge Enhancement',out3)      # tạo đường biên
# cv2.waitKey(0)
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Khởi tạo các kernel cho các tính năng
kernel1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
kernel2 = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
kernel3 = np.array([[-1, -1, -1, -1, -1],
                    [-1, 2, 2, 2, -1],
                    [-1, 2, 8, 2, -1],
                    [-1, 2, 2, 2, -1],
                    [-1, -1, -1, -1, -1]]) / 8.0
# Hàm xử lý khi nhấn nút Lưu ảnh

# Hàm xử lý khi nhấn nút Làm sắc nét
def sharpen_image():
    global img
    out = cv2.filter2D(img, -1, kernel1)
    cv2.imshow("Sharpened Image", out)
    save_button = tk.Button(root, text="Save sharpen_image", command=lambda: save_image(out))
    save_button.pack()
# Hàm xử lý khi nhấn nút Làm mờ
def blur_image():
    global img
    blurred = cv2.blur(img, (15, 15))
    cv2.imshow('Blurred Image', blurred)
    save_button = tk.Button(root, text="Save blurred Image", command=lambda: save_image(blurred))
    save_button.pack()
# Hàm xử lý khi nhấn nút Cắt ảnh
def crop_image():
    global img
    x, y, w, h = 100, 100, 300, 200
    cropped_img = img[y:y+h, x:x+w]
    cv2.imshow('Cropped Image', cropped_img)
    save_button = tk.Button(root, text="Save cropped_img", command=lambda: save_image(cropped_img))
    save_button.pack()
# Hàm xử lý khi nhấn nút Excessive Sharpening
def Excessive_sharpening():
    global img
    out2 = cv2.filter2D(img, -1, kernel2)
    cv2.imshow('Excessive sharpening', out2)
    save_button = tk.Button(root, text="Save Excessive_sharpening Image", command=lambda: save_image(out2))
    save_button.pack()
# Hàm xử lý khi nhấn nút Edge Enhancement
def Edge_Enhancement():
    global img
    out3 = cv2.filter2D(img, -1, kernel3)
    cv2.imshow('Edge Enhancement', out3)
    save_button = tk.Button(root, text="Save Edge_Enhancement Image", command=lambda: save_image(out3))
    save_button.pack()
#Xám
def grayscale_image():
    global img
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray_img)
    save_button = tk.Button(root, text="Save Image", command=lambda: save_image(gray_img))
    save_button.pack()
save_button = None
def save_image(img_to_save):
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))
    if save_path:
        cv2.imwrite(save_path, img_to_save)
        print("Đã lưu ảnh thành công.")
def open_image():
    global img
    file_path = filedialog.askopenfilename()

    if file_path:
        try:
            img = cv2.imread(file_path)
            if img is not None:
                cv2.imshow('Original', img)

                # Xóa nút "Open Image"
                open_button.destroy()

                # Hiển thị các nút chức năng sau khi ảnh đã được chọn
                sharpen_button.pack()
                blur_button.pack()
                crop_button.pack()
                Excessive_sharpening_button.pack()
                Edge_Enhancement_button.pack()
                grayscale_button.pack()
                

            else:
                raise ValueError("Không thể mở ảnh.")

        except (IOError, SyntaxError) as e:
            print("File không hợp lệ:", e)

# Tạo cửa sổ và nút mở ảnh
root = tk.Tk()
root.title("OpenCV Functions")

open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

# Tạo các nút chức năng, nhưng ẩn đi ban đầu
sharpen_button = tk.Button(root, text="Sharpen Image", command=sharpen_image)
blur_button = tk.Button(root, text="Blur Image", command=blur_image)
crop_button = tk.Button(root, text="Crop Image", command=crop_image)
Excessive_sharpening_button = tk.Button(root, text="Excessive Sharpening", command=Excessive_sharpening)
Edge_Enhancement_button = tk.Button(root, text="Edge Enhancement", command=Edge_Enhancement)
grayscale_button = tk.Button(root, text="Grayscale Image", command=grayscale_image)


# Hiển thị cửa sổ
root.mainloop()
