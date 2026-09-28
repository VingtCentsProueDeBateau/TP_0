import random
diff: int = int(input("Chosissez une difficulté (1 = facile, 2 = moyen, 3 = difficile, 4 = ridicule 5 = custom) : "))

devine: int
nombre: int
essais: int
nbMax: int
essaisMax: int


match diff:
    case 1:
        nbMax = 20
        nombre = random.randint(1, 20)
        essaisMax = 5
        
    case 2:
        nbMax = 100
        nombre = random.randint(1, 100)
        essaisMax = 5
        
    case 3:
        nbMax = 100
        nombre = random.randint(1, 100)
        essaisMax = 2
        
    case 4:
        nbMax = 1000
        nombre = random.randint(1, 1000)
        essaisMax = 1
                     
    case 5:
        nbMax = int(input("Nombre maximum: "))
        nombre = random.randint(1, nbMax)
        essaisMax = int(input("Nombre d'essais maximal: "))
                
    case _:
        print("Difficulté non valide. Redémarrer le programme.")
        nbMax = 0
        essaisMax = 0
        nombre = 0
        
print(f"Devinez un nombre entre 1 et {nbMax} en {essaisMax} essais!")
for essais in range(1, (essaisMax + 1), 1):
    devine = int(input(f"Essai #{essais}: "))
    if devine == nombre:
        print("Bonne réponse!")
        break
    else:
        print("Mauvaise réponse.")
        if devine < nombre:
            print("TROP FROID")
        elif devine > nombre:
            print("TROP CHAUD")
        essais += 1

print("La réponse était:", nombre)