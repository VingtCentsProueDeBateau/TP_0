import random
from COULEURS import *

nombre: int = 0
devine: int
nombreMax: int = 0
essaisMax: int = 0
continuer: bool
diff: int = 0
essai: int = 1
nombreMin: int = 0
jeu: int = 0


while jeu >= 0:
    if jeu == 0:
        continuer = bool(input("Entrez un caractère non-nul pour commencer!"))
    else:
        continuer = bool(input("Voulez vous recommencer? '0' pour FERMER, '1' pour CONTINUER"))

    while continuer:
        while diff < 1 or diff > 5:
            diff = int(input(f"{MAUVE}Choisissez une difficulté: 1 = FACLIE, 2 = MOYEN, 3 = DIFFICILE, 4 = RIDICULE, 5 = CUSTOM: {RESET}"))

            match diff:
                case 1:
                    essaisMax = 10
                    nombreMax = 20

                case 2:
                    essaisMax = 5
                    nombreMax = 50

                case 3:
                    essaisMax = 5
                    nombreMax = 100

                case 4:
                    essaisMax = 1
                    nombreMax = 1000

                case 5:
                    nombreMax = int(input("Nombre maximal: "))
                    essaisMax = int(input("Quantité d'essais: "))

                case _:
                    print("ERREUR. REDÉMARRER.")

        nombre = random.randint(0, nombreMax)


        while essai <= essaisMax:
            devine = int(input(f"({essai}/{essaisMax}) {nombreMin} < ? < {nombreMax} : "))
            if devine > nombreMax or devine < nombreMin and essai != essaisMax:
                print(f"{ROUGE}Nombre en dehors des limites. Veuillez réessayer.{RESET}")
                essai += 1
            elif devine < nombre and essai <= essaisMax:
                nombreMin = devine
                essai += 1
            elif devine > nombre and essai <= essaisMax:
                nombreMax = devine
                essai += 1
            elif devine == nombre and essai <= essaisMax:
                print("Félicitations, vous avez trouvé le nombre mystère!")

    if essai > essaisMax:
        print(f"Vous avez échoué! Le nombre mystère était: {nombre}")
        
    jeu += 1