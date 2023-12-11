"""
Exercise de matrice. 
Demander à l'utilisateur de saisir les valeurs d'une matrice puis calculer le total par ligne dans une autre liste
"""


def user_matrix(row: int = 2, col: int = 2) -> list[list[int]]:
    """_summary_

    Keyword Arguments:
        row -- nombre de lignes dans la matrice (default: {2})
        col -- nombre de colonnes dans la matrice (default: {2})

    Returns:
        _description_
    """
    matrix: list[list] = []
    for i in range(row):
        matrix.append([])
        for _ in range(col):
            matrix[i].append(int(input("Saisissez un nombre entier : ")))
    return matrix


def sum_row_matrix(matrix_to_sum_row: list[list[int]]) -> list[int]:
    """Calcule et retourne la somme des lignes de la matrice

    Arguments:
        matrix_to_sum_row -- matrice dont on veut sommer chaque ligne

    Returns:
        list of sum of each row
    """
    list_sum: list[int] = []
    sum_row: int = None
    for idx, row in enumerate(matrix_to_sum_row):
        sum_row = 0
        for val in row:
            sum_row += val
        list_sum.append(sum_row)
    return list_sum


def sum_col_matrix(matrix_to_sum_col: list[list[int]]) -> list[int]:
    """fonction qui somme les colonnes d'une matrice

    Arguments:
        matrice_to_sum_col -- matrice dont on veut sommer les colonnes

    Returns:
        retourne une liste de sommes
    """
    list_sum: list[int] = []
    sum_col: int = None
    for idx in range(len(matrix_to_sum_col[0])):
        sum_col = 0
        for val in matrix_to_sum_col:
            sum_col += val[idx]
        list_sum.append(sum_col)
    return list_sum


def show_col_value(matrix_to_print_col: list[list]):
    """show the value column by column

    Arguments:
        matrix_to_print_col -- matrix that we will print value of
    """
    for idx in range(len(matrix_to_print_col[0])):
        for col in matrix_to_print_col:
            print(col[idx])


def main():
    usr_matrix: list[list[int]] = user_matrix(2)
    print(*sum_row_matrix(usr_matrix))
    print("\n")
    print(show_col_value(usr_matrix))
    print("\n\nCol results: ")
    print(*sum_col_matrix(usr_matrix))


if __name__ == "__main__":
    main()
