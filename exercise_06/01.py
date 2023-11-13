def compare_float(_f1: float, _f2: float):
    """
    Fonction qui compare deux float et qui indique lequel est plus petit
    en cas d'égalité indique qu'ils sont semblable
    @param _f1: float -> chiffre à comparé
    @param _f2: float -> deuxième chiffre à comparé
    """
    min_no: float = False
    if _f1 < _f2:
        min_no = _f1
    elif _f2 < _f1:
        min_no = _f2
    else:
        pass

    if min_no:
        print(f"{min_no} est le plus petit des 2 nombres")
    else:
        print("Ces 2 nombres sont égaux")


no1: float = float(input("Saisir un 1er nombre : "))
no2: float = float(input("Saisir un 2ème nombre : "))

compare_float(no1, no2)
