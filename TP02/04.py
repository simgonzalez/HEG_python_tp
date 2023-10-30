# déclaration
CARBURANT_MAX_APPAREIL: float = 199158
CONSOMMATION_RYTHME_CROISIERE: float = 1340.78
AUGMENTATION_CONSO_PERSONNE: float = 0.001724
ACTION_FAIRE_LE_PLEIN: float = 0
distance_a_parcourir_user: float = 0
carburant_restant: float = 0
carburant_nécessaire: float = 0
nb_voyageur: int = 0
total_distance_parcourue: float = 0

# initialisation
carburant_restant = CARBURANT_MAX_APPAREIL

# tant qu'il y a assez de carburant on vole ou on fait le plein
while carburant_restant >= 0:
    distance_a_parcourir_user = float(input("Entrez la distance de votre destination (en km) ou entrez 0 pour faire le plein : "))
    # Si l'utilisateur décide de faire le pleins on remet au max le réservoir
    if distance_a_parcourir_user == ACTION_FAIRE_LE_PLEIN:
        carburant_restant = CARBURANT_MAX_APPAREIL
        print("Le réservoir est rempli entièrement")
    # Sinon on demande le nombre de voyageur et on calcul le carburant nécessaire
    else:
        nb_voyageur = int(input("Combien de personnes font parties du voyage ? "))
        # le carburant nécessaire dépend du nombre de voyageur et de la distance à parcourir
        carburant_nécessaire = (distance_a_parcourir_user / 100) *\
                               (CONSOMMATION_RYTHME_CROISIERE * (1 + nb_voyageur * AUGMENTATION_CONSO_PERSONNE))
        # on effectue le trajet
        carburant_restant -= carburant_nécessaire
        # Si on a pu faire le trajet on indique le carburant restant, sinon on dit que le trajet est impossible
        if carburant_restant >= 0:
            total_distance_parcourue += distance_a_parcourir_user
            print(f"Il vous reste encore {carburant_restant:.2f} litres de carburant")
        else:
            print("Vol impossible ! Vol interdit par manque de carburant !")
print(f"Vous avez parcouru {total_distance_parcourue:.2f} km")
