import random
import tkinter as tk
from PIL import Image, ImageTk

# État de la partie
paquet = []
main_joueur = []
main_croupier = []
partie_terminee = True
message = "Bienvenue ! Cliquez sur Nouvelle Manche pour commencer."

carte = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# Initiales correspondant à tes fichiers .gif (c, h, d, s)
couleurs_dict = {"Trefle": "c", "Coeur": "h", "Caraux": "d", "Piques": "s"}

def creer_paquet():
    nouveau_paquet = []
    for couleur in couleurs_dict:
        for rang in carte:
            nouveau_paquet.append((rang, couleur))
    random.shuffle(nouveau_paquet)
    return nouveau_paquet

def tirer_carte(p):
    return p.pop()

def calculer_score(main):
    total = 0
    as_count = 0
    for c in main:
        rang = c[0]
        if rang in ["J", "Q", "K"]:
            total += 10
        elif rang == "A":
            as_count += 1
            total += 11
        else:
            total += int(rang)
    
    while total > 21 and as_count > 0:
        total -= 10
        as_count -= 1
    return total

def on_tirer():
    global partie_terminee, message
    if partie_terminee: return
    
    main_joueur.append(tirer_carte(paquet))
    if calculer_score(main_joueur) > 21:
        partie_terminee = True
        message = "Bust ! Le croupier gagne."
    rafraichir_ui()

def on_rester():
    global partie_terminee, message
    if partie_terminee: return
    
    while calculer_score(main_croupier) < 17:
        main_croupier.append(tirer_carte(paquet))
    
    partie_terminee = True
    s_joueur = calculer_score(main_joueur)
    s_croupier = calculer_score(main_croupier)
    
    if s_croupier > 21 or s_joueur > s_croupier:
        message = "Bravo, vous avez gagné !"
    elif s_croupier > s_joueur:
        message = "Le croupier gagne."
    else:
        message = "Égalité !"
    rafraichir_ui()

def jouer_manche():
    global paquet, main_joueur, main_croupier, partie_terminee, message
    paquet = creer_paquet()
    main_joueur = [tirer_carte(paquet), tirer_carte(paquet)]
    main_croupier = [tirer_carte(paquet), tirer_carte(paquet)]
    partie_terminee = False
    message = "Tirer ou Rester ?"
    rafraichir_ui()

# --- PARTIE GRAPHIQUE ---

images_cartes = {}

def charger_toutes_les_images():
    """Charge les 52 images en mémoire une seule fois"""
    for rang in carte:
        for nom_long, initiale in couleurs_dict.items():
            nom_fichier = f"images/{rang}{initiale}.gif"
            try:
                img = Image.open(nom_fichier)
                images_cartes[f"{rang}_{nom_long}"] = ImageTk.PhotoImage(img)
            except:
                print(f"Erreur : Image {nom_fichier} introuvable.")

def rafraichir_ui():
    # Affichage Joueur
    canvas_joueur.delete("all")
    for i, c in enumerate(main_joueur):
        cle = f"{c[0]}_{c[1]}"
        canvas_joueur.create_image(50 + (i * 40), 60, image=images_cartes[cle])
    label_mainjoueur.config(text=f"Score Joueur: {calculer_score(main_joueur)}")

    # Affichage Croupier
    canvas_croupier.delete("all")
    for i, c in enumerate(main_croupier):
        if i == 0 and not partie_terminee:
            # Dessine un rectangle gris si la carte est cachée
            canvas_croupier.create_rectangle(15, 10, 85, 110, fill="blue", outline="white")
            canvas_croupier.create_text(50, 60, text="?", fill="white", font=("Arial", 20, "bold"))
        else:
            cle = f"{c[0]}_{c[1]}"
            canvas_croupier.create_image(50 + (i * 40), 60, image=images_cartes[cle])
    
    score_c_txt = calculer_score(main_croupier) if partie_terminee else "?"
    label_maincroupier.config(text=f"Score Croupier: {score_c_txt}")
    label_message.config(text=message)

    etat = "disabled" if partie_terminee else "normal"
    bouton_tirer.config(state=etat)
    bouton_rester.config(state=etat)

app = tk.Tk()
app.title("BlackJack Deluxe")
app.geometry("500x700")
app.configure(bg="darkgreen")

# Chargement des images dès le début
charger_toutes_les_images()

# Interface
tk.Label(app, text="BLACKJACK", font=("Arial", 24, "bold"), bg="darkgreen", fg="gold").pack(pady=10)

tk.Label(app, text="Main du Croupier", bg="darkgreen", fg="white").pack()
canvas_croupier = tk.Canvas(app, width=350, height=130, bg="forestgreen", highlightthickness=0)
canvas_croupier.pack()
label_maincroupier = tk.Label(app, text="", font=("Arial", 12), bg="darkgreen", fg="white")
label_maincroupier.pack()

tk.Label(app, text="Votre Main", bg="darkgreen", fg="white").pack(pady=(20, 0))
canvas_joueur = tk.Canvas(app, width=350, height=130, bg="forestgreen", highlightthickness=0)
canvas_joueur.pack()
label_mainjoueur = tk.Label(app, text="", font=("Arial", 12), bg="darkgreen", fg="white")
label_mainjoueur.pack()

label_message = tk.Label(app, text=message, font=("Arial", 14, "italic"), bg="darkgreen", fg="white")
label_message.pack(pady=20)

# Boutons
cadre_boutons = tk.Frame(app, bg="darkgreen")
cadre_boutons.pack(pady=10)

tk.Button(cadre_boutons, text="Nouvelle Manche", command=jouer_manche, width=15).grid(row=0, column=0, columnspan=2, pady=5)
bouton_tirer = tk.Button(cadre_boutons, text="Tirer", command=on_tirer, width=7, state="disabled")
bouton_tirer.grid(row=1, column=0, padx=5)
bouton_rester = tk.Button(cadre_boutons, text="Rester", command=on_rester, width=7, state="disabled")
bouton_rester.grid(row=1, column=1, padx=5)




app.mainloop()