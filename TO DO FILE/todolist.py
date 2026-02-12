import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x500")
root.resizable(False, False)
tasks = []

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")
def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            tasks[selected_task_index] = new_task
            update_listbox()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter updated task!")
    except:
        messagebox.showwarning("Warning", "Please select a task to update!")
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index] = tasks[selected_task_index] + " ✔"
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task!")
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)
title_label = tk.Label(root, text="My To-Do List", font=("Arial", 18))
title_label.pack(pady=10)
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)
add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)
update_button = tk.Button(root, text="Update Task", width=15, command=update_task)
update_button.pack(pady=5)
delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)
complete_button = tk.Button(root, text="Mark Completed", width=15, command=mark_completed)
complete_button.pack(pady=5)
task_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
task_listbox.pack(pady=15)
root.mainloop()
