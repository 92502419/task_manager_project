from tkinter import Tk
from ui.app import TaskManagerApp

if __name__ == "__main__":
    root = Tk()
    app = TaskManagerApp(root)
    app.run()

