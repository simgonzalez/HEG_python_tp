"""
algo: demande à l'utilisateur de saisir un chiffre entre 5-10
donnée: chiffre saisi par l'utilisateur
"""
# déclaration
chiffre_saisi_utilisateur: int

# init
chiffre_saisi_utilisateur = 0

# logique
# forcer l'utilisateur à saisir un chiffre entre 1 et 10
while not (5 <= chiffre_saisi_utilisateur <= 10):
    chiffre_saisi_utilisateur = int(input("saisissez un chiffre entre 5-10: "))
