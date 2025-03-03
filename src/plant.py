class Plant:
    def __init__(self, name , etat, eau, terre):
        self.name = name
        self.etat = etat
        self.eau = eau
        self.terre = terre
        self.croissance = etat + eau + terre
        self.max_etat = 10
        self.max_eau = 10
        self.max_terre = 10

    def arroser(self):
        if self.eau < self.max_eau:
            self.eau += 2
            if self.eau > self.max_eau:
                self.eau = self.max_eau
            print(f"Vous avez arrosé {self.name}. Le niveau d'eau est maintenant de {self.eau}.")
        else:
            print(f"{self.name} a déjà atteint le niveau d'eau maximum.")

    def fertiliser(self):
        if self.terre < self.max_terre:
            self.terre += 2
            if self.terre > self.max_terre:
                self.terre = self.max_terre
            print(f"Vous avez fertilisé {self.name}. La qualité du sol est maintenant de {self.terre}.")
        else:
            print(f"{self.name} a déjà atteint la qualité du sol maximum.")

    def entretenir(self):
        if self.etat < self.max_etat:
            self.etat += 2
            if self.etat > self.max_etat:
                self.etat = self.max_etat
            print(f"Vous avez entretenu {self.name}. Son état est maintenant de {self.etat}.")
        else:
            print(f"{self.name} a déjà atteint l'état maximum.")
            

    def est_mort(self):
        if self.etat <= 0 or self.eau <= 0 or self.terre <= 0:
            print(f"{self.name} est mort.")
            return True
        return False