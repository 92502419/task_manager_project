from src.category import Category
from tkinter import messagebox
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.categories = []

    def add_task(self, task, category_name=None):
        if category_name:
            category = self.find_category(category_name)
            if category:
                category.tasks.append(task)
        else:
            self.tasks.append(task)

    def remove_task(self, task, category_name=None):
        if category_name:
            category = self.find_category(category_name)
            if category:
                category.tasks.remove(task)
        else:
            self.tasks.remove(task)

    def update_task(self, old_task, new_task, category_name=None):
        if category_name:
            category = self.find_category(category_name)
            if category:
                index = category.tasks.index(old_task)
                category.tasks[index] = new_task
        else:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task

    def add_category(self, category_name, parent_category=None):
        category = Category(category_name)
        if parent_category:
            parent = self.find_category(parent_category)
            if parent:
                parent.subcategories.append(category)
        else:
            self.categories.append(category)

    def remove_category(self, category_name):
        category = self.find_category(category_name)
        if category:
            self.categories.remove(category)

    def find_category(self, category_name):
        for category in self.categories:
            if category.name == category_name:
                return category
        return None
    
    def update_category(self, old_category_name, new_category_name): 
        """
        Met à jour le nom d'une catégorie dans TaskManager et l'arborescence des catégories.

        Args:
            old_category_name (str): Nom de la catégorie à mettre à jour.
            new_category_name (str): Nouveau nom de la catégorie.
        """

        category = self.find_category(old_category_name)

        # Si la catégorie est trouvée, mettre à jour son nom
        if category:
            category.name = new_category_name

            # Mettre à jour l'arborescence des catégories
            self.update_category_tree()

        else:
            # Afficher un message d'erreur si la catégorie n'est pas trouvée
            messagebox.showerror("Erreur", f"Catégorie '{old_category_name}' non trouvée.")

    def _update_subcategory_references(self, category, old_name, new_name):
        """
        Updates the category name reference in subcategories and their tasks (recursive).

        Args:
            category (Category): The category object.
            old_name (str): Old name of the category.
            new_name (str): New name of the category.
        """

        for subcategory in category.subcategories:
            # Update subcategory name if it matches the old name
            if subcategory.name == old_name:
                subcategory.name = new_name

            # Update tasks in the subcategory
            for task in subcategory.tasks:
                if task.category == old_name:
                    task.category = new_name

            # Update references in sub-subcategories (recursive call)
            self._update_subcategory_references(subcategory, old_name, new_name)


    def get_root_category(self):
        """
        Renvoie la catégorie racine avec un nom spécifique (si elle existe) ou None.
        """
        nom_category_racine = "Nom de votre catégorie racine"  # Remplacez par le nom réel
        for category in self.categories:
            if category.name == nom_category_racine:
                return category
        return None
