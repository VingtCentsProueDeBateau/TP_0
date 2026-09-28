# LE JEU
import random
diff: int = int(input("Chosissez une difficulté (1 = facile, 2 = moyen, 3 = difficile et 4 = ridicule) : "))
devine: int

nombre: int

    
match diff:
    case 1:
        nombre = random.randint(1, 20)
        devine = int(input("Devinez un nombre entre 1 et 20 (essais restants: 5): "))
        
        if devine <= 0 or devine > 20:
            print("Nombre non compris entre 0 et 20.")
        if devine != nombre:
            devine = int(input("Mauvaise réponse (essais restants: 4): "))
            
            if devine <= 0 or devine > 20:
                print("Nombre non compris entre 0 et 20.")
            if devine != nombre:
                devine = int(input("Mauvaise réponse (essais restants: 3): "))
                
            if devine <= 0 or devine > 20:
                print("Nombre non compris entre 0 et 20.")
                if devine != nombre:
                    devine = int(input("Mauvaise réponse (essais restants: 2): "))
                    
                if devine <= 0 or devine > 20:
                    print("Nombre non compris entre 0 et 20.")
                    if devine != nombre:
                        devine = int(input("Mauvaise réponse (essais restants: 1): "))
                        
                    if devine <= 0 or devine > 20:
                        print("Nombre non compris entre 0 et 20.")
                        if devine != nombre:
                            print("Nombre non trouvé! Le nombre était:", nombre)
                            
                        else:
                            print(devine,": Bonne réponse!")
                            
                    else:
                        print(devine,": Bonne réponse!")
                        
                else:
                    print(devine,": Bonne réponse!")
                    
            else:
                print(devine,": Bonne réponse!")
                
        else:
            print(devine,": Bonne réponse!")
            
        
    case 2:
        nombre = random.randint(1, 100)
        devine = int(input("Devinez un nombre entre 1 et 100 (essais restants: 5): "))
        
        if devine <= 0 or devine > 100:
            print("Nombre non compris entre 0 et 100.")
        if devine != nombre:
            devine = int(input("Mauvaise réponse (essais restants: 4): "))
            
            if devine <= 0 or devine > 100:
                print("Nombre non compris entre 0 et 100.")
            if devine != nombre:
                devine = int(input("Mauvaise réponse (essais restants: 3): "))
                
            if devine <= 0 or devine > 100:
                print("Nombre non compris entre 0 et 100.")
                if devine != nombre:
                    devine = int(input("Mauvaise réponse (essais restants: 2): "))
                    
                if devine <= 0 or devine > 100:
                    print("Nombre non compris entre 0 et 100.")
                    if devine != nombre:
                        devine = int(input("Mauvaise réponse (essais restants: 1): "))
                        
                    if devine <= 0 or devine > 100:
                        print("Nombre non compris entre 0 et 100.")
                        if devine != nombre:
                            print("Nombre non trouvé! Le nombre était:", nombre)
                            
                        else:
                            print(devine,": Bonne réponse!")
                            
                    else:
                        print(devine,": Bonne réponse!")
                        
                else:
                    print(devine,": Bonne réponse!")
                    
            else:
                print(devine,": Bonne réponse!")
                
        else:
            print(devine,": Bonne réponse!")
            
        
    case 3:
        nombre = random.randint(1, 100)
        devine = int(input("Devinez un nombre entre 1 et 100 (essais restants: 2): "))
        
        if devine <= 0 or devine > 100:
            print("Nombre non compris entre 0 et 100.")
        if devine != nombre:
            devine = int(input("Mauvaise réponse (essais restants: 1): "))
            
            if devine <= 0 or devine > 100:
                print("Nombre non compris entre 0 et 100.")
            if devine != nombre:
                print("Nombre non trouvé! Le nombre était:", nombre)
            
            else:
                print(devine,": Bonne réponse!")
                
        else:
            print(devine,": Bonne réponse!")
    
    case 4:
        nombre = random.randint(1, 1000)
        devine = int(input("Devinez un nombre entre 1 et 1000 (1 seul essai!): "))
        
        if devine <= 0 or devine > 1000:
            devine = int(input("Nombre non compris entre 0 et 1000. Deuxième essai de grâce: "))
            
            if devine != nombre:
                print("Nombre non trouvé! Le nombre était:", nombre)
                
            else:
                print(devine,": Bonne réponse!")     
                           
        elif devine != nombre:
            print("Nombre non trouvé! Le nombre était:", nombre)

        else:
            print(devine,": Bonne réponse!")
    
    case _:
        print("Difficulté invalide. Redémarrer le programme.")