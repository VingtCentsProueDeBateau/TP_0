import random
from COULEURS import *

nombre: int
devine: int
nombreMax: int
essaisMax: int
continuer: int = 1

while continuer == 1:
    diff: int = int(input(f"{MAUVE}Choisissez une difficulté: 1 = FACLIE, 2 = MOYEN, 3 = DIFFICILE, 4 = RIDICULE, 5 = CUSTOM: {RESET}"))

    match diff:
        case 1:
            essaisMax = 5
            nombreMax = 20

        case 2:
            essaisMax = 5
            nombreMax = 100

        case 3:
            essaisMax = 2
            nombreMax = 100

        case 4:
            essaisMax = 1
            nombreMax = 1000

        case 5:
            nombreMax = int(input("Nombre maximal: "))
            essaisMax = int(input("Quantité d'essais: "))

        case _:
            print("ERREUR. REDÉMARRER.")
            essaisMax = 0
            nombreMax = 0

    essais: int = essaisMax
    nombre = random.randint(0, nombreMax)


    while essais > 0:
        devine = int(input(f"Devinez un nombre entre 1 et {nombreMax}. {essais} essais restants: "))
        if devine == nombre:
            print(f"{VERT}Bonne réponse!{RESET}")
            break
        else:
            print(f"{ROUGE}Mauvaise réponse.{RESET}")
            if devine < nombre:
                print(f"{BLEU_CLAIR}TROP FROID{RESET}")
            elif devine > nombre:
                print(f"{JAUNE_CLAIR}TROP CHAUD{RESET}")
            essais -= 1

        if essais == 0:
            print(f"Le nombre était {nombre}")
    continuer = int(input("Continuer? 1 pour OUI, 0 pour NON; "))