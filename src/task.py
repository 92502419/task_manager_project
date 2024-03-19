from datetime import datetime
class Task:
    def __init__(self, description, deadline, priority ):
        self.description = description
        self.deadline = deadline
        self.priority = priority
        """self.category = category"""



    def secondes_avant_deadline(self):
        """
        Calcule le nombre de secondes qui restent avant l'arrivée de la date limite de la tâche.

        Returns:
            Le nombre de secondes restantes avant la date limite.
        """

        # Conversion de la date limite en datetime
        deadline_datetime = datetime.strptime(self.deadline, "%Y-%m-%d")

        # Calcul du nombre de secondes restantes
        secondes_restantes = (deadline_datetime - datetime.today()).total_seconds()

        # Retour du nombre de secondes
        return secondes_restantes