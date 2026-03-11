# 🃏 Blackjack Python GUI

Bienvenue dans **BlackJack App** : une application de Blackjack développée en Python avec Tkinter !  
Une interface simple, efficace et visuelle pour jouer au Blackjack contre un croupier automatisé.

## 🌐 Badges
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

---

## 🎯 Fonctionnalités principales

- **Interface Graphique Tkinter** : Une fenêtre de jeu interactive avec des zones dédiées pour le joueur et le croupier.
- **Affichage dynamique des cartes** : Les cartes s'affichent sous forme d'images (.gif) lors du tirage.
- **Logique de jeu complète** :
    - Gestion d'un paquet de 52 cartes avec mélange aléatoire.
    - Calcul automatique des scores en temps réel.
    - Gestion intelligente de l'**As** (valeur 11 ou 1 selon le score total).
- **Règles du Casino** : 
    - Le croupier s'arrête obligatoirement à 17 ("Dealer stands on 17").
    - Détection automatique des victoires, des égalités et des dépassements (Bust).

---

## 🚀 Installation et Lancement

1. **Prérequis** :
   Assurez-vous d'avoir Python installé. Ce projet nécessite également la bibliothèque `Pillow` pour l'affichage des images.
   ```bash
   pip install Pillow
