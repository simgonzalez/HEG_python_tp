ACTION_FIN: str = "fin"
cholesterol_saisie: str = ""
total_valeur_cholesterol: str = ""
moyenne_taux_choleseterol: float = 0
resultat_traitement_necessaire: str = ""

while cholesterol_saisie.lower() != ACTION_FIN:
    cholesterol_saisie = input("Entrez votre taux de cholestérol : ")

    if 1 <= float(cholesterol_saisie) <= 7:
        total_valeur_cholesterol += cholesterol_saisie + ';'
    elif cholesterol_saisie != ACTION_FIN:
        print("Le taux de cholestérol doit être compris entre 1 et 7 mmol/L !")

moyenne_taux_choleseterol = round(sum([float(val_chol)]for val_chol in total_valeur_cholesterol.split(
    ';')) / len(total_valeur_cholesterol.split(';')))
print(
    f"La moyenne des taux dfe cholestérol est de {moyenne_taux_choleseterol:.1f}")
if moyenne_taux_choleseterol < 5.7:
    resultat_traitement_necessaire = "Le patient doit suivre un traitement anti-cholestérol"
else:
    resultat_traitement_necessaire = "Le patient n'a pas besoin de traitement"
print(resultat_traitement_necessaire)
