import tkinter as tk  # Importe la bibliothèque tkinter sous le nom de tk.
from tkinter import ttk  # Importe le module ttk de tkinter pour les widgets de thème.
from tkinter import simpledialog  # Importe simpledialog pour afficher des boîtes de dialogue simples.
from tkinter import messagebox  # Importe messagebox pour afficher des boîtes de message.

from src.task_manager import TaskManager  # Importe la classe TaskManager du module src.task_manager.
from src.task import Task  # Importe la classe Task du module src.task.
from src.category import Category  # Importe la classe Category du module src.category.

class TaskManagerApp:
    def __init__(self, root):
        self.root = root  # Initialise la fenêtre principale de l'application.
        self.task_manager = TaskManager()  # Initialise un gestionnaire de tâches.
        self.current_category = None  # Initialise la catégorie actuellement sélectionnée.
        self.setup_ui()  # Configure l'interface utilisateur de l'application.

    def setup_ui(self):
        self.root.title("Task Manager")  # Définit le titre de la fenêtre principale.

        # Crée des widgets Entry pour la description, la date limite et la priorité des tâches.
        self.description_entry = tk.Entry(self.root, width=30)
        self.description_entry.grid(row=0, column=1, padx=10, pady=5)
        self.deadline_entry = tk.Entry(self.root, width=15)
        self.deadline_entry.grid(row=0, column=3, padx=10, pady=5)
        self.priority_entry = tk.Entry(self.root, width=5)
        self.priority_entry.grid(row=0, column=5, padx=10, pady=5)

        # Crée des étiquettes pour les champs de saisie.
        tk.Label(self.root, text="Description").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Deadline").grid(row=0, column=2, padx=10, pady=5)
        tk.Label(self.root, text="Priority").grid(row=0, column=4, padx=10, pady=5)

        # Crée des boutons pour ajouter, supprimer et mettre à jour les tâches et les catégories.
        tk.Button(self.root, text="Add Task", command=self.add_task).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(self.root, text="Delete Task", command=self.delete_task).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.root, text="Update Task", command=self.update_task).grid(row=1, column=2, padx=10, pady=5)
        tk.Button(self.root, text="Add Category", command=self.add_category).grid(row=1, column=3, padx=10, pady=5)
        tk.Button(self.root, text="Delete Category", command=self.delete_category).grid(row=1, column=4, padx=10, pady=5)

        # Crée une liste pour afficher les tâches.
        self.tasks_listbox = tk.Listbox(self.root, width=50)
        self.tasks_listbox.grid(row=2, column=0, columnspan=6, padx=10, pady=5)

        # Crée un Treeview pour afficher les catégories et les sous-catégories.
        self.category_tree = ttk.Treeview(self.root)
        self.category_tree.heading("#0", text="Categories")
        self.category_tree.grid(row=3, column=0, columnspan=6, padx=10, pady=5)
        self.category_tree.bind("<<Treeview Select>>", self.on_category_select)

        self.update_tasks_listbox()
        self.update_category_tree()

    # Méthodes pour ajouter, supprimer et mettre à jour les tâches et les catégories.
    def add_task(self):
        # Récupère la description, la date limite et la priorité de la tâche.
        description = self.description_entry.get()
        deadline = self.deadline_entry.get()
        priority = self.priority_entry.get()
        if description and deadline and priority:
            # Ajoute une nouvelle tâche au gestionnaire de tâches.
            self.task_manager.add_task(Task(description, deadline, priority))
            self.update_tasks_listbox()
        else:
            # Affiche un avertissement si tous les champs ne sont pas remplis.
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def delete_task(self):
        # Supprime la tâche sélectionnée de la liste des tâches.
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            task = self.task_manager.tasks[selected_index[0]]
            self.task_manager.remove_task(task)
            self.update_tasks_listbox()

    def update_task(self):
        # Met à jour la tâche sélectionnée avec de nouvelles informations.
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

    def on_category_select(self, event):
        # Met à jour la liste des tâches en fonction de la catégorie sélectionnée.
        selected_item = self.category_tree.focus()
        if selected_item:
            self.current_category = self.category_tree.item(selected_item)['values'][0]
            self.update_tasks_listbox()

    def add_category(self):
        # Ajoute une nouvelle catégorie ou sous-catégorie.
        new_category_name = tk.simpledialog.askstring("New Category", "Enter the name of the new category:")
        if new_category_name:
            new_category = Category(new_category_name)
            if self.current_category:
                parent_category = self.task_manager.get_category(self.current_category)
                parent_category.add_subcategory(new_category)
            else:
                self.task_manager.add_category(new_category)
            self.update_category_tree()

    def delete_category(self):
        # Supprime une catégorie ou une sous-catégorie.
        if not self.current_category:
            messagebox.showerror("Error", "No category selected")
            return
        if messagebox.askyesno("Delete Category", f"Are you sure you want to delete the category '{self.current_category}'?"):
            self.task_manager.remove_category(self.current_category)
            self.current_category = None
            self.update_category_tree()
            self.update_tasks_listbox()

    def update_tasks_listbox(self):
        # Met à jour la liste des tâches en fonction de la catégorie sélectionnée.
        self.tasks_listbox.delete(0, tk.END)
        if self.current_category:
            tasks = self.task_manager.get_tasks_by_category(self.current_category)
        else:
            tasks = self.task_manager.tasks
        for task in tasks:
            self.tasks_listbox.insert(tk.END, f"{task.description} - {task.deadline} - {task.priority}")

    def update_category_tree(self):
        # Met à jour l'arborescence des catégories et sous-catégories.
        self.category_tree.delete(*self.category_tree.get_children())
        root_category = self.task_manager.get_root_category()
        if root_category:
            self.category_tree.insert("", tk.END, text=root_category.name, values=[root_category.name])
            self._populate_subcategories(root_category)
        else :
            for cat in self.task_manager.categories:
                self.category_tree.insert("", tk.END, text=cat.name, values=[cat.name])
                self._populate_subcategories(cat)
                

    def _populate_subcategories(self, category):
        # Fonction récursive pour ajouter les sous-catégories à l'arborescence.
        for subcategory in category.subcategories:
            self.category_tree.insert(category.name, tk.END, text=subcategory.name, values=[subcategory.name])
            self._populate_subcategories(subcategory)

    def run(self):
        # Lance la boucle principale de l'application.
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    app.run()

""" Ce code crée une application Tkinter pour gérer des tâches et des catégories de tâches. 
    Il utilise des widgets Entry pour saisir les détails des tâches, des boutons pour ajouter, 
    supprimer et mettre à jour les tâches et les catégories, une liste pour afficher les tâches, 
    et un Treeview pour afficher les catégories et les sous-catégories. L'application utilise également 
    des boîtes de dialogue simples pour afficher des avertissements et des messages.
"""