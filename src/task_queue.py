from collections import deque

class Filesecondes_avant_deadline:
    def __init__(self):
        # Initialisation d'une file d'attente vide en utilisant deque de la bibliothèque collections
        self.elements = deque()

    def est_vide(self):
        # Vérifie si la file d'attente est vide en regardant sa longueur
        return len(self.elements) == 0

    def ajouter(self, element):
        # Parcours de la file d'attente
        for i, elt in enumerate(self.elements):
            # Si la date limite de la nouvelle tâche est proche avant celle de l'élément actuel
            if element.secondes_avant_deadline() < elt.secondes_avant_deadline():
                # Insertion de la nouvelle tâche avant l'élément actuel
                self.elements.insert(i, element)
                return
        
        # Si la nouvelle tâche a la date limite la plus éloignée, l'ajouter à la fin de la file
        self.elements.append(element)

    def retirer(self):
        # Retire et renvoie l'élément en tête de file
        return self.elements.popleft()

    def premier(self):
        # Renvoie l'élément en tête de file sans le retirer
        return self.elements[0]
