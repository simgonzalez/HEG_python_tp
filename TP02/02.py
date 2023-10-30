""" Définir en quelle année la population zombie dépasse la population humaine
    L'utilisateur défini la tailles des populations de départ.
    Afficher l'évolution chaque année
"""

# Déclaration
POURCENTAGE_CONVERSION_ZOMBIE: float = 20
POURCENTAGE_DIMINUTION_ZOMBIE: float = 20
POURCENTAGE_AUGMENTATION_HUMAIN: float = 1
nb_habitant: int = 0
nb_zombie: int = 0
nb_conversion_zombie: int = 0
nb_zombie_dead: int = 0
nb_habitant_plus: int = 0
current_year: int = 0


# Initialisation
current_year = 2017
nb_habitant = int(input("Saisissez un nombre d'habitant : "))
nb_zombie = int(input("Saisissez un nombre de zombies : "))

# Algo
while nb_habitant >= nb_zombie:
    # Calcul population
    current_year += 1
    # Augmentation des habitants
    nb_habitant_plus = int(nb_habitant * (POURCENTAGE_AUGMENTATION_HUMAIN / 100))
    nb_habitant += nb_habitant_plus
    # Conversion des zombies avec diminutions des habitant
    nb_conversion_zombie = int(nb_habitant * (POURCENTAGE_CONVERSION_ZOMBIE / 100))
    nb_habitant -= nb_conversion_zombie
    nb_zombie += nb_conversion_zombie
    # Zombie tué par les humains
    nb_zombie_dead = int(nb_zombie * (POURCENTAGE_DIMINUTION_ZOMBIE / 100))
    nb_zombie -= nb_zombie_dead

    # Affichage changement de population
    print(f"--------{current_year}--------")
    print(f"  - nb habitants : {nb_habitant}")
    print(f"  - nb zombies : {nb_zombie}")
    print(f"  - nb zombies tués : {nb_zombie_dead}")
    print(f"  - augmentation habitants : {nb_habitant_plus}", end="\n\n")
print(f"Durant l'année {current_year}, il y aura {nb_zombie} zombies et {nb_habitant} habitants.")