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
    for i in main:
        if main [i] == "J" or main [i] == "Q" or main [i] == "K":
            total + 10
        elif main [i] == "A":
            if total + 11 > 21:
                total - 10
        else :
            total + main [i]
    return total

def afficher_main(nom, main, cacher_premiere=False):
    print(nom," :")
    if cacher_premiere == True:
        print("Premiere carte caché !")
        for i in range(1, len(main)):
            print (main[i])
    else:
        for i in main:
            print (main[i])


def tour_joueur(paquet, main_joueur, main_croupier):
    while tirage == True:
        print("Voici votre main :", afficher_main("Joueur",main_joueur))
        clavier = input("tirer ou rester ?")
        if clavier == "tirer":
            main_joueur.append(tirer_carte(paquet))
        elif clavier == "rester":
            break
        else: 
            print("Erreur ")









        








# main
paquet = creer_paquet()

for c in paquet:
    print(c)

print(len(paquet))

tirage = tirer_carte(paquet)

print(tirage)
