import random
from COULEURS import *

nombre: int
devine: int
nombreMax: int = 0
essaisMax: int = 0
continuer: bool = True
diff: int = 0
essai: int
nombreMin: int = 0
jeu: bool = True

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

    essai = 1
    nombre = random.randint(0, nombreMax)


    while essai <= essaisMax and jeu == True:
        devine = int(input(f"({essai}/{essaisMax}) {nombreMin} < ? < {nombreMax} : "))
        if devine > nombreMax or devine < nombreMin and essai != essaisMax:
            print(f"{ROUGE}Nombre en dehors des limites. Veuillez réessayer.{RESET}")
            essai += 1
        elif devine < nombre and essai != essaisMax:
            nombreMin = devine
            essai += 1
        elif devine > nombre and essai != essaisMax:
            nombreMax = devine
            essai += 1
        elif devine == nombre and essai != essaisMax:
            print("Félicitations, vous avez trouvé le nombre mystère!")
            essai = essaisMax + 1
        elif essai == essaisMax:
            print(f"Vous avez échoué! Le nombre était: {nombre}")
            jeu = False

if jeu == False:
    continuer = bool(input("Voulez-vous recommencer? '1' pour OUI / '0' pour NON; "))
    if continuer:
        jeu = True
    else: jeu = False