import random
from COULEURS import *
from lib import *


print("Bienvenue au jeu!")

deSix = random.randint(1, 6)
match deSix:
    case 1 | 2:
        mvt = "la Gauche"
        rencontre = random.randint(1, 2)
    case 3 | 4:
        mvt = "l'Avant"
        rencontre = 0
    case 5 | 6:
        mvt = "la Droite"
        rencontre = random.randint(0, 3)
    case _:
        mvt = "Nulle part"
        rencontre = 0

print(f"Vous avancez vers {mvt}")

match rencontre:
    case 1:
        enemi = "Zombie"
        enemiAtt = 5
        enemihp = 50
    case 2:
        enemi = "Squelette"
        enemiAtt = 7
        enemihp = 30
    case 3:
        enemi = "Arbre mort"
        enemiAtt = 0
        enemihp = 100
    case _:
        enemi = "Rien"
        enemiAtt = 0
        enemihp = 0
        print("Rien ne passe dans votre chemin.")
rencontre = 0
        
if enemi == "Zombie" or enemi == "Squelette" or enemi == "Arbre mort":
    print(f"{JAUNE}Vous rencontrez un {enemi}! Qu'allez vous faire?{RESET}")
    while enemihp > 0:
        choix = int(input("FRAPPER: 1 / ÉVITER LA PROCHAINE ATTAQUE: 2 / ITEM: 3 / NE RIEN FAIRE: 4"))
        
        if choix == 1:
            deVingt = random.randint(1, 20)
            print(f"Vous attaquez. Vous avez roulé un: {deVingt}.")
            
            match deVingt:
                case 1:
                    print(f"Attaque manquée! Skill issue, {enemi} rit de votre face")
                    degat = 0
                    
                case 2 | 3 | 4 | 5:
                    degat = (attaqueBase - 5)
                    print(f"Vous attaquez {enemi} pour {BLEU}{degat}{RESET} points de dégâts!")
                    enemihp -= degat
                    print(enemihp)
                    
                case 6 | 7 | 8 | 9 | 10:
                    degat = (attaqueBase - 2)
                    print(f"Vous attaquez {enemi} pour {BLEU}{degat}{RESET} points de dégâts!")
                    enemihp -= degat
                    print(enemihp)
                    
                case 11 | 12 | 13 | 14 | 15:
                    degat = attaqueBase
                    print(f"Vous attaquez {enemi} pour {BLEU}{degat}{RESET} points de dégâts")
                    enemihp -= degat
                    print(enemihp)
                    
                case _:
                    degat = (attaqueBase + 2)
                    print(f"Coup critique! Vous attaquez {enemi} pour {BLEU}{degat}{RESET} points de dégâts!")
                    enemihp -= degat
                    print(enemihp)
                    
            if enemi == "Squelette":
                print(f"{enemi} Riposte et vous fait {ROUGE_CLAIR}{enemiAtt}{RESET} dégâts!")
                sante -= enemiAtt
                print(f"Santé restante: {sante}")
                
            elif enemi == "Zombie":
                print(f"{enemi} Riposte et vous fait {ROUGE_CLAIR}{enemiAtt}{RESET} dégâts")
                sante -= enemiAtt
                print(f"Santé restante: {sante}")
            elif enemi == "Arbre mort":
                print("L'enemi ne riposte pas.")
            
        elif choix == 2:
            print("Vous éviterez la prochaine attaque.")
            print(f"{enemi} Vous attaque, mais vous évitez son attaque! Vous ne perdez aucune santé.")
            
        elif choix == 3:
            print("Quel item voulez vous utiliser?")
            item = int(input(f"Inventaire: Potion de Santé (Santé MAX) x{potion} [1], Pain (+ 25 Santé) x{pain} [2], Lait (+ 35 Santé) x{lait} [3], Pomme (+ 15 Santé) x{pomme} [4], Potion de Posion (Empoisonne l'enemi pour 25 dégâts) x{potion2} [5], Annuler [6] "))
            match item:
                case 1:
                    print(f"Vous utilisez Potion de Santé. Votre santé passe de {sante} à 100!")
                    potion -= 1
                    if sante >= 95:
                        print("Bravo, vous venez de gaspiller votre Potion de Santé.")
                case 2:
                    santeFin = sante + 25
                    pain -= 1
                    if santeFin > 100:
                        santeFin = 100
                    print(f"Vous utilisez Pain. Votre santé passe de {VERT}{sante}{RESET} à {VERT}{santeFin}{RESET}!")
                    sante = santeFin
                case 3:
                    santeFin = sante + 35
                    lait -= 1
                    if santeFin > 100:
                        santeFin = 100
                    print(f"Vous utilisez Lait. Votre santé passe de {VERT}{sante}{RESET} à {VERT}{santeFin}{RESET}!")
                    sante = santeFin
                case 4:
                    santeFin = sante + 15
                    pomme -= 1
                    if santeFin > 100:
                        santeFin = 100
                    print(f"Vous utilisez Pomme. Votre santé passe de {VERT}{sante}{RESET} à {VERT}{santeFin}{RESET}!")
                    sante = santeFin
                case 5:
                    enemihpFin = enemihp - 25
                    potion2 -= 1
                    print(f"Vous utilisez Potion de Poison.")
                    if enemihpFin <= 0:
                        print(f"Vous avez vaincu {enemi}!")
                    else:
                        print(f"{enemi} prends 25 dégâts, passant de {ROUGE}{enemihp}{RESET} à {ROUGE}{enemihpFin}{RESET}!")
                        enemihp = enemihpFin
                case _:
                    print("Choix annulé.")
        else:
            print("Vous ne faites rien.")
            if enemi != "Arbre mort":
                print(f"{enemi} vous attaque pour {ROUGE_CLAIR}{enemiAtt}{RESET} dégâts!")
                print(f"Vous passez de {sante} à {sante - enemiAtt}")
            else:
                print("... Rien ne se passe.")
    if enemihp <= 0:
        print(f"Vous avez vaincu {enemi}!")
        if enemi == "Zombie" or enemi == "Squelette":
            loot = "Os"
            ramasser = int(input(f"{enemi} a lâché {loot}! Voulez vous récupérer l'item? '1' pour OUI, '0' pour NON: "))
            if ramasser == 1:
                os += 1
                print(f"Vous ramassez 1 {loot}.")
            else:
                print(f"Vous laissez {loot} par terre comme un crade qui laisse ses déchets à côté de la poubelle.")
        enemi = "Rien"