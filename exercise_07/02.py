def main():
    chiffres_utilisateur: list = input ("Saisisez une liste de chiffre")
    str_to_add = "OK"
    if len(chiffres_utilisateur) > 5:
        str_to_add = "Trop long"
    liste_final: list = [chiffre for chiffre in chiffres_utilisateur[:5]]
    liste_final.append(str_to_add)
    print(*liste_final)


if __name__ == "__main__":
    main()