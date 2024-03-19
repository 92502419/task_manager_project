from tkinter import Tk  # Importe la classe Tk de tkinter pour créer une fenêtre principale.
from ui.app import TaskManagerApp  # Importe la classe TaskManagerApp de votre module ui.app.


if __name__ == "__main__":  # Vérifie si le script est exécuté en tant que programme principal.
    root = Tk()  # Crée une instance de la classe Tk pour la fenêtre principale.
    app = TaskManagerApp(root)  # Crée une instance de la classe TaskManagerApp en lui passant la fenêtre principale.
    app.run()  # Lance la boucle principale de l'application tkinter pour afficher la fenêtre et gérer les événements.