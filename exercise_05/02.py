import random

nb_essai: int = 0

chiffre_a_deviner: int = random.randint(1, 100)
chiffre_utilisateur: int = 0

while nb_essai < 5 and chiffre_utilisateur != chiffre_a_deviner:
    chiffre_utilisateur = int(input("Deviner le chiffre entre 1 et 100 "))
    if chiffre_utilisateur < chiffre_a_deviner:
        print("Plus grand")
    elif chiffre_utilisateur > chiffre_a_deviner:
        print("Plus petit")
    nb_essai += 1

if nb_essai == 5 and chiffre_utilisateur != chiffre_a_deviner:
    print("Vous avez perdu")
