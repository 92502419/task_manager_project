from src.category import Category

class TaskManager:
    def __init__(self):
        self.tasks = []  # Initialise une liste vide de tâches.
        self.categories = []  # Initialise une liste vide de catégories.

    def add_task(self, task, name=None):
        # Ajoute une tâche à la liste des tâches générales ou à une catégorie spécifique.
        if name:
            category = self.find_category(name)
            if category:
                category.tasks.append(task)
        else:
            self.tasks.append(task)

    def remove_task(self, task, name=None):
        # Supprime une tâche de la liste des tâches générales ou d'une catégorie spécifique.
        if name:
            category = self.find_category(name)
            if category:
                category.tasks.remove(task)
        else:
            self.tasks.remove(task)

    def update_task(self, old_task, new_task, name=None):
        # Met à jour une tâche dans la liste des tâches générales ou d'une catégorie spécifique.
        if name:
            category = self.find_category(name)
            if category:
                index = category.tasks.index(old_task)
                category.tasks[index] = new_task
        else:
            index = self.tasks.index(old_task)
            self.tasks[index] = new_task

    def add_category(self, category, parent=None):
        # Ajoute une nouvelle catégorie ou sous-catégorie.
        if parent:
            parent = self.find_category(parent)
            if parent:
                parent.subcategories.append(category)
        else:
            self.categories.append(category)

    def remove_category(self, name):
        # Supprime une catégorie ou sous-catégorie.
        category = self.find_category(name)
        if category:
            self.categories.remove(category)

    def find_category(self, name):
        # Trouve une catégorie par son nom.
        for category in self.categories:
            if category.name == name:
                return category
        return None
    
    def get_root_category(self):
        """
        Renvoie la catégorie racine avec un nom spécifique (si elle existe) ou None.
        """
        root_category_name = "Nom de votre catégorie racine"  # Remplacez par le nom réel de la catégorie racine.
        for category in self.categories:
            if category.name == root_category_name:
                return category
        return None

""" Cette classe TaskManager permet de gérer des tâches et des catégories de tâches. 
    Elle contient des méthodes pour ajouter, supprimer et mettre à jour des tâches, 
    ainsi que pour ajouter et supprimer des catégories. La méthode find_category permet 
    de trouver une catégorie par son nom, et get_root_category renvoie la catégorie racine (si elle existe).
"""