from TP03_mots_pendus import *


### Déclaration et Initialisation des variables

MOT: str = tirer_mot()


#Programme Principal
if __name__ == "__main__":
    lettre_tiree: list = []
    erreures_restantes: int = 10
    while erreures_restantes > 0 and not verification_mot(MOT, lettre_tiree):
        affichage_mot_cache(MOT, lettre_tiree, erreures_restantes)
        tirage_lettre(lettre_tiree)
        if lettre_tiree[-1] not in MOT:
            erreures_restantes = diminuer_erreurs(erreures_restantes)
    if verification_mot(MOT, lettre_tiree):
        print("Vous avez gagné")
