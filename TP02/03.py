# Délclaration
INDICE_SOMME_TROIS_CODE: int = 12
INDICE_CENTAINE_DIZAINE_DIVISIBLE: int = 3
INDICE_CODE_DIVISIBLE: int = 78
current_combinaison: int = 0
nb_code_un: int = -1
nb_code_deux: int = -1
nb_code_trois: int = -1

# algo
for possible_un in range(10):
    # Chiffre des centaine doit être divisible par 3
    if possible_un % 3 == 0:
        for possible_deux in range(10):
            # Chiffre des dizaines doit aussi être divisible par 3
            if possible_deux % 3 == 0:
                for possible_trois in range(10):
                    # La somem des chiffres doit être egal au nombre de signe du zodiac
                    if possible_trois + possible_deux + possible_un == INDICE_SOMME_TROIS_CODE:
                        # Recomposition de la combinaison
                        current_combinaison = int(str(possible_un) + str(possible_deux) + str(possible_trois))
                        if current_combinaison % 78 == 0:
                            nb_code_un = possible_un
                            nb_code_deux = possible_deux
                            nb_code_trois = possible_trois

print(f"Combinaison: {nb_code_un} {nb_code_deux} {nb_code_trois}")
