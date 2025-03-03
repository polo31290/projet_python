from src.salad import Salade
from src.sunflower import tournesol
from src.tree import arbre


def choisir_classe():
    while True:

        print("\nChoisissez votre plante :")
        print("1. Tournesol (taux d'eau : 5, etat du sol et de la terre: 5, taux d'exposition à la lumière: 8)")
        print("2. Arbre (taux d'eau : 4, etat du sol et de la terre: 4, taux d'exposition à la lumière: )")
        print("3. Salade (taux d'eau : 7, etat du sol et de la terre: 5, taux d'exposition à la lumière: 5)")
        choix = input("Votre choix : ")
        if choix == "1":
            return tournesol("tournesol")
        elif choix == "2":
            return arbre("arbre")
        elif choix == "3":
            return Salade("salade")
        else:
            print("Choix invalide, veuillez réessayer.")

plante = choisir_classe()

del plante.est_mort 


def choisir_action():
    while True:
        print("\nChoisissez une action :")
        print("1. arroser")
        print("2. fertiliser la terre")
        print("3. entretenir la plante")
        print("4. passer la journée")
        choix = input("Votre choix : ")
        if choix in ["1", "2", "3", "4"]:
            return choix
        else:
            print("Choix invalide, veuillez réessayer.")

tour = 1

while plante.est_mort() == False:
    print(f"\n--- jour : {tour} ---")
    print(f"{plante.name}: Etat: {plante.etat}, Eau: {plante.eau}, Terre: {plante.terre}")

    if plante == "tournesol":
        if plante.croissance >= 20:
            print(f"{plante.name} grandi !")
    elif plante == "arbre":
        if plante.croissance >= 25:
            print(f"{plante.name} grandi !")
    elif plante == "salade":
        if plante.croissance >= 15:
            print(f"{plante.name} grandi !")
    else:
        pass
    
    action = choisir_action()
    if action == "1":
        plante.arroser()

        if plante == "tournesol":
            if plante.croissance >= 20:
                print(f"{plante.name} grandi !")
        elif plante == "arbre":
            if plante.croissance >= 25:
                print(f"{plante.name} grandi !")
        elif plante == "salade":
            if plante.croissance >= 15:
                print(f"{plante.name} grandi !")
        else:
            pass
    elif action == "2":
        plante.fertiliser()

        if plante == "tournesol":
            if plante.croissance >= 20:
                print(f"{plante.name} grandi !")
        elif plante == "arbre":
            if plante.croissance >= 25:
                print(f"{plante.name} grandi !")
        elif plante == "salade":
            if plante.croissance >= 15:
                print(f"{plante.name} grandi !")
        else:
            pass

    elif action == "3":
        plante.entretenir()

        if plante == "tournesol":
            if plante.croissance >= 20:
                print(f"{plante.name} grandi !")
        elif plante == "arbre":
            if plante.croissance >= 25:
                print(f"{plante.name} grandi !")
        elif plante == "salade":
            if plante.croissance >= 15:
                print(f"{plante.name} grandi !")
        else:
            pass
    elif action == "4":
        pass

        if plante == "tournesol":
            if plante.croissance >= 20:
                print(f"{plante.name} grandi !")
        elif plante == "arbre":
            if plante.croissance >= 25:
                print(f"{plante.name} grandi !")
        elif plante == "salade":
            if plante.croissance >= 15:
                print(f"{plante.name} grandi !")
        else:
            pass
    else:
        print("Choix invalide, veuillez réessayer.")