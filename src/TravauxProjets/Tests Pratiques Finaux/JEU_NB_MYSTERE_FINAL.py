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

    essai = 0
    nombre = random.randint(0, nombreMax)


    while essai <= essaisMax:
        devine = int(input(f"({essai}/{essaisMax}) 0 < ? < {nombreMax} : "))
        if devine > nombreMax or devine < nombreMin:
            print(f"{ROUGE}Nombre en dehors des limites. Veuillez réessayer.{RESET}")
            essai += 1
        elif devine < nombre:
            nombreMin = devine
            essai += 1
        elif devine > nombre:
            nombreMax = devine
            essai += 1
        else:
            print("Félicitations, vous avez trouvé le nombre mystère!")
            essai = essaisMax + 1

    if essai == essaisMax:
        print(f"Vous avez échoué! le nombre était: {nombre}")

continuer = bool(input("Voulez-vous recommencer? '1' pour OUI / '0' pour NON; "))








#    if devine == nombre:
#        print(f"{VERT}Bonne réponse!{RESET}")
#        break
#    else:
#        print(f"{ROUGE}Mauvaise réponse.{RESET}")
#        if devine < nombre:
#            print(f"{BLEU_CLAIR}TROP FROID{RESET}")
#        elif devine > nombre:
#            print(f"{JAUNE_CLAIR}TROP CHAUD{RESET}")
#        essais += 1
#        
#    if essais == 0:
#        print(f"Le nombre était {nombre}")
#continuer = int(input("Continuer? 1 pour OUI, 0 pour NON; "))