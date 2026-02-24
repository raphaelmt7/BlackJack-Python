import random
import tkinter as tk

# Etat de la partie (partagé entre les callbacks Tkinter)
paquet = []
main_joueur = []
main_croupier = []
partie_terminee = True
message = "Bienvenue pour commencer cliquez sur nouvelle manche !"


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

def on_tirer():
    global partie_terminee, message

    if partie_terminee:
        return

    main_joueur.append(tirer_carte(paquet))
    score = calculer_score(main_joueur)

    if score > 21:
        partie_terminee = True
        message = "Bust ! Le croupier gagne."
    else:
        message =  "tirer ou rester."

    rafraichir_ui()

def on_rester():
    global partie_terminee, message

    if partie_terminee:
        return
    
    tour_croupier(paquet, main_croupier)

    partie_terminee = True
    gagnant = determiner_gagnant(calculer_score(main_joueur), calculer_score(main_croupier))

    if gagnant == "croupier":
        message = "Bust ! Le croupier gagne."
    elif gagnant == "joueur":
        message = "Bravo vous avez gagner !"
    elif gagnant == "egalité":
        message = "egalite......."
    
    rafraichir_ui()

    
        
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
    global paquet, main_joueur, main_croupier, partie_terminee, message
    main_joueur = []
    main_croupier = []
    partie_terminee = False

    message = ""


    paquet = creer_paquet()

    main_croupier.append(tirer_carte(paquet))
    main_joueur.append(tirer_carte(paquet))
    main_croupier.append(tirer_carte(paquet))
    main_joueur.append(tirer_carte(paquet))

    message =  "tirer ou rester."

    rafraichir_ui()

def formater_main(main):
    return " | ".join([f"{rang} de {couleur}" for rang, couleur in main])

def rafraichir_ui():
    # Main + score joueur
    texte_joueur = f"Joueur: {formater_main(main_joueur)}\nScore: {calculer_score(main_joueur)}"
    label_mainjoueur.config(text=texte_joueur)

    # Main + score croupier (carte cachée si partie non finie)
    if partie_terminee:
        texte_croupier = f"Croupier: {formater_main(main_croupier)}\nScore: {calculer_score(main_croupier)}"
    else:
        if len(main_croupier) > 0:
            visible = " | ".join([f"{r} de {c}" for r, c in main_croupier[1:]])
            texte_croupier = f"Croupier: [Carte cachée]"
            if visible:
                texte_croupier += f" | {visible}"
        else:
            texte_croupier = "Croupier: -"
    label_maincroupier.config(text=texte_croupier)

    # Message état
    label_message.config(text=message)


    # Activer/désactiver boutons
    etat = "disabled" if partie_terminee else "normal"
    bouton_tirer.config(state=etat)
    bouton_rester.config(state=etat)





# Création de la fenêtre
app = tk.Tk()
app.title("BlackJack")
app.geometry("600x600")

# Création des éléments
titre = tk.Label(app, text="BlackJack", font=("Arial", 20))
label_message= tk.Label(app, text="", font=("Arial", 24, "bold"))
label_mainjoueur = tk.Label(app, text="", font=("Arial", 24, "bold"))
label_maincroupier = tk.Label(app, text="", font=("Arial", 24, "bold"))
bouton_manche = tk.Button(app, text="nouvelle manche", command=jouer_manche)
bouton_tirer = tk.Button(app, text="tirer", command=on_tirer)
bouton_rester = tk.Button(app, text="rester", command=on_rester)

# Placement (Layout)
titre.pack(pady=10)
bouton_manche.pack(pady=10)
label_message.pack(pady=10)
label_maincroupier.pack(pady=10)
label_mainjoueur.pack(pady=10)
bouton_tirer.pack(pady=5)
bouton_rester.pack(pady=10, padx=5)

# Lancement
app.mainloop()






