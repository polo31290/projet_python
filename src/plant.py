class Plante:
    def __init__(self, exposition_lumiere, taux_eau, etat_terre):
        self.exposition_lumiere = exposition_lumiere
        self.taux_eau = taux_eau
        self.etat_terre = etat_terre
        self.etat_gen = (exposition_lumiere + taux_eau + etat_terre) / 3

    def arroser(self):
        self.taux_eau += 1
        self.etat_gen = (self.exposition_lumiere + self.taux_eau + self.etat_terre) / 3

    def exposer_a_la_lumiere(self):
        self.exposition_lumiere += 1
        self.etat_gen = (self.exposition_lumiere + self.taux_eau + self.etat_terre) / 3

    def fertiliser_sol(self):
        self.etat_terre += 1
        self.etat_gen = (self.exposition_lumiere + self.taux_eau + self.etat_terre) / 3
