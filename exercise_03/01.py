ANNEE_ESCALADE: int = 1602
annee_escalade_user:int = 0

while annee_escalade_user != ANNEE_ESCALADE:
    annee_escalade_user: int = int(input("En quelle année à eu lieu l'escalade ?"))
    if annee_escalade_user == ANNEE_ESCALADE:
        print("C'est la bonne réponse")
    elif ANNEE_ESCALADE - 5 <= annee_escalade_user <= ANNEE_ESCALADE + 5:
        print("C'est presque ca")
    else:
        print("Non c'est faux")
