def affichage_liste(liste: list[int]):
    print(*liste)

def affichage_liste_colonne(liste: list[int]):
    no_idx_to_show: str = '   '.join(str(x) for x in range(len(liste)))
    val_list_to_show: str = ' | '.join(str(x) for x in liste)
    print(f'Indices :   {no_idx_to_show}')
    print(f'Valeurs : [ {val_list_to_show} ]')

def multiple_liste(liste: list[int]):
    print(*[x*3 for x in liste])

def plus_petit_chiffre(liste: list[int]):
    min_no: int = 999999
    for no in liste:
        if no < min_no:
            min_no = no
    print(f"Plus petit chiffre : {min_no}")

def somme_impair(liste: list[int]):
    total: int = sum([x if x % 2 == 0 else 0 for x in liste])
    print(f"Somme impair = {total}")

def affichage_separateur():
    print("------------------")
