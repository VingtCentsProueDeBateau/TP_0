estValide: bool

mois = int(input("Quel mois? "))
jour = int(input("Quel jour? "))

match mois:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        estValide = 1 <= jour <= 31
    case 4 | 6 | 9 | 11:
        estValide = 1 <= jour <= 30
    case 2:
        estValide = 1 <= jour <= 28
    case _:
        estValide = False

print("Valide" if estValide else "Invalide")