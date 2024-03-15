import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.task_manager import TaskManager
from src.task import Task
from src.category import Category
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.task_manager = TaskManager()
        self.current_category = None  # Track the current selected category
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
        
        # Treeview for displaying categories and subcategories
        self.category_tree = ttk.Treeview(self.root)
        self.category_tree.heading("#0", text="Categories")
        self.category_tree.grid(row=3, column=0, columnspan=6, padx=10, pady=5)
        self.category_tree.bind("<<Treeview Select>>", self.on_category_select)
        
        self.update_tasks_listbox()
        self.update_category_tree()

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
                
    def on_category_select(self, event):
        # Récupérer la catégorie sélectionnée
        selected_item = self.category_tree.focus()
        if selected_item:
            self.current_category = self.category_tree.item(selected_item)['values'][0]
            self.update_tasks_listbox()            

    def add_category(self):
        # Demander le nom de la nouvelle catégorie
        new_category_name = tk.simpledialog.askstring("Nouvelle Catégorie", "Entrez le nom de la nouvelle catégorie :")
        if new_category_name:
            # Créer une nouvelle instance de Catégorie
            new_category = Category(new_category_name)

            # Si une catégorie est sélectionnée, l'ajouter comme sous-catégorie
            if self.current_category:
                parent_category = self.task_manager.get_category(self.current_category)
                parent_category.add_subcategory(new_category)
            else:
                # Sinon, l'ajouter comme catégorie principale
                self.task_manager.add_category(new_category)

            # Mettre à jour l'arborescence des catégories
            self.update_category_tree()

    def delete_category(self):
        # Vérifier si une catégorie est sélectionnée
        if not self.current_category:
            messagebox.showerror("Erreur", "Aucune catégorie sélectionnée")
            return

        # Confirmer la suppression
        if messagebox.askyesno("Supprimer la Catégorie", f"Êtes-vous sûr de vouloir supprimer la catégorie '{self.current_category}' ?"):
            # Supprimer la catégorie et ses sous-catégories
            self.task_manager.remove_category(self.current_category)

            # Réinitialiser la catégorie courante et mettre à jour l'arborescence
            self.current_category = None
            self.update_category_tree()
            self.update_tasks_listbox()

    def update_tasks_listbox(self):
        # Effacer la liste des tâches
        self.tasks_listbox.delete(0, tk.END)

        # Si une catégorie est sélectionnée, afficher ses tâches
        if self.current_category:
            tasks = self.task_manager.get_tasks_by_category(self.current_category)
        else:
            # Sinon, afficher toutes les tâches
            tasks = self.task_manager.tasks

        # Ajouter chaque tâche à la liste
        for task in tasks:
            self.tasks_listbox.insert(tk.END, f"{task.description} - {task.deadline} - {task.priority}")

    def update_category_tree(self):
        # Effacer l'arborescence des catégories
        self.category_tree.delete(*self.category_tree.get_children())

        # Insérer la catégorie principale (s'il en existe une)
        root_category = self.task_manager.get_root_category()
        if root_category:
            self.category_tree.insert("", tk.END, text=root_category.name, values=[root_category.name])
            self._populate_subcategories(root_category)

    def _populate_subcategories(self, category):
        # Fonction récursive pour parcourir les sous-catégories
        for subcategory in category.subcategories:
            self.category_tree.insert(category.name, tk.END, text=subcategory.name, values=[subcategory.name])
            self._populate_subcategories(subcategory)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    app.run()
