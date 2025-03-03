from src.plant import Plant

class Salade(Plant):
    def __init__(self, name):
        super().__init__(name, 5, 7, 5)
        self.est_mort = False
        

    def croitre (self):
        if (self.etat >= 5 and self.eau >= 7 and self.terre >= 5):
            print(f"{self.name} grandi !")
