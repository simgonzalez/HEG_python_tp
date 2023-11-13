from phare import hauteur_parcourue

no_marche: int = int(input("Combien de marches ? : "))
hauteur_marche: float = float(input("hauteur d'une marche (cm) ? "))

print(f"Pour {no_marche} marches de {hauteur_marche}cm, il parcourt {hauteur_parcourue(no_marche, hauteur_marche):.2f} m par semaine !")