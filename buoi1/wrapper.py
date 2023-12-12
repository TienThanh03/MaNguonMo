# Bài 2: Thiết kế phần mềm hỗ trợ học tập môn giải tích
# - Tính đạo hàm phương trình bậc n  1 ẩn
# - Tính tích phân, xác định và không xác định cận
# - Tính giới hạn
import sympy as sp
import tkinter as tk
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)

def calculate_derivative(expression, variable):
    expr = parse_expr(expression)
    derivative = sp.diff(expr, variable)
    return derivative

def calculate_integral(expression, variable, lower_limit, upper_limit):
    expr = parse_expr(expression)
    integral = sp.integrate(expr, (variable, lower_limit, upper_limit))
    return integral

def calculate_limit(expression, variable, value):
    expr = parse_expr(expression)
    limit = sp.limit(expr, variable, value)
    return limit

def on_derivative():
    expression = entry_expression.get()
    variable = entry_variable.get()
    result = calculate_derivative(expression, variable)
    result_label.config(text="Đạo hàm: " + str(result))

def on_integral():
    expression = entry_expression.get()
    variable = entry_variable.get()
    lower_limit = entry_lower_limit.get()
    upper_limit = entry_upper_limit.get()
    result = calculate_integral(expression, variable, lower_limit, upper_limit)
    result_label.config(text="Tích phân: " + str(result))

def on_limit():
    expression = entry_expression.get()
    variable = entry_variable.get()
    value = entry_limit_value.get()
    result = calculate_limit(expression, variable, value)
    result_label.config(text="Giới hạn: " + str(result))

root = tk.Tk()
root.title("Phần mềm hỗ trợ học môn Giải tích")

label_expression = tk.Label(root, text="Nhập biểu thức f(x):")
label_expression.pack()

entry_expression = tk.Entry(root)
entry_expression.pack()

label_variable = tk.Label(root, text="Nhập biến:")
label_variable.pack()

entry_variable = tk.Entry(root)
entry_variable.pack()

button_derivative = tk.Button(root, text="Tính đạo hàm", command=on_derivative)
button_derivative.pack()

button_integral = tk.Button(root, text="Tính tích phân", command=on_integral)
button_integral.pack()

label_limits = tk.Label(root, text="Nhập giới hạn:")
label_limits.pack()

entry_lower_limit = tk.Entry(root)
entry_lower_limit.pack()

entry_upper_limit = tk.Entry(root)
entry_upper_limit.pack()

button_limit = tk.Button(root, text="Tính giới hạn", command=on_limit)
button_limit.pack()

label_limit_value = tk.Label(root, text="Nhập giá trị giới hạn:")
label_limit_value.pack()

entry_limit_value = tk.Entry(root)
entry_limit_value.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()





