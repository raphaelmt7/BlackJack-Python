import random

carte = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
couleurs = ["Piques", "Coeur", "Caraux", "Trefle"]

def creer_paquet():
    paquet = []
    for couleur in couleurs:
        for rang in carte:
            paquet.append((rang, couleur))  # tuple (rang, couleur)
    random.shuffle(paquet)
    return paquet

def tirer_carte(paquet):
    element = paquet.pop()
    return element

def calculer_score(main):
    total = 0
    for carte in main:
        rang = carte[0]
        if rang == "J" or rang == "Q" or rang == "K":
            total = total + 10
        elif rang == "A":
            if total + 11 > 21:
                total = total + 1
        else :
            total = total + int(rang)
    return total

def afficher_main(nom, main, cacher_premiere=False):
    print(f"{nom} :")
    if cacher_premiere:
        print("Carte cachée")
        for i in range(1, len(main)):
            rang, couleur = main[i]
            print(f"{rang} de {couleur}")
    else:
        for rang, couleur in main:
            print(f"{rang} de {couleur}")



def tour_joueur(paquet, main_joueur, main_croupier):
    tirage = True
    while tirage == True:
        if calculer_score(main_joueur) > 21:
            break
        else:
            afficher_main("Joueur",main_joueur)
            afficher_main("Croupier",main_croupier, True)
            
            clavier = input("tirer ou rester ?")
            if clavier == "tirer":
                main_joueur.append(tirer_carte(paquet))
            elif clavier == "rester":
                break
            else: 
             print("Erreur ")
    
        
def tour_croupier(paquet, main_croupier):
    while calculer_score(main_croupier) < 17:
        main_croupier.append(tirer_carte(paquet))

def determiner_gagnant(score_joueur, score_croupier):
    if score_croupier > 21:
        return "joueur"
    elif score_croupier > score_joueur:
        return "croupier"
    elif score_joueur > 21:
        return "croupier"
    elif score_croupier == score_joueur:
        return "egalité"
    elif score_joueur > score_croupier:
        return "joueur"
    
def jouer_manche():
    paquet = []
    main_croupier = []
    main_joueur = []

    paquet = creer_paquet()

    main_croupier.append(tirer_carte(paquet))
    main_joueur.append(tirer_carte(paquet))
    main_croupier.append(tirer_carte(paquet))
    main_joueur.append(tirer_carte(paquet))

    tour_joueur(paquet, main_joueur, main_croupier)
    tour_croupier(paquet, main_croupier)

    gagnant = determiner_gagnant(calculer_score(main_joueur), calculer_score(main_croupier))

    print("le gagnant est le : ",gagnant)


# main
jouer_manche()
