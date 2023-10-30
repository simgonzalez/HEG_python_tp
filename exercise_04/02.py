"""
Programme qui calcul le montant total d'un panier de course
"""
# Déclaration et initialisation
TAUX_TVA: float = 1.08  # 1 fois et 8% le prix de l'article
ACTION_STOP: int = 0
prix_article_utilisateur: float = -1
no_article_actuel: int = 0
total_panier_utilisateur: float = 0
etat: str = "er"

while prix_article_utilisateur != ACTION_STOP:
    no_article_actuel += 1
    if no_article_actuel > 1:
        etat = "ème"
    # Demande à l'utilisateur le prix de l'article et l'ajoute au montant total avec la TVA
    prix_article_utilisateur = float(input(f"Quel est le prix du {no_article_actuel}{etat} article ? (0 pour terminer) : "))
    total_panier_utilisateur += prix_article_utilisateur * TAUX_TVA
print(f"Vous avez acheté {no_article_actuel} et vous devez payer {round(total_panier_utilisateur,2):.2f} CHF")