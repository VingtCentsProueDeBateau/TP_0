nombre: int = int(input("Entrez un nombre: "))

if nombre == 420:
    print("Arrête de tricher")
else:
    for nombre in range(0, 421):
        nombre += 5
        print(nombre)
        if nombre == 420:
            break
        

    if nombre == 420:
        print("420!!!")
    elif nombre > 420:
        for nombre in range(419, 450):
            nombre -= 2
            print(nombre)
            if nombre == 420:
                break
        if nombre < 420:
            for nombre in range(0, 421):
                nombre += 1
                print(nombre)            
        elif nombre == 420:
            print("420!!!")
        else:
            print("euhh")
    else:
        print("euhh")