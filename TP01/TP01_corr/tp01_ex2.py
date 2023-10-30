"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Fanta orange à 2.90
           - Coca cola à 2.90
           - Coca cola light à 2.70
           - Henniez à 2.30
           - Ice Tea à 2.20
           - Limonade à 1.90
           
 Résultats : - Un message d’annulation de la transaction
                 (« Produit inconnu / Monnaie insuffisante »)
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant "santé"

"""

###Déclaration et initialisation des variables

FANTA_ORANGE:float = 2.90
COCA_COLA:float = 2.90
COCA_COLA_LIGHT:float = 2.70
HENNIEZ:float = 3.30
ICE_TEA:float = 2.20
LIMONADE:float = 1.90

montant:float = 0.0
selection:int = 0

### Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Fanta Orange")
print("2. Coca cola")
print("3. Coca cola light")
print("4. Henniez")
print("5. Ice tea")
print("6. Limonade")

# Entrées utilisateur
montant = float(input("Veuillez introduire votre monnaie :"))
selection = int(input("Veuillez sélectionner un produit :"))

# Test pour chaque produit s'il existe et si le montant est suffisant
if selection == 1 and montant >= FANTA_ORANGE:
    if montant != FANTA_ORANGE:
        print(f"Monnaie à rendre : {round(montant - FANTA_ORANGE, 2)}")
    print("Fanta Orange servi ! Santé !")
elif selection == 2 and montant >= COCA_COLA:
    if montant != COCA_COLA:
        print("Monnaie à rendre : " + str(round(montant - COCA_COLA, 2)))
    print("Coca cola servi ! Santé !")
elif selection == 3 and montant >= COCA_COLA_LIGHT:
    if montant != COCA_COLA_LIGHT:
        print("Monnaie à rendre : {}".format(round(montant - COCA_COLA_LIGHT, 2)))
    print("Coca cola light servi ! Santé !")
elif selection == 4 and montant >= HENNIEZ:
    if montant != HENNIEZ:
        print("Monnaie à rendre : %.2f" % round(montant - HENNIEZ, 2))
    print("Henniez servi ! Santé !")
elif selection == 5 and montant >= ICE_TEA:
    if montant != ICE_TEA:
        print("Monnaie à rendre : ", round(montant - ICE_TEA, 2))
    print("Ice tea servi ! Santé !")
elif selection == 6 and montant >= LIMONADE:
    if montant != LIMONADE:
        print("Monnaie à rendre : " + str(round(montant - LIMONADE, 2)))
    print("Limonade servie ! Santé !")
else:
    print("Produit inconnu ou monnaie insuffisante")

