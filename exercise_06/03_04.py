from math_perso import divider_of_int

no_to_find_divider: int = False
while no_to_find_divider < 1:
    no_to_find_divider = int(input("Saisir un nombre entier (plus grand que 1) : "))

print(f"Les diviseurs de {no_to_find_divider} sont :\n{divider_of_int(no_to_find_divider)}")