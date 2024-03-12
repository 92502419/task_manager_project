import tkinter as tk
from tkinter import messagebox
from src.task_manager import TaskManager
from src.task import Task
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.task_manager = TaskManager()
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Task Manager")

        # Entry widgets
        self.description_entry = tk.Entry(self.root, width=30)
        self.description_entry.grid(row=0, column=1, padx=10, pady=5)
        self.deadline_entry = tk.Entry(self.root, width=15)
        self.deadline_entry.grid(row=0, column=3, padx=10, pady=5)
        self.priority_entry = tk.Entry(self.root, width=5)
        self.priority_entry.grid(row=0, column=5, padx=10, pady=5)

        # Labels
        tk.Label(self.root, text="Description").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Deadline").grid(row=0, column=2, padx=10, pady=5)
        tk.Label(self.root, text="Priority").grid(row=0, column=4, padx=10, pady=5)

        # Buttons
        tk.Button(self.root, text="Add Task", command=self.add_task).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(self.root, text="Delete Task", command=self.delete_task).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Update Task", command=self.update_task).grid(row=1, column=2, padx=10, pady=5)
        tk.Button(self.root, text="Add Category", command=self.add_category).grid(row=1, column=3, padx=10, pady=5)
        tk.Button(self.root, text="Delete Category", command=self.delete_category).grid(row=1, column=4, padx=10, pady=5)

        # Listbox
        self.tasks_listbox = tk.Listbox(self.root, width=50)
        self.tasks_listbox.grid(row=2, column=0, columnspan=6, padx=10, pady=5)

        self.update_tasks_listbox()

    def add_task(self):
        description = self.description_entry.get()
        deadline = self.deadline_entry.get()
        priority = self.priority_entry.get()
        if description and deadline and priority:
            self.task_manager.add_task(Task(description, deadline, priority))
            self.update_tasks_listbox()
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            task = self.task_manager.tasks[selected_index[0]]
            self.task_manager.remove_task(task)
            self.update_tasks_listbox()

    def update_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            description = self.description_entry.get()
            deadline = self.deadline_entry.get()
            priority = self.priority_entry.get()
            if description and deadline and priority:
                new_task = Task(description, deadline, priority)
                old_task = self.task_manager.tasks[selected_index[0]]
                self.task_manager.update_task(old_task, new_task)
                self.update_tasks_listbox()
            else:
                messagebox.showwarning("Warning", "Please fill in all fields.")

    def add_category(self):
        pass  # Add logic for adding categories

    def delete_category(self):
        pass  # Add logic for deleting categories

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.task_manager.tasks:
            self.tasks_listbox.insert(tk.END, f"{task.description} - {task.deadline} - {task.priority}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    app.run()
