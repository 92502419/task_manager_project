class Pilepriority:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return len(self.elements) == 0

    def empiler(self, element):
        """
        Ajoute une nouvelle tâche à la pile en respectant la priorité.

        Args:
            element: La nouvelle tâche à ajouter.
        """

        # Parcours de la pile
        for i, elt in enumerate(self.elements):
            # Si la priorité de la nouvelle tâche est supérieure à celle de l'élément actuel
            if element.priority > elt.priority:
                # Insertion de la nouvelle tâche avant l'élément actuel
                self.elements.insert(i, element)
                return
    
        # Si la nouvelle tâche a la priorité la plus basse
        self.elements.append(element)


    def depiler(self):
        return self.elements.pop()

    def premier(self):
        return self.elements[-1]
