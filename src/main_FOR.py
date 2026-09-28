for i in range(5): # i est un itérateur: variable par défaut pour "for" ; range(5): code effectuer tant que i n'atteint pas 5 à partir de 0. "for" rajoute 1 à chaque opération
    print(i)

for i in range(1, 6): # i commence à 1 au lieu de 0. dernier nombre est tjrs exclu
    print("i= ", i)
    
    
for i in range(1, 10, 2): # 1 à 10 à bonds de 2
    print("i10= ", i)
    if i == 7:
        break # NE PAS UTILISER BREAK EN BOUCLE FOR!!! INTERDIT EN COURS!!!
else:
    print("banane")
    
#for i in range(10, 1, -1): ## ne fonctionne pas: pas capable de faire bonds de -1
#    print(i)

somme: int = 0

for i in range(1, 101):
    somme += i

print(somme) # somme fait 0, + 1 = 1, + 2 = 3, + 3 = 6, + 4 = 10...