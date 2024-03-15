class Category:
    def __init__(self, name, parent=None):
        self.name = name
        self.tasks = []
        self.subcategories = []
    
    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def add_subcategory(self, subcategory):
        self.subcategories.append(subcategory)

    def remove_subcategory(self, subcategory):
        self.subcategories.remove(subcategory)    
