TAILLE: int = 5
tourX: bool = True
damier: str = ""

for _ in range(TAILLE): # RANGÉE
    for _ in range(TAILLE): # COLONNE
        print("x " if tourX else "o ", end="")
        tourX = not tourX # utile pour inverser et ré-inverser
    print()
    
    

for i in range(TAILLE):
    for j in range(TAILLE):
        if (i + j) % 2 == 0:
            damier += "X "
        else:
            damier += "O "
    damier += "\n" # RAPPEL: \n = ENTRÉE

print(damier, end="")