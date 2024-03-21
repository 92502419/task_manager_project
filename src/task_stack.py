class Pilepriority:
    def __init__(self):
        # Initialise une pile vide en utilisant une liste
        self.elements = []

    def est_vide(self):
        # Vérifie si la pile est vide en regardant sa longueur
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
    
        # Si la nouvelle tâche a la priorité la plus basse, l'ajouter à la fin de la pile
        self.elements.append(element)

    def depiler(self):
        # Retire et renvoie l'élément en haut de la pile
        return self.elements.pop()

    def premier(self):
        # Renvoie l'élément en haut de la pile sans le retirer
        return self.elements[-1]
