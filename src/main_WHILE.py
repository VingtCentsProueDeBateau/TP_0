tour: int = 1
continuer: bool = True

while tour <= 5 and continuer:
    print("alo lé zami") # n'arrête pas
    break # temporaire: pour arrêter la boucle
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

de: int = 0

while de < 1 or de > 6:
    de = int(input("Entrez un nombre entre 1 et 6: "))

print(de)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

for i in range(1, 11, 1):
    print(i)
    
banane: int = 1

while banane <= 10:
    print(banane)
    banane += 1 # même fonction que le for juste avant
    


nova: int = 1
resultat = ""

while nova <= 10:
    resultat += str(nova) + \
        " - " if nova < 10 else ""
    nova += 1

print(resultat)



SEUIL: int = 1000

somme: int = 0
ctrl: int = 1

while somme < SEUIL:
    somme += ctrl
    ctrl += 1

print(somme)