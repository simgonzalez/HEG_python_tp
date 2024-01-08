from module01 import *

def main():
    liste: list[int] = [8, 2, 4, 6, 9, 1, 3]
    affichage_liste(liste)
    affichage_separateur()
    affichage_liste_colonne(liste)
    affichage_separateur()
    multiple_liste(liste)
    affichage_separateur()
    plus_petit_chiffre(liste)
    affichage_separateur()
    somme_impair(liste)
    affichage_separateur()

if __name__ == '__main__':
    main()
