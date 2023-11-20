from random import randint


def main():
    phrase_utilisateur: str = input("Saisir une phrase")
    for idx_char in range(len(phrase_utilisateur)-1, -1, -1):
        print(phrase_utilisateur[idx_char],end="")
    print()
    mots: list[str] = phrase_utilisateur.split(' ')
    for idx_mot in range(len(mots)-1, -1, -1):
        print(mots[idx_mot], end=" ")
    print()
    while len(mots) > 0:
        print(mots.pop(randint(0, len(mots) - 1)), end=" ")


if __name__ == "__main__":
    main()