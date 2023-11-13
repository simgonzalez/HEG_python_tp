def divider_of_int(_number_to_find_divider: int) -> str:
    """
    cherche et retourne les diviseurs d'un nombre passer en paramètre
    @param _number_to_find_divider: int -> nombre dont on souhaite connaitre les diviseurs
    @return: str -> diviseur du nombre entré en param
    """
    divider: str = ""
    divider_count: int = 0
    for i in range(1,_number_to_find_divider + 1):
        if _number_to_find_divider % i == 0:
            divider += f"{i}\n"
            divider_count += 1
    return f"{divider}Il y a {divider_count} diviseur"

