UNITE_CONVERSION_MAPPING: dict = {
    "J": 1,
    "ft-lb": 0.738,
    "cal": 0.239,
    "eV": 6.24 * 10 ** 18
}


def demande_saisie() -> (int, str):
    """
    Demande à l'utilisateur de saisir une quantité et une unité parmi celles dans la liste fournie entre parenthèse
    @return: quantité d'energie saisie: int, unite_saisie: str
    """
    unite_saisie = False
    quantite_energie_saisie: int = int(input("Quantité d'énergie à convertir:"))
    while unite_saisie not in UNITE_CONVERSION_MAPPING.keys():
        unite_saisie: str = input(f"Unité ({UNITE_CONVERSION_MAPPING.keys()}")
    return quantite_energie_saisie, unite_saisie


def conversion(qty, unite_original, unite_final) -> str:
    """
    Convertie la quantité fourni dans l'unité désirée
    @param: qty: int, quantité à convertir
    @param: unite_original: str, unite de départ de la quantité fournie
    @param: unite_final: str, unite dans laquelle la valeure doit être convertie
    @return: str valeur convertie avec l'unite à la fin
    """
    val_orig_unit = UNITE_CONVERSION_MAPPING.get(unite_original,1)
    val_final_unit = UNITE_CONVERSION_MAPPING.get(unite_final)
    return str((qty / val_orig_unit) * val_final_unit) + " " + unite_final


quantite_energie, unite_saisie = demande_saisie()
print(f"Valeur en entrée : {str(quantite_energie)} {unite_saisie}")
print("---------Conversion----------")
for u in UNITE_CONVERSION_MAPPING.keys():
    print(f"en {u} : {conversion(quantite_energie, unite_saisie, u)}")
