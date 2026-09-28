# si dé = 1: PERDU
# si dé = 6: DOUBLE ou +1 (le plus grand)
# si dé = 2 à 5: +1

import random
de: int = 0
score: int = 0
continuer: bool = True


while de != 1 and continuer:
    de = random.randint(1, 6)
    if 2 <= de <= 5 or (de == 6 and score == 0):
        score += 1
    elif de == 6:
        score *= 2
        
    if de != 1:
        print(f"Vous avez lancé un {de}, vous avez maintenant {score} points")
        continuer = input("Voulez-vous continuer? O/N: ") == "O"
    else:
        print(f"Vous avez lancé un {de}")

if de == 1:
    print(f"Vous avez perdu. Vous aviez: {score} points")
else:
    print(f"Vous avez fini avec {score} points")