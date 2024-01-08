from pizza import *

MENU_PIZZERIA: list[dict] = [{"calzone": 16}, {"funghi": 15}, {"picante": 17}, {"hawaii": 16}, {"margherita": 12}, {"napoli": 14}]
ACTION_MENU: str = "Menu de l'application :\n    1. Afficher le prix d'une pizza\n    2. Afficher le pizza pour un budget"\
                   "\n    3. Demander si une pizza est diponible\n    4. Commander une ou plusieurs pizzas"
MAPPING_ACTION_MENU: dict = {1: afficher_prix_pizza, 2: pizza_interval_prix, 3: pizza_existe, 4: commander_pizza}

def main():
    action_utilisateur: int = 0
    while action_utilisateur != 4:
        print(ACTION_MENU)
        action_utilisateur = int(input("Quel est votre choix ? "))
        if action_utilisateur in MAPPING_ACTION_MENU.keys():
            action: function = MAPPING_ACTION_MENU.get(int(action_utilisateur))
            action(MENU_PIZZERIA)


if __name__ == '__main__':
    main()
