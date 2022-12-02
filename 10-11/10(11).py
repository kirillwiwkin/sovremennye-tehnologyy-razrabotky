from tkinter import *
from tkinter import ttk, messagebox, filedialog as fd
from tkinter.ttk import Combobox
import requests


window = Tk()
window.title("Шишкин Кирилл Сергеевич")
window.geometry('700x700')

tab_control = ttk.Notebook(window)

# Калькулятор

tab_calc = ttk.Frame(tab_control)
tab_control.add(tab_calc, text="Калькулятор")
tab_control.pack(expand=True, fill='both')

entry1 = Entry(tab_calc, text="Первое число")
entry1.pack()


sign_combo = Combobox(tab_calc)
sign_combo['values'] = ["+", "-", "*", "/"]
sign_combo.current(0)
sign_combo.pack()

entry2 = Entry(tab_calc, text="Второе число")
entry2.pack()

def calc():
    global sum_text
    a = int(entry1.get())
    b = int(entry2.get())

    sign = sign_combo.get()

    if sign == "+":
        sum_text.set(a + b)
    if sign == "-":
        sum_text.set(a - b)
    if sign == "*":
        sum_text.set(a * b)
    if sign == "/":
        sum_text.set(a / b)              
calc_btn = Button(tab_calc, command=calc, text="Вычислить")
calc_btn.pack()

sum_text = StringVar()
entry_sum = Entry(tab_calc, textvariable=sum_text)
entry_sum.pack()

# Чекбоксы

tab_checkbox = ttk.Frame(tab_control)
tab_control.add(tab_checkbox, text="Чекбоксы")
tab_control.pack(expand=True, fill='both')

var = IntVar()
var.set(1)
rd1 = Radiobutton(tab_checkbox, text="Первый вариант", variable=var, value=1)
rd1.pack()
rd2 = Radiobutton(tab_checkbox, text="Второй вариант", variable=var, value=2)
rd2.pack()
rd3 = Radiobutton(tab_checkbox, text="Третий вариант", variable=var, value=3)
rd3.pack()

def rd_btn_click():
    messagebox.showinfo("Сообщение", f"Выбран вариант №{var.get()}")

rd_btn = Button(tab_checkbox, text="Сообщение", command=rd_btn_click)
rd_btn.pack()

# Текст

tab_text = ttk.Frame(tab_control)
tab_control.add(tab_text, text="Текст")
tab_control.pack(expand=True, fill='both')


def file_upload_clicked():
    global text_data
    filename = fd.askopenfilename()
    text_data.delete(1.0, END)
    with open(filename, "r") as f:
        text_data.insert(END, f.read())

menu = Menu(window)
window.config(menu=menu)
file_upload = Menu(menu)
file_upload.add_command(label='Открыть', command=file_upload_clicked)
menu.add_cascade(label='Файл', menu=file_upload)

text_data = Text(tab_text)
text_data.pack()

# Github

tab_github = ttk.Frame(tab_control)
tab_control.add(tab_github, text="Github")
tab_control.pack(expand=True, fill='both')

label = ttk.Label(tab_github, text="Вводить в формате автор/репозиторий\nНапример: kubernetes/kubernetes")
label.pack()

repo_name_entry = Entry(tab_github, text="Название репозитория")
repo_name_entry.pack()

def load_info():
    url = f"https://api.github.com/repos/{repo_name_entry.get()}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        keys = ['company', 'created_at', 'email', 'id', 'name', 'url']
        filtered_data = {k: data[k] if k in data else None for k in keys}

        with open("filtered_data.txt", "w") as f:
            f.write(str(filtered_data))

        messagebox.showinfo("Успешно", "Информация загружена")
    else:
        messagebox.showerror("Ошибка", f"Ошибка при загрузке информации: {response.reason}")

load_info_btn = ttk.Button(tab_github, command=load_info, text="Загрузить информацию")
load_info_btn.pack()

window.mainloop()
