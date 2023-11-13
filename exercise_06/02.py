def compare_float(_f1: float, _f2: float):
    """
    Fonction qui compare deux float et qui indique lequel est plus petit
    en cas d'égalité indique qu'ils sont semblable
    @param _f1: float -> chiffre à comparé
    @param _f2: float -> deuxième chiffre à comparé
    """
    if _f1 < _f2:
        return _f1
    elif _f2 < _f1:
        return _f2
    else:
        return False



no1: float = float(input("Saisir un 1er nombre : "))
no2: float = float(input("Saisir un 2ème nombre : "))

min_val: float = compare_float(no1, no2)
if min_val:
    print(f"{min_val} est la plus petite valeure")
else:
    print("Les deux valeures sont les mêmes")