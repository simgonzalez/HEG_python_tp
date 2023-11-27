from random import randint


def reverse_word(phrase_utilisateur: str) -> list[str]:
    """

    @param phrase_utilisateur:
    @return:
    """
    mots: list[str] = phrase_utilisateur.split(' ')
    for idx_mot in range(len(mots) - 1, -1, -1):
        print(mots[idx_mot], end=" ")
    return mots


def randomize_words(mots):
    while len(mots) > 0:
        print(mots.pop(randint(0, len(mots) - 1)), end=" ")


def reverse_word_letter(phrase_utilisateur):
    for idx_char in range(len(phrase_utilisateur) - 1, -1, -1):
        print(phrase_utilisateur[idx_char], end="")


def main():
    phrase_utilisateur: str = input("Saisir une phrase")
    reverse_word_letter(phrase_utilisateur)
    print()
    mots = reverse_word(phrase_utilisateur)
    print()
    randomize_words(mots)


if __name__ == "__main__":
    main()