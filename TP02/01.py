NORMAL_CHAR: chr = 'X'
ALT_CHAR: chr = 'O'

chiffre_impair_user: int = int(input("entrez un chiffre impair :"))

for row in range(chiffre_impair_user):
    for col in range(chiffre_impair_user):
        if row == col or (row == chiffre_impair_user - (col+1)):
            print(ALT_CHAR, end='')
        else:
            print(NORMAL_CHAR, end='')
    print()