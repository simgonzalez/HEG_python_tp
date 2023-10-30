"""
Programme de cryptage
Données : phrase utilisateur, mot utilisateur
Résultat : intercalle une lettre du mot entre chaque caractere de la phrase
"""
# Déclaration
phrase_a_chiffrer: str = ""
mot_pour_chiffrer: str = ""
phrase_chiffree: str = ""
count_char_mot_chiffrage: int = 0

# Initialisation
phrase_a_chiffrer = input("Saisir la phrase à chiffrer : ")
mot_pour_chiffrer = input("Saisir le mot de chiffrage : ")

# Chiffrement de la phrase à l'aide du mot
for char in phrase_a_chiffrer:
    # On veut que le compteur se repete s'il atteint la taille maximale du mot de chiffrage
    if count_char_mot_chiffrage >= len(mot_pour_chiffrer):
        count_char_mot_chiffrage = 0
    # On ajoute le caractere de la phrase et un caractere du mot de chiffrage
    phrase_chiffree += char + mot_pour_chiffrer[count_char_mot_chiffrage]
    count_char_mot_chiffrage += 1
print(f"La phrase cryptée est : {phrase_chiffree}")
