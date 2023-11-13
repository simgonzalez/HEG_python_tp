from math import pi

def calc_perimetre_cercle(_r: float) -> float:
    """
    Calcul et retourne le périmètre du cercle en fonction du rayon en entrée
    @param _r: float -> Rayon du cercle dont on veut calculer le périmètre
    @return: float -> le périmètre du cercle
    """
    return 2 * pi * _r


r: float = float(input("Entrez le rayon du cercle: "))
print(f"Le périmètre du cercle est : {calc_perimetre_cercle(r):.2f}")
