def hauteur_parcourue(_nb_marche: int, _hauteur_marche: float = 10.5) -> float:
    """
    calcul le nombre de mètre parcouru par semaine sachant que le gardien de phare
    va au toilettes cinq fois par jour
    @param _nb_marche: int -> nombre de marche
    @param _hauteur_marche: float -> hauteur des marches
    @return: float -> distance parcourue en mètre
    """
    NB_TRAJETS_JOUR: int = 10
    return _nb_marche * _hauteur_marche/100 * NB_TRAJETS_JOUR * 7
