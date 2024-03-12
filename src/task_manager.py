from src.category import Category
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

