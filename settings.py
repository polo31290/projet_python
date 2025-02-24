import random

class Plant:
    def __init__(self):
        self.niveau_eau = 100  # Niveau d'eau initial
        self.exposition_lumiere = 100  # Exposition à la lumière initiale
        self.etat_terre = 100  # État de la terre initial

    def evenement_secheresse(self):
        self.niveau_eau -= 20  # Diminuer le niveau d'eau
        self.exposition_lumiere += 10  # Augmenter l'exposition à la lumière

    def evenement_inondation(self):
        self.niveau_eau += 20  # Augmenter le niveau d'eau
        self.exposition_lumiere -= 10  # Diminuer l'exposition à la lumière

    def attaque_nuisible(self):
        self.niveau_eau -= 10  # Diminuer le niveau d'eau
        self.exposition_lumiere -= 10  # Diminuer l'exposition à la lumière
        self.etat_terre -= 10  # Diminuer l'état de la terre

    def tempete(self):
        self.niveau_eau += 10  # Augmenter le niveau d'eau
        self.exposition_lumiere -= 10  # Diminuer l'exposition à la lumière
        self.etat_terre -= 10  # Diminuer l'état de la terre

    def verifier_sante_plante(self):
        if self.niveau_eau <= 0 or self.exposition_lumiere <= 0 or self.etat_terre <= 0:
            return False  # La plante est morte
        else:
            return True  # La plante est en vie

    def evenement_survenu(self):
        evenement = random.choice(["secheresse", "inondation", "attaque_nuisible", "tempete"])
        if evenement == "secheresse":
            self.evenement_secheresse()
        elif evenement == "inondation":
            self.evenement_inondation()
        elif evenement == "attaque_nuisible":
            self.attaque_nuisible()
        elif evenement == "tempete":
            self.tempete()
