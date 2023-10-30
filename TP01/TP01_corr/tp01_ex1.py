"""
Programme permettant de convertir une quantité en plusieurs unités d'énergie.
Unités : joule, calorie, Ft-lb et eV
  Données : Une valeur et une unité
  Indications:
        Selon l'unité entrée par l'utilisateur, afficher la conversion
        dans les 3 autres unités.
  Résultats : Affichage des conversions
"""

### Déclaration et initialisation des variables
FT_LB: float = 0.738
CAL: float = 0.239
EV: float = 6.24 * (10 ** 18)

affichage: str = "\nValeur en entrée : "
res_j: float = 0.0
res_ft_lb: float = 0.0
res_cal: float = 0.0
res_ev: float = 0.0


#Inputs
valeur_energie: float = float(input("Quantité d'énergie à convertir: "))
unite: str = input("Unité (J, ft-lb, cal ou eV)")


### Séquences . d'opération

# Conversion d'unité selon l'unité d'entrée
if unite == "J":  #Conversion à partir de J
    res_j = valeur_energie
    res_ft_lb = valeur_energie * FT_LB
    res_cal = valeur_energie * CAL
    res_ev = valeur_energie * EV
    affichage += str(res_j) + " "+ unite +" \n" \
                + "---------Conversion-----------\n"+ "en ft-lb : " + str(res_ft_lb)\
                + " ft-lb \n" + "en calories : " + str(res_cal)\
                + " cal \n"+"en eV : " + str(res_ev) + " eV \n"
elif unite == "ft-lb": #Conversion à partir de ft-lb
    res_j = valeur_energie / FT_LB
    res_ft_lb = valeur_energie
    res_cal = res_j * CAL
    res_ev = res_j * EV
    affichage += str(res_ft_lb) + " "+ unite +" \n" \
                + "---------Conversion-----------\n"+ "en joule : " + str(res_j)\
                + " J \n" + "en calories : " + str(res_cal) \
                +" cal \n"+"en eV : " + str(res_ev) + " eV \n"
elif unite == "cal": #Conversion à partir de cal
    res_j = valeur_energie / CAL
    res_ft_lb = res_j * FT_LB
    res_cal = valeur_energie
    res_ev = res_j * EV
    affichage += str(res_cal) + " "+ unite +" \n" \
                + "---------Conversion-----------\n"+ "en joule : " + str(res_j) + " J \n"\
                + "en ft-lb : " + str(res_ft_lb) + " ft-lb \n" \
                + "en eV : " + str(res_ev) + " eV \n"
elif unite == "eV": #Conversion à partir de eV
    res_j = valeur_energie / EV
    res_ft_lb = res_j * FT_LB
    res_cal = res_j * CAL
    res_ev = valeur_energie
    affichage += str(res_ev) + " "+ unite +" \n" \
                + "---------Conversion-----------\n"+ "en joule : " + str(res_j) +  " J \n"\
                +"en ft-lb : " + str(res_ft_lb) + " ft-lb \n" \
                + "en calories : " + str(res_cal) + " cal \n"

#Affichage
print(affichage)
