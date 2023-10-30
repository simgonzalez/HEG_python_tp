"""
Programme calculant le niveau de risque cardiovasculaire. 
  Données : - L'Age de l'utilisateur
            - Le sexe de l'utilisateur
            - Si l'utilisateur est un fumeur ou non
            - Si l'utilisateur pratique du sport
            - Si l’utilisateur possède une alimentation trop sucrée
  Indications :
            - Si l'utilisateur est fumeur, le niveau de risque augmente de 2
            - Si l'utilisateur fait du sport, le niveau de risque diminue de 1
            - Si l'utilisateur est un homme de plus de 50 ans,
              le niveau de risque augmente de 1
            - Si l'utilisateur est une femme de plus de 60ans,
              le niveau de risque augmente de 1
            - Si l’utilisateur consomme trop de sucre, le niveau de risque augmente de 2
            
  Résultats : Un message spécifiant le niveau de risque obtenu.
            - Si le niveau de risque est inférieur ou égal à 1, le niveau de risque est faible.
            - Si le niveau de risque est de 2 à 3, le niveau de risque est élevé
            - Sinon il est très élevé.

"""
### Déclaration et initialisation des variables
niveau_risque: int = 0


# Entrées utilisateur
fumeur: str = input("Êtes-vous fumeur ? (oui ou non)")
sport: str = input("Faîtes-vous du sport ? (oui ou non)")
sexe: str = input("Quel est votre sexe ? (h ou f)")
age: int = int(input("Quel est votre age ?"))
sucre: str = input("Consommez-vous beaucoup d'aliments sucrés ? (oui ou non)")

### Séquence d'opération

# Tests selon les entrées utilisateurs. Modification du niveau de risque total.
if fumeur == "oui":
    niveau_risque +=2
if sport == "oui":
    niveau_risque -=1
if sexe == "h" and age > 50:
    niveau_risque +=1
if sexe == "f" and age > 60:
    niveau_risque +=1
if sucre == "oui":
    niveau_risque += 2

#Affichage
#Catégorisation selon le niveau de risque total    
if niveau_risque <= 1:
    print("Le niveau de risque est faible("+str(niveau_risque)+")")
elif niveau_risque <= 3:
    print("Le niveau de risque est élevé("+str(niveau_risque)+")")
else:
    print("Le niveau de risque est très élevé("+str(niveau_risque)+")")


