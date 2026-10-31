# To-Do List GUI App - Codtech Task 3
# Intern ID: CITS9867 | Name: Shaik Abdul Reshma

import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List - CITS9867")
        self.root.geometry("450x550")
        self.root.config(bg="#f0f4ff")
        
        # Title
        title = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#f0f4ff", fg="#2c3e50")
        title.pack(pady=15)

        # Input Frame
        input_frame = tk.Frame(root, bg="#f0f4ff")
        input_frame.pack(pady=10, padx=20, fill="x")

        self.entry = tk.Entry(input_frame, font=("Arial", 12), width=22, bd=2, relief="groove")
        self.entry.pack(side="left", fill="x", expand=True, padx=(0,10))
        self.entry.bind("<Return>", lambda e: self.add_task())

        add_btn = tk.Button(input_frame, text="Add", command=self.add_task, bg="#6c5ce7", fg="white", font=("Arial", 11, "bold"), bd=0, padx=15, pady=5)
        add_btn.pack(side="right")

        # Listbox Frame
        list_frame = tk.Frame(root)
        list_frame.pack(pady=10, padx=20, fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(list_frame, font=("Arial", 12), height=15, yscrollcommand=scrollbar.set, bd=2, relief="groove")
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.listbox.yview)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#f0f4ff")
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Done", command=self.mark_done, bg="#00b894", fg="white", font=("Arial", 10, "bold"), width=8, bd=0, pady=5).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_task, bg="#d63031", fg="white", font=("Arial", 10, "bold"), width=8, bd=0, pady=5).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Clear All", command=self.clear_all, bg="#636e72", fg="white", font=("Arial", 10, "bold"), width=8, bd=0, pady=5).pack(side="left", padx=5)

        self.load_tasks()

    def add_task(self):
        task = self.entry.get().strip()
        if task == "":
            messagebox.showwarning("Warning", "Please enter a task!")
            return
        self.listbox.insert("end", task)
        self.entry.delete(0, "end")
        self.save_tasks()

    def mark_done(self):
        try:
            selected = self.listbox.curselection()[0]
            task = self.listbox.get(selected)
            if not task.startswith("[DONE] "):
                self.listbox.delete(selected)
                self.listbox.insert(selected, f"[DONE] {task}")
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")

    def delete_task(self):
        try:
            self.listbox.delete(self.listbox.curselection())
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Delete all tasks?"):
            self.listbox.delete(0, "end")
            self.save_tasks()

    def save_tasks(self):
        tasks = list(self.listbox.get(0, "end"))
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f)

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, "r") as f:
                    tasks = json.load(f)
                    for task in tasks:
                        self.listbox.insert("end", task)
            except:
                pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
