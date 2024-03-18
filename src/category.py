class Category:
    def __init__(self, name):
        self.name = name  # Initialise le nom de la catégorie.
        #self.tasks = []  # Initialise une liste vide pour stocker les tâches de la catégorie.
        self.subcategories = []  # Initialise une liste vide pour stocker les sous-catégories de la catégorie.

        #self.categories = []  # initialise une liste vide pour stocker les categories

"""
    def add_category(self, category):
        self.categories.append(category)  # Ajoute une catégorie à la liste des catégories de la catégorie.

    def add_task(self, task):
        self.tasks.append(task)  # Ajoute une tâche à la liste des tâches de la catégorie.

    def remove_task(self, task):
        self.tasks.remove(task)  # Supprime une tâche de la liste des tâches de la catégorie.

    def add_subcategory(self, subcategory):
        self.subcategories.append(subcategory)  # Ajoute une sous-catégorie à la liste des sous-catégories de la catégorie.

    def remove_subcategory(self, subcategory):
        self.subcategories.remove(subcategory)  # Supprime une sous-catégorie de la liste des sous-catégories de la catégorie.
"""