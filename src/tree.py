from src.plant import Plant

class arbre(Plant):
    def __init__(self, name):
        super().__init__(name, 6, 4, 4)
        self.est_mort = False

        
    def croitre (self):
        if (self.etat >= 6 and self.eau >= 5 and self.terre >= 5):
            print(f"{self.name} grandi !")