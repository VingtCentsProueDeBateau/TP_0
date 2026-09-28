import random
diff: int = int(input("Chosissez une difficulté (1 = facile, 2 = moyen, 3 = difficile, 4 = ridicule 5 = custom) : "))

devine: int
nombre: int
essais: int
nbMax: int
bonneRéponse: bool = False


match diff:
    case 1:
        nombre = random.randint(1, 20)
        print("Devinez un nombre entre 1 et 20 en 5 essais!")
        
        for essais in range(1, 6, 1):
            if bonneRéponse == False:
                print("essai #", essais)
                devine = int(input("Devinez un nombre: "))
            
                if devine == nombre:
                    bonneRéponse = True

                elif devine != nombre and bonneRéponse == False:
                    print("Mauvaise réponse.")
                    if devine > nombre:
                        print("TROP CHAUD")
                    elif devine < nombre:
                        print("TROP FROID")
                    essais += 1
            else:
                print(nombre,": Bonne réponse!")
                break
                
        print("La réponse était:", nombre)
        
    case 2:
        nombre = random.randint(1, 100)
        print("Devinez un nombre entre 1 et 100 en 5 essais!")
        
        for essais in range(1, 6, 1):
            if bonneRéponse == False:
                print("essai #", essais)
                devine = int(input("Devinez un nombre: "))
            
                if devine == nombre:
                    bonneRéponse = True

                elif devine != nombre and bonneRéponse == False:
                    print("Mauvaise réponse.")
                    if devine > nombre:
                        print("TROP CHAUD")
                    elif devine < nombre:
                        print("TROP FROID")
                    essais += 1
            else:
                print(nombre,": Bonne réponse!")
                break
                
        print("La réponse était:", nombre)
                   
    case 3:
        nombre = random.randint(1, 100)
        print("Devinez un nombre entre 1 et 100 en 2 essais!")
        
        for essais in range(1, 3, 1):
            if bonneRéponse == False:
                print("essai #", essais)
                devine = int(input("Devinez un nombre: "))
            
                if devine == nombre:
                    bonneRéponse = True

                elif devine != nombre and bonneRéponse == False:
                    print("Mauvaise réponse.")
                    if devine > nombre:
                        print("TROP CHAUD")
                    elif devine < nombre:
                        print("TROP FROID")
                    essais += 1
            else:
                print(nombre,": Bonne réponse!")
                break
                
        print("La réponse était:", nombre)
                        
    case 4:
        nombre = random.randint(1, 1000)
        print("Devinez un nombre entre 1 et 1000 en un seul essai!")
        
        for essais in range(1, 2, 1):
            if bonneRéponse == False:
                print("Un seul essai.")
                devine = int(input("Devinez un nombre: "))
            
                if devine == nombre:
                    bonneRéponse = True

                elif devine != nombre and bonneRéponse == False:
                    print("Mauvaise réponse.")
                    
            else:
                print(nombre,": Bonne réponse!")
                break
                
        print("La réponse était:", nombre)
                
    case 5:
        nbMax = int(input("Nombre maximum: "))
        nombre = random.randint(1, nbMax)
        essais = int(input("Nombre d'essais maximal: "))
        print(f"Devinez un nombre entre 1 et {nbMax} en {essais} essais!")
                
        for essais in range(1, (essais + 1), 1):
            if bonneRéponse == False:
                print("essai #", essais)
                devine = int(input("Devinez un nombre: "))
            
                if devine == nombre:
                    bonneRéponse = True

                elif devine != nombre and bonneRéponse == False:
                    print("Mauvaise réponse.")
                    if devine > nombre:
                        print("TROP CHAUD")
                    elif devine < nombre:
                        print("TROP FROID")
                    essais += 1
            else:
                print(nombre,": Bonne réponse!")
                break
                
        print("La réponse était:", nombre)
                
    case _:
        print("Difficulté non valide. Redémarrer le programme.")