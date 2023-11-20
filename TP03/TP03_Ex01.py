"""
TP03 exo 1
"""
liste_carre_nombre: list[int] = []
nombre_utilisateur: str = False

while int(nombre_utilisateur) <= 10:
    nombre_utilisateur = input("Veuillez entrer un nombre plus grand que 10 : ")

somme_chiffre: int = int(nombre_utilisateur)
while somme_chiffre > 10:
    for chiffre in str(somme_chiffre):
        carre_chiffre: int = int(chiffre) ** 2
        print(f"{chiffre}^2= {carre_chiffre}")
        liste_carre_nombre.append(carre_chiffre)

    somme_chiffre = sum(liste_carre_nombre)
    print(f"Nouveau nombre : {'+'.join(str(x) for x in liste_carre_nombre)}={somme_chiffre}")
    liste_carre_nombre.clear()

if somme_chiffre == 1:
    print(f"Le nombre {nombre_utilisateur} est un nombre porte bonheur !")
else:
    print(f"Le nombre {nombre_utilisateur} n'est pas un nombre porte bonheur !")
