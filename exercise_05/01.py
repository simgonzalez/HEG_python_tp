# Déclaration
CAPITALE_SUISSE: str = "Bern"
NOMBRE_HB_SUISSE: int = 133115
pays: str = "Suisse"
nb_habitant: int = 0
capitale: str = 0
is_capitale_bern: bool = False

# Initialisation
capitale = str(input(f"Quelle est la capitale de la {pays}"))
nb_habitant = int(input("Quel est le nombre d'habitants de cette capitale ? : "))
is_capitale_bern = capitale == CAPITALE_SUISSE

if is_capitale_bern:
    print("C'est la bonne capitale")
    if nb_habitant == NOMBRE_HB_SUISSE:
        print("c'est le bon nombre hb")
    else:
        print("c'est pas le bon nombre hb")
else:
    print("Ce n'est pas la bonne capitale")

