import random
import time

class Plante:
    def __init__(self, nom):
        self.nom = nom
        self.niveau_eau = 5
        self.qualite_sol = 5
        self.exposition_lumiere = 5
        self.sante = 10
    
    def arroser(self):
        self.niveau_eau += 1
        print(f"Vous avez arrosé {self.nom}. Le niveau d'eau est maintenant de {self.niveau_eau}.")
    
    def fertiliser(self):
        self.qualite_sol += 1
        print(f"Vous avez fertilisé {self.nom}. La qualité du sol est maintenant de {self.qualite_sol}.")
    
    def fournir_lumiere(self):
        self.exposition_lumiere += 1
        print(f"Vous avez fourni de la lumière à {self.nom}. L'exposition à la lumière est maintenant de {self.exposition_lumiere}.")
    
    def evenement_aleatoire(self):
        evenement = random.choice(["secheresse", "attaque_de_nuisibles", "jour_nuageux"])
        if evenement == "secheresse":
            self.niveau_eau -= 2
            print(f"Une sécheresse est survenue ! Le niveau d'eau de {self.nom} a diminué à {self.niveau_eau}.")
        elif evenement == "attaque_de_nuisibles":
            self.sante -= 3
            print(f"Une attaque de nuisibles est survenue ! La santé de {self.nom} a diminué à {self.sante}.")
        elif evenement == "jour_nuageux":
            self.exposition_lumiere -= 2
            print(f"Un jour nuageux est survenu ! L'exposition à la lumière de {self.nom} a diminué à {self.exposition_lumiere}.")
    
    def statut(self):
        print(f"{self.nom} - Niveau d'eau: {self.niveau_eau}, Qualité du sol: {self.qualite_sol}, Exposition à la lumière: {self.exposition_lumiere}, Santé: {self.sante}")
    
    def est_vivante(self):
        return self.sante > 0 and self.niveau_eau > 0 and self.qualite_sol > 0 and self.exposition_lumiere > 0

def main():
    plante = Plante("Tournesol")
    
    while plante.est_vivante():
        plante.statut()
        action = input("Que voulez-vous faire ? (arroser/fertiliser/lumiere/passer) : ")
        if action == "arroser":
            plante.arroser()
        elif action == "fertiliser":
            plante.fertiliser()
        elif action == "lumiere":
            plante.fournir_lumiere()
        elif action == "passer":
            print("Vous avez choisi de passer votre tour.")
        else:
            print("Action invalide. Veuillez choisir à nouveau.")
        
        plante.evenement_aleatoire()
        time.sleep(1)
        
    print(f"{plante.nom} est morte. Fin du jeu.")

if __name__ == "__main__":
    main()