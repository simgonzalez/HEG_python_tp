"""
Exercise de matrice. 
Demander à l'utilisateur de saisir les valeurs d'une matrice puis calculer le total par ligne dans une autre liste
"""


def user_matrice(row: int = 2, col: int = 2) -> list[list[int]]:
    """
    Créé et retourne une matrice de size x col entrée par l'utilisateur

    Returns:
        Matrice de 2 par 2 saisie par l'utilisateur
    """
    matrice: list[list] = []
    for i in range(row):
        matrice.append([])
        for _ in range(col):
            matrice[i].append(int(input("Saisissez un nombre entier : ")))
    return matrice


def sum_row_matrice(matrice_to_sum_row: list[int]) -> list[int]:
    """
    Calcule et retourne la somme des lignes de la matrice

    Returns:
       list of sum of each row
    """
    list_sum: list[int] = []
    sum_row: int = None
    for idx, row in enumerate(matrice_to_sum_row):
        sum_row = 0
        for val in row:
            sum_row += val
        list_sum.append(sum_row)
    return list_sum


def main():
    print(*sum_row_matrice(user_matrice(2)))


if __name__ == "__main__":
    main()
