import random

#Initialisation
lance_1:int = 0
lance_2:int = 0
lance_3:int = 0
score_utilisateur: int = 0

#Algo
while score_utilisateur < 200:
    no_utilisateur_garde: int = -1
    input("Appuyer sur \"Enter\" pour lancer les dés ")
    for i in range(3):
        for j in range(1,4):
            exec(f"lance_{j} = random.randint(1,6) if lance_{j} != {no_utilisateur_garde} else {no_utilisateur_garde}")
            print(f"|{eval(f'lance_{j}')}| ", end="")
        print()
        if i < 2:
            no_utilisateur_garde = int(input("Voulez-vous garder une valeure ? (1-6) "))
        else:
            if lance_1 == lance_2 == lance_3:
                if lance_1 == 1:
                    score_utilisateur += 100
                elif lance_1 == 6:
                    score_utilisateur += 60
                else:
                    score_utilisateur += lance_1
            print(f"Votre score est : {score_utilisateur} pts")