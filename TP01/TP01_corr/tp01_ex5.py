"""
Programme de calcul du prix d'un billet de transport journalier selon plusieurs rabais possibles.
    Prix normal d'un billet : 10chf
    Rabais étudiant : 2chf
    Rabais demi-tarif : 5chf
    Rabais groupe : 2 chf par billet acheté à partir de 4.
    Carte mensuelle : Billet gratuit

Indications :
    - Il est possible de bénéficier d'un rabais demi-tarif et étudiant
    - Le rabais groupe n’est cumulable avec aucun autre rabais
    - Il est possible d'avoir une carte mensuelle permettant d’avoir ce billet gratuitement

Contrainte : 
- Si la personne possède la carte mensuelle, il ne faut pas lui demander
d'autres informations.

"""
### Déclaration et Initialisation des variables
rabais_etudiant:int = 0
rabais_demi_tarif:int = 0
rabais_groupe :int = 0
prix:int = 0

rabais_etudiant = 2
rabais_demi_tarif = 5
rabais_groupe  = 2
prix = 10


### Séquence d'opération
carte_mensuelle:str = input("Possédez-vous la carte mensuelle ? (oui ou non)")

if carte_mensuelle == "non":
    demi_tarif:str = input("Possédez-vous la carte demi-tarif ? (oui ou non)")
    carte_etudiant:str = input("Possédez-vous la carte étudiante ? (oui ou non)")
    if demi_tarif == "oui":
        prix -= rabais_demi_tarif
    if carte_etudiant == "oui" :
        prix -= rabais_etudiant
    if carte_etudiant == "non" and demi_tarif == "non":
        groupe:int = int(input("Combien de billets voulez-vous ?"))
        if groupe >= 4:
            prix = (prix-rabais_groupe)*groupe
        else:
            prix *=groupe
else:
    prix = 0

#Affichage
print("Le prix à payer est : " + str(prix) + "CHF")
