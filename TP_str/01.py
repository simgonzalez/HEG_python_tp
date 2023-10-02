"""
Programme qui affiche une variable contenant mon nom prénom.

"""


# 1. Création et affichage d'une chaine de caractères
nom_prenom: str = "Simon Gonzalez"
print(nom_prenom)

# 2. Affichage de la longueur d'une str
longueur_nom_prenom: int =  len(nom_prenom)
print(longueur_nom_prenom)

# 3. Premier caractère d'une str
premier_char: str = nom_prenom[:1]
dernier_char: str = nom_prenom[-1:]
print(premier_char)
print(dernier_char)

# 4. lower and upper case convertion
uc_nom_prenom: str = nom_prenom.upper()
lc_nom_prenom: str = nom_prenom.lower()
print(uc_nom_prenom)
print(lc_nom_prenom)

# 5. string into int and int into string
int_into_str: str = str(10)
str_into_int: int = int(int_into_str)
print(f"{int_into_str} : {type(int_into_str)}")
print(f"{str_into_int} : {type(str_into_int)}")

# 6. format() method to inster float and int
print("myStr with float {} and int {}".format(10.2, 5))

# 7. f string to insert var with int and float
int_to_show: int = 1039452
float_to_show: float = 1294.3124890
print(f"myStr with float {float_to_show} and int {int_to_show}")

# 8. reverse str
print("Python"[::-1])


# 9. check palindrome
def test_palindrom(potential_palindrom: str):
    """ Test if a string is a palindrom if it is it will print the result

    @param potential_palindrom: string that we want to test
    """
    if potential_palindrome == potential_palindrome[::-1]:
        print("Votre string est un palindrome \n{} \n{}".format(potential_palindrom, potential_palindrom[::-1]))
    else:
        print("Votre string n'est pas un palindrome \n{} \n{}".format(potential_palindrom, potential_palindrom[::-1]))


print("----------------Test de palindrome---------------")
potential_palindrome: str = input("insérer une chaine de charactère : ")
test_palindrom(potential_palindrome)

# 10. count word in a string
phrase: str = "ma phrase contient 5 mots"
print(len(phrase.split(" ")))
