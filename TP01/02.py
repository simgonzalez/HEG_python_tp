DRINKS_MAPPING: dict = {
    "Fanta orange": 2.9,
    "Coca cola": 2.9,
    "Coca cola light": 2.7,
    "Henniez": 2.3,
    "Ice Tea": 2.2,
    "Limonade": 1.9
}
print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
for idx, drink in enumerate(DRINKS_MAPPING.keys()):
    print(f"{idx + 1}. {drink}")
monnaie_client: float = float(input("Veuillez introduire votre monnaie : "))
boisson_voulue: int = int(input("Veuillez sélectionner un produit : "))
boisson_voulue -= 1
price_drink_wanted: float = list(DRINKS_MAPPING.values())[boisson_voulue]
monnaie_client -= price_drink_wanted
if monnaie_client < 0\
        or boisson_voulue > len(DRINKS_MAPPING):
    print("Produit inconnu ou monnaie insuffisante")
    quit()
elif monnaie_client > 0:
    print(f"Monnaie à rendre {monnaie_client}")
print(f"{list(DRINKS_MAPPING.keys())[boisson_voulue]} servi ! Santé !")
