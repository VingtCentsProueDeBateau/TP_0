for i in range(1, 11):
    if i < 10:
        print(i, end=" - ")
    else:
        print(i) # condition IF dans la boucle FOR

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

nbLignes: int = int(input("Combien de lignes? "))
etoiles: str = "*"
TXT_ROUGE: str = "\033[91m"
TXT_RESET: str = "\033[0m"

if 255 >= nbLignes >= 1:
    for i in range(nbLignes):
        print("*" * (i + 1))
else:
    print(TXT_ROUGE + "ERREUR: NOMBRE INVALIDE" + TXT_RESET)
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#de: int = 0
#choixValide: bool = False
#
#while not choixValide:
#    de = int(input("Entrez un nombre entre 1 et 6: "))
#    choixValide = de < 1 or de > 6
#    if not choixValide:
#        print(TXT_ROUGE + "CHOIX INVALIDE" + TXT_RESET) # ??? marche pas???