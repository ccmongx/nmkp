import tkinter as tk
from tkinter import messagebox
import joblib

# Load mô hình đã được huấn luyện
def load_model():
    # Thực hiện việc load mô hình đã được huấn luyện từ file hoặc từ bộ nhớ
    # Trong ví dụ này, ta giả định mô hình đã được huấn luyện và lưu trong biến clf
    clf = joblib.load("decision_tree_model.pkl")
    # Đoạn này có thể thay đổi tùy theo cách bạn lưu và load mô hình

    return clf

# Dự đoán kết quả khi nhấn nút
def on_select(event):
    selected_option = []
    for i in range(9):
        selected_option.append(variables[i].get())
    print("Selected options:", selected_option)

# Hàm được gọi khi nút "Dự đoán" được nhấn
def predict():
    selected_options = []
    for var in variables:
        selected_option_name = var.get()
        selected_option_value = options_lists[variables.index(var)][selected_option_name]
        selected_options.append(selected_option_value)
    prediction = clf.predict([selected_options])
    result_str = ""
    if prediction[0] == 1:
        result_str = "Poisonous"
    else:
        result_str = "Edible"
    messagebox.showinfo("Prediction", f"This type of mushroom is: {result_str}")


# Tạo giao diện
root = tk.Tk()
root.title("Decision Tree Prediction")

# Tạo các ô nhập liệu cho 9 thuộc tính
title = ['veil-color','habitat', 'ring-type','cap-shape','spore-print-color','cap-color','gill-attachment','veil-type','gill-color', "gill-spacing", "cap-surface"]
options_lists = [
    {"orange": 0, "brown": 1, "purple": 2, "unknown": 3, "white": 4, "yellow": 5, "black": 6, "red": 7}, #veil color
    {"grasses": 0, "heaths": 1, "urban": 2, "woods": 3, "leaves": 4, "paths": 5, "waste": 6, "meadows": 7}, #habitat
    {"flaring": 0, "grooved": 1, "none": 2, "none'": 3, "unknown": 4, "zone": 5, "large": 6, "pendant": 7, "movable": 8, "evanescent": 9}, #ring-type
    {"sunken": 0, "others": 1, "flat": 2, "convex": 3, "knobbed": 4, "bell": 5, "spherical": 6, "conical": 7}, #cap-shape
    {"green": 0, "gray": 1, "yellow": 2, "orange": 3, "chocolate": 4, "brown": 5, "purple": 6, "unknown": 7, "white": 8, "black": 9, "buff": 10, "pink": 11}, 
    {"green": 0, "gray": 1, "orange": 2, "brown": 3, "purple": 4, "blue": 5, "white": 6, "yellow": 7, "pink": 8, "buff": 9, "black": 10, "red": 11, "cinnamon": 12}, #cap-color
    {"adnexed": 0, "sinuate": 1, "decurrent": 2, "unknown": 3, "none": 4, "adnexed": 5, "pores": 6, "free": 7}, #gill-attachment
    {"unknown": 0, "universial": 1, "partial": 2}, #veil-type
    {"green": 0, "gray": 1, "yellow": 2, "orange": 3, "brown": 4, "chocolate": 5, "purple": 6, "none": 7, "pink": 8, "white": 9, "black": 10, "buff": 11, "red": 12}, #gill-color
    {"distant": 0, "unknown": 1, "none": 2, "crowded": 3, "close": 4},
    {"smooth": 0, "grooves": 1, "shiny": 2, "fibrous": 3, "d": 4, "fibrous'": 5, "unknown": 6, "leathery": 7, "wrinkled": 8, "scaly": 9, "silky": 10, "sticky": 11, "fleshy": 12} #cap-surface
]

option_values = [{name: value for value, name in options.items()} for options in options_lists]
# Biến lưu trữ giá trị được chọn cho mỗi dropdown
variables = []

for i in range(11):
    options = list(options_lists[i].keys())
    variable = tk.StringVar(root)
    variable.set(options[0])  # Giá trị mặc định cho dropdown thứ i
    variables.append(variable)
    
    # Tạo nhãn
    label = tk.Label(root, text=f"{title[i]}:")
    label.grid(row=i, column=0, padx=5, pady=5, sticky='w')
    
    # Tạo dropdown list
    dropdown = tk.OptionMenu(root, variable, *options, command=on_select)
    dropdown.grid(row=i, column=1, padx=5, pady=5, sticky='w')

# Tải mô hình đã được huấn luyện
clf = load_model()

# Nút "Dự đoán"
predict_button = tk.Button(root, text="Dự đoán", command=predict)
predict_button.grid(row=11, columnspan=2, padx=5, pady=5)

# Khởi chạy giao diện
root.mainloop()