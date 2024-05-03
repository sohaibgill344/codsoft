#to do list
import tkinter as tk
from tkinter import simpledialog, messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        master.title("Todo List")
        self.to_do_list = []

        self.task_label = tk.Label(master, text="Task:")
        self.task_label.grid(row=0, column=0, sticky="w")
        self.task_entry = tk.Entry(master)
        self.task_entry.grid(row=0, column=1, sticky="ew")

        self.description_label = tk.Label(master, text="Description:")
        self.description_label.grid(row=1, column=0, sticky="w")
        self.description_entry = tk.Entry(master)
        self.description_entry.grid(row=1, column=1, sticky="ew")

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.view_button = tk.Button(master, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.mark_button = tk.Button(master, text="Mark Task as Completed", command=self.mark_as_completed_dialog)
        self.mark_button.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        self.task_text = tk.Text(master, height=10, width=50)
        self.task_text.grid(row=7, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        description = self.description_entry.get()
        if task:
            self.to_do_list.append({"task": task, "description": description})
            self.task_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
            messagebox.showinfo("Task Added", f"Task '{task}' has been added successfully.\nDescription: {description}")

    def view_tasks(self):
        self.task_text.delete(1.0, tk.END)
        if not self.to_do_list:
            self.task_text.insert(tk.END, "No tasks to view")
        else:
            for index, task_info in enumerate(self.to_do_list, start=1):
                task = task_info["task"]
                description = task_info["description"]
                self.task_text.insert(tk.END, f"{index}. Task: {task}\n   Description: {description}\n\n")

    def mark_as_completed_dialog(self):
        try:
            index = int(simpledialog.askstring("Mark Task as Completed", "Enter the index of the task to mark as completed:"))
            if index is not None:
                self.mark_as_completed(index - 1)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid index.")

    def mark_as_completed(self, index):
        if 0 <= index < len(self.to_do_list):
            self.to_do_list[index]["task"] += " (completed)"
            messagebox.showinfo("Task Marked as Completed", "Task marked as completed successfully.")
        else:
            messagebox.showerror("Invalid Index", "Invalid index provided.")

    def delete_task(self):
        try:
            index = int(simpledialog.askstring("Delete Task", "Enter the index of the task to delete:"))
            if index is not None:
                self.delete_task_at_index(index - 1)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid index.")

    def delete_task_at_index(self, index):
        if 0 <= index < len(self.to_do_list):
            del self.to_do_list[index]
            messagebox.showinfo("Task Deleted", "Task deleted successfully.")
        else:
            messagebox.showerror("Invalid Index", "Invalid index provided.")

root = tk.Tk()
app = TodoListApp(root)
root.mainloop()


