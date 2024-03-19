from collections import deque

class Filesecondes_avant_deadline:
    def __init__(self):
        self.elements = deque()
        

    def est_vide(self):
        return len(self.elements) == 0

    def ajouter(self, element):
        # Parcours de la file d'attente
        for i, elt in enumerate(self.elements):
            # Si la date limite de la nouvelle tâche est proche avant celle de l'élément actuel
            if element.secondes_avant_deadline() < elt.secondes_avant_deadline():
                # Insertion de la nouvelle tâche avant l'élément actuel
                self.elements.insert(i, element)
                return
        
        # Si la nouvelle tâche a la date limite la plus éloignée
        self.elements.append(element)

    def retirer(self):
        return self.elements.popleft()

    def premier(self):
        return self.elements[0]
