import tkinter as tk

def add_task():
    task = task_entry1.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry1.delete(0, tk.END)

def add_task1():
    task = task_entry1.get()
    if task:
        task_listbox1.insert(tk.END, task)
        task_entry1.delete(0, tk.END)

def delete_task():
    selected_hard_skill = task_listbox.curselection()
    selected_soft_skill = task_listbox1.curselection()
    if selected_hard_skill:
        task_listbox.delete(selected_hard_skill)
    elif selected_soft_skill:
        task_listbox1.delete(selected_soft_skill)

root = tk.Tk()
root.title("Skills")
root.configure(background="snow3")

text1 = tk.Label(root, text="Введите навык:", bg="DarkSeaGreen1")
text1.grid(row=1, column=5)

task_entry1 = tk.Entry(root, width=40, bg="cornsilk1")
task_entry1.grid(row=2, column=5)

add_task_button = tk.Button(root, text="Hard skills",bg="firebrick1",command=add_task)
add_task_button.grid(row=9, column=2)

delete_button = tk.Button(root, text="Удалить выбор",bg="seashell4", command=delete_task)
delete_button.grid(row=10, column=5)

add_task1_button = tk.Button(root, text="Soft skills",bg="DodgerBlue2", command=add_task1)
add_task1_button.grid(row=9, column=6)

task_listbox = tk.Listbox(root,height=10, width=40, bg="white")
task_listbox.grid(row=10, column=2)

task_listbox1 = tk.Listbox(root,height=10, width=40, bg="white")
task_listbox1.grid(row=10, column=6)

root.mainloop()