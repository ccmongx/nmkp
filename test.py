import tkinter as tk

def submit_form():
    selected_answers = []
    for question, radio_buttons in zip(questions, answer_vars):
        for i, var in enumerate(radio_buttons):
            if var.get() == 1:
                selected_answers.append(f"{question}: {answers[i]}")
                break
    
    if selected_answers:
        info_label.config(text="Các đáp án đã chọn:\n" + "\n".join(selected_answers))
    else:
        info_label.config(text="Bạn chưa chọn đáp án nào.")

# Tạo cửa sổ
root = tk.Tk()
root.title("PHÂN LOẠI NẤM ĐỘC")

# Danh sách các câu hỏi và đáp án
questions = ["", "Câu hỏi 2", "Câu hỏi 3"]
answers = ["Đáp án 1", "Đáp án 2", "Đáp án 3"]

# Biến lưu trữ các radio button cho mỗi câu hỏi
answer_vars = []

# Tạo các radio button cho mỗi câu hỏi
for i, question in enumerate(questions):
    tk.Label(root, text=question).grid(row=i, column=0, sticky="w", padx=10, pady=5)
    vars_for_question = []
    for j, answer in enumerate(answers):
        var = tk.IntVar()
        radio_button = tk.Radiobutton(root, text=answer, variable=var, value=1)
        radio_button.grid(row=i, column=j+1, padx=10, pady=5, sticky="w")
        vars_for_question.append(var)
    answer_vars.append(vars_for_question)

# Tạo nút "Submit" để gửi dữ liệu
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=len(questions), column=0, columnspan=len(answers)+1, pady=10)

# Nhãn để hiển thị thông tin đã chọn
info_label = tk.Label(root, text="")
info_label.grid(row=len(questions) + 1, column=0, columnspan=len(answers)+1, pady=10)

root.mainloop()
