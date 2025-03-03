from src.plant import Plant

class tournesol(Plant):
    def __init__(self, name):
        super().__init__(name, 8, 5, 5)
        self.est_mort = False
        

    def croitre (self):
        if (self.etat >= 8 and self.eau >= 6 and self.terre >= 5) :
            print(f"{self.name} grandi !")