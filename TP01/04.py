jour_saisie: int = int(input("Saisissez un jour : "))
mois_saisie: int = int(input("Saisissez un mois : "))
annee_saisie: int = int(input("Saisissez une année : "))

is_year_bissextile: bool = False
# si l'année saisie n'est pas multiple de 4 elle n'est pas bissextile
if annee_saisie[:-2] % 4 != 0:
    if annee_saisie % 100  == 0:
        if annee_saisie % 400 == 0:
            is_year_bissextile = True
        else:
            is_year_bissextile = False
    else:
        is_year_bissextile = True
# affichage de la validité ou non de la date
if is_year_bissextile:
    print("Cette date est valide.")
else:
    print("Cette date n'est pas valide.")
