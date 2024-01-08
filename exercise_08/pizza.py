
def afficher_pizza(pizza: dict):
    for element in pizza:
        print(f"{element} : {pizza[element]} frs")

def pizza_interval_prix(menu: list[dict]):
    prix_min: int = int(input("Quelle est le prix minimum de la pizza ?"))
    prix_max: int = int(input("Quelle est le prix maximal de la pizza ?"))
    pizza_affichee: bool = False
    for pizza in menu:
        for element in pizza:
            if prix_min <= pizza[element] <= prix_max:
                pizza_affichee = True
                afficher_pizza(pizza)
    if not pizza_affichee:
        print("Il n'y a aucune pizza dans cette tranche de prix")

def afficher_prix_pizza(menu: list[dict]):
    pizza_prix_to_know: str = input("Pour quelle pizza souhaitez vous connaitre le prix ? ").lower()
    for pizza in menu:
        if pizza_prix_to_know in pizza:
            for element in pizza:
                print(f"Le prix de la pizza {pizza_prix_to_know} est de {pizza[element]}")
                return 0

def commander_pizza(menu: list[dict]):
    liste_pizza_voulue: list[str] = input("Saisissez la liste des pizza souhaitée: ").lower().split(";")
    is_commande_possible: bool = True
    for pizza_name in liste_pizza_voulue:
        is_commande_possible = pizza_disponible(menu, pizza_name)
    if is_commande_possible:
        total_commande: int = 0
        for pizza in menu:
            for element in pizza:
                if element in liste_pizza_voulue:
                    total_commande += pizza[element]
        print(f"le total de votre commande s'eleve à {total_commande} frs")
    else:
        print("Commande impossible une des pizza demandée n'est pas disponible")

def pizza_existe(menu: list[dict]):
    pizza_exist: str = input("Quel est le nom de la pizza recherché ? ").lower()
    if pizza_disponible(menu, pizza_exist):
        print(f"La pizza {pizza_exist} est disponible.")
    else:
        print("La pizza {pizza_exist} n'est pas dans votre pizzeria")

def pizza_disponible(menu: list[dict], pizza_souhaitee: str):
    for pizza in menu:
        if pizza_souhaitee in pizza:
            return True
    return False
