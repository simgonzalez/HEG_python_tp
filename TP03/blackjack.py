from random import randint


def jeu():
    """
    - le jeu se déroule en 2 phases :
    - Phase 1 : le joueur lance un nombre de dés dépendant du nombre séléctionné par l'utilisateur
    - Phase 2 : l'ordinateur lance un nombre de dés dépendant de son score
    """
    BLACKJACK_OBJECTIF: int = 21
    score_joueur: int = jeu_joueur(0, BLACKJACK_OBJECTIF)
    old_score_joueur: int = -1
    score_ordianteur: int = jeu_ordinateur(0, BLACKJACK_OBJECTIF)

    while score_joueur != old_score_joueur or score_joueur > BLACKJACK_OBJECTIF or score_ordianteur <= 18:
        if old_score_joueur != score_joueur and score_joueur <= BLACKJACK_OBJECTIF:
            old_score_joueur = score_joueur
            score_joueur = jeu_joueur(score_joueur, BLACKJACK_OBJECTIF)
        if score_ordianteur <= 18:
            score_ordianteur += jeu_ordinateur(score_ordianteur, BLACKJACK_OBJECTIF)

    affichage_resultat(score_joueur, score_ordianteur, BLACKJACK_OBJECTIF)


def jeu_joueur(score_joueur: int, objectif: int = 21) -> int:
    """
    lance un nombre de dés dépendant du nombre séléctionné par l'utilisateur
    @param score_joueur: int -> score du joueur
    @param objectif: int -> score à atteindre
    @return: int -> nouveau score du joueur
    """
    no_de: int = int(input("Combien de dés souhaitez-vous lancer ? "))
    for i in range(no_de):
        score_joueur += randint(1, 6)
    print(f"Votre score est de {score_joueur}\n")
    return score_joueur


def jeu_ordinateur(score_ordinateur: int, objectif: int = 21) -> int:
    """
    - Voici le détail sur la stratégie de jeu de l’ordinateur :
    - Si la somme de l'ordinateur est inférieure à 6, il demande 3 dés
    - Si la somme de l'ordinateur est supérieure ou égale à 6 et inférieure à 12, il demande 2 dés
    - Si la somme de l'ordinateur est supérieure ou égale à 12 et inférieure à 18, il demande 1 dés
    - Si la somme de l'ordinateur est supérieure ou égale à 18, il s'arrête de jouer
    @param score_ordinateur:
    @param objectif:
    @return:
    """
    chiffre_aleatoire: int = randint(1, 6)
    if chiffre_aleatoire*3 < 6:
        score_ordinateur += chiffre_aleatoire*3
        print("L'ordinateur choisi trois dés")
    elif chiffre_aleatoire*2 >= 6 and chiffre_aleatoire*2 < 12:
        score_ordinateur += chiffre_aleatoire*2
        print("L'ordinateur choisi deux dés")
    else:
        score_ordinateur += chiffre_aleatoire
        print("L'ordinateur choisi un dé")
    print(f"Le score de l'ordinateur est de {score_ordinateur}\n")
    return score_ordinateur


def affichage_resultat(score_joueur: int, score_ordinateur: int, objectif: int = 21) -> None:
    if score_joueur > objectif and score_ordinateur > objectif:
        print(f"Vous avez perd car vous avez dépassé {objectif} ({score_joueur})")
        print(f"L'ordinateur a également dépassé {objectif} ({score_ordinateur})")
    elif score_joueur > score_ordinateur and score_joueur > objectif and score_ordinateur <= objectif:
        print(f"Vous avez perdu ({score_joueur}) contre l'ordinateur ({score_ordinateur})")
    elif score_joueur > score_ordinateur:
        print(f"Vous avez gagné ({score_ordinateur}) contre l'ordinateur ({score_ordinateur})")
    elif score_joueur == score_ordinateur:
        print(f"égalité ! pas de gagnant ! ({score_joueur})")