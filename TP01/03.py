# récupère les informations du patient
smoke: str = input(f"Êtes-vous fumeur ? (oui ou non) ")
sport: str = input(f"Faîtes-vous du sport ? (oui ou non) ")
gender: str = input(f"Quel est votre sexe ? (h ou f) ")
age: int = int(input(f"Quel est votre âge ? "))
sweet: str = input(f"Consommez-vous veaucoup d'aliments sucrés ? (oui ou non) ")

# calcul du niveau de risque cardio vasculaire
risk_count: int = 0
# les fumeurs ont plus de risques
if smoke.lower() == "oui":
    risk_count += 2
# la pratique régulière d'une activité sportive réduit les risques
if sport.lower() == "oui":
    risk_count -= 1
# un homme de plus de 50 ans à plus de risque
# une femme de plus de 60 ans à plus de risque
if age > 50:
    if gender.lower() == "h":
        risk_count += 1
    elif gender.lower() == "f" and age > 60:
        risk_count += 1
# manger sucrés favorises les maladies cardiovasculaires
if sweet.lower() == "oui":
    risk_count += 2

# affichage du niveau de risque
print(f"Le niveau de risque {'faible' if risk_count <= 1 else 'élevé' if 3 > risk_count > 1 else 'très élevé'} ({risk_count})")