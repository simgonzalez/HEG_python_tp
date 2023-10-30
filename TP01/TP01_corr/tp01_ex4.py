"""
Programme testant si une date, saisie par l'utilisateur, est valide ou non.
Données : Une date saisie par l'utilisateur
Indications:
        Pour pouvoir déterminer si une année est bissextile :       
        	- Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
        	- Si elle est multiple de 4, on regarde si elle est multiple de 100.
            	   - Si c'est le cas, on regarde si elle est multiple de 400.
      		        - Si c'est le cas, l'année est bissextile.
                        - Sinon, elle n'est pas bissextile.
                   - Sinon, elle est bissextile.

Résultats : Un message spécifiant si la date entrée est valide.

"""

### Déclaration et initialisation des variables

bissextile: bool = False
valide: bool = True

# Entrées utilisateur
jour: int = int(input("Saisissez un jour : "))
mois: int = int(input("Saisissez un mois : "))
annee: int = int(input("Saisissez une année : "))

### Séquence d'opération

#Test validité jour et mois
if (jour < 1 or jour > 31) or (mois < 1 or mois > 12) :
    valide = False
else:# Ici on sait que le jour est entre 1 et 31 inclus et le mois entre 1 et 12 inclus 
    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0): #Test bissextile
        bissextile = True
    if jour == 31 and (mois == 2 or mois == 4 or mois == 6 or mois == 9 or mois == 11):
        valide = False
    elif jour > 28 and mois == 2 :
        valide = False
        if jour == 29 and bissextile:
            valide = True      

#Affichage
if valide:
    print("Cette date est valide.")
else:
    print("Cette date n'est pas valide.")
        
