nbLignes: int = int(input("Combien de lignes? "))
etoiles: str = "*"

if nbLignes > 255:
    print("Nombre trop grand, opération refusée: nb. maximal = 255")
else:
    for i in range(nbLignes):
        print("*" * (i + 1))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# inverser chiffres dans un nombre: ex. 1234 devient 4321

nombre: str = str(input("Nombre: "))
nbChiffres: int = len(str(nombre))

nombre[::-1]
