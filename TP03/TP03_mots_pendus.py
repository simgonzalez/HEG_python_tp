import random


def affichage_mot_cache(mot_cache: str, lettre_tiree: list, erreures_restantes: int):
    """
    La fonction affichage_mot_cache qui prends en paramètres le mot
    caché, les lettres déjà tirées et le nombre d’erreurs restant
    i. Cette fonction affichera le mot caché et les lettres déjà trouvées sous
    la forme vu ci-dessus
    ii. Elle affichera également le nombre d’erreurs restantes (voir exemple
    de sortie)
    @return:
    """
    print(f"                        ({erreures_restantes})")
    for lettre in mot_cache:
        if lettre in lettre_tiree:
            print(lettre, end=" ")
        else:
            print("_", end=" ")


def tirage_lettre(lettre_tiree: list) -> str:
    """

    @param lettre_tiree:
    @return:
    """
    lettre: str = False
    while not lettre:
        lettre = input("Veuillez entrer une lettre : ")
        if lettre in lettre_tiree:
            print("Vous avez déjà tiré cette lettre")
            lettre = False
    return lettre_tiree.append(lettre)


def verification_mot(mot: str, lettre_tiree: list) -> bool:
    """
    La fonction verification_mot qui prends en paramètres le mot caché et
    les lettres déjà tirées. Cette fonction vérifiera si le mot est trouvé ou
    non
    @param mot: str -> mot à trouver
    @param lettre_tiree: list -> liste des lettres tirées
    @return: bool -> True si le mot est trouvé, False sinon
    """
    for lettre in mot:
        if lettre not in lettre_tiree:
            return False
    return True


def diminuer_erreurs(erreures_restantes: int) -> int:
    return erreures_restantes - 1


def tirer_mot()-> str:
    tab_mots = ['bleu', 'super', 'autre', 'bizarre', 'difficile', 'drole', 'etrange', 'facile', 'grave', 'impossible',
                'jeune', 'juste', 'libre', 'malade', 'meme', 'pauvre', 'possible', 'propre', 'rouge', 'sale', 'simple',
                'tranquille', 'triste', 'vide', 'bonne', 'toute', 'doux', 'FAUX', 'francais', 'gros', 'heureux',
                'mauvais', 'serieux', 'vieux', 'VRAI', 'ancien', 'beau', 'blanc', 'certain', 'chaud', 'cher', 'clair',
                'content', 'dernier', 'desole', 'different', 'droit', 'entier', 'fort', 'froid', 'gentil', 'grand',
                'haut', 'humain', 'important', 'joli', 'leger', 'long', 'meilleur', 'mort', 'noir', 'nouveau', 'pareil',
                'petit', 'plein', 'premier', 'pret', 'prochain', 'quoi', 'seul', 'tout', 'vert', 'vivant', 'aide',
                'chef', 'enfant', 'garde', 'gauche', 'geste', 'gosse', 'livre', 'merci', 'mort', 'ombre', 'part',
                'poche', 'professeur', 'tour', 'fois', 'madame', 'paix', 'voix', 'affaire', 'annee', 'arme', 'armee',
                'attention', 'balle', 'boite', 'bouche', 'carte', 'cause', 'chambre', 'chance', 'chose', 'classe',
                'confiance', 'couleur', 'cour', 'cuisine', 'dame', 'dent', 'droite', 'ecole', 'eglise', 'envie',
                'epaule', 'epoque', 'equipe', 'erreur', 'espece', 'face', 'facon', 'faim', 'famille', 'faute', 'femme',
                'fenetre', 'fete', 'fille', 'fleur', 'force', 'forme', 'guerre', 'gueule', 'habitude', 'heure',
                'histoire', 'idee', 'image', 'impression', 'jambe', 'joie', 'journee', 'langue', 'lettre', 'levre',
                'ligne', 'lumiere', 'main', 'maison', 'maman', 'maniere', 'marche', 'mere', 'minute', 'musique', 'nuit',
                'odeur', 'oreille', 'parole', 'partie', 'peau', 'peine', 'pensee', 'personne', 'peur', 'photo', 'piece',
                'pierre', 'place', 'police', 'porte', 'presence', 'prison', 'putain', 'question', 'raison', 'reponse',
                'robe', 'route', 'salle', 'scene', 'seconde', 'securite', 'semaine', 'situation', 'soeur', 'soiree',
                'sorte', 'suite', 'table', 'terre', 'tete', 'verite', 'ville', 'voiture', 'avis', 'bois', 'bras',
                'choix', 'corps', 'cours', 'gars', 'mois', 'pays', 'prix', 'propos', 'sens', 'temps', 'travers',
                'vieux', 'accord', 'agent', 'amour', 'appel', 'arbre', 'argent', 'avenir', 'avion', 'bateau', 'bebe',
                'besoin', 'bonheur', 'bonjour', 'bord', 'boulot', 'bout', 'bruit', 'bureau', 'cafe', 'camp',
                'capitaine', 'chat', 'chemin', 'cheri', 'cheval', 'cheveu', 'chien', 'ciel', 'client', 'coeur', 'coin',
                'colonel', 'compte', 'copain', 'cote', 'coup', 'courant', 'debut', 'depart', 'dieu', 'docteur', 'doigt',
                'dollar', 'doute', 'droit', 'effet', 'endroit', 'ennemi', 'escalier', 'esprit', 'etat', 'etre',
                'exemple', 'fait', 'film', 'flic', 'fond', 'francais', 'frere', 'front', 'garcon', 'general', 'genre',
                'gout', 'gouvernement', 'grand', 'groupe', 'haut', 'homme', 'honneur', 'hotel', 'instant', 'interet',
                'interieur', 'jardin', 'jour', 'journal', 'lieu', 'long', 'maitre', 'mari', 'mariage', 'matin',
                'medecin', 'metre', 'milieu', 'million', 'moment', 'monde', 'monsieur', 'mouvement', 'moyen', 'noir',
                'nouveau', 'numero', 'oeil', 'oiseau', 'oncle', 'ordre', 'papa', 'papier', 'parent', 'passage', 'passe',
                'patron', 'pere', 'petit', 'peuple', 'pied', 'plaisir', 'plan', 'point', 'pouvoir', 'premier',
                'present', 'president', 'prince', 'probleme', 'quartier', 'rapport', 'regard', 'reste', 'retard',
                'retour', 'reve', 'revoir', 'salut', 'sang', 'secret', 'seigneur', 'sentiment', 'service', 'seul',
                'siecle', 'signe', 'silence', 'soir', 'soldat', 'soleil', 'sourire', 'souvenir', 'sujet', 'telephone',
                'tout', 'train', 'travail', 'trou', 'truc', 'type', 'vent', 'ventre', 'verre', 'village', 'visage',
                'voyage', 'fils', 'gens', 'abandonner', 'accepter', 'accompagner', 'acheter', 'adorer', 'agir', 'aider',
                'aimer', 'ajouter', 'aller', 'amener', 'amuser', 'annoncer', 'apercevoir', 'apparaitre', 'appeler',
                'apporter', 'apprendre', 'approcher', 'arranger', 'arreter', 'arriver', 'asseoir', 'assurer',
                'attaquer', 'atteindre', 'attendre', 'avancer', 'avoir', 'baisser', 'battre', 'boire', 'bouger',
                'bruler', 'cacher', 'calmer', 'casser', 'cesser', 'changer', 'chanter', 'charger', 'chercher',
                'choisir', 'commencer', 'comprendre', 'compter', 'conduire', 'connaitre', 'continuer',
                'couper', 'courir', 'couvrir', 'craindre', 'crier', 'croire', 'danser', 'decider', 'decouvrir',
                'degager', 'demander', 'descendre', 'desoler', 'detester', 'detruire', 'devenir', 'deviner', 'devoir',
                'dire', 'disparaitre', 'donner', 'dormir', 'echapper', 'ecouter', 'ecrire', 'eloigner', 'embrasser',
                'emmener', 'empecher', 'emporter', 'enlever', 'entendre', 'entrer', 'envoyer', 'esperer', 'essayer',
                'etre', 'eviter', 'excuser', 'exister', 'expliquer', 'faire', 'falloir', 'fermer', 'filer', 'finir',
                'frapper', 'gagner', 'garder', 'glisser', 'habiter', 'ignorer', 'imaginer', 'importer',
                'inquieter', 'installer', 'interesser', 'inviter', 'jeter', 'jouer', 'jurer', 'lacher', 'laisser',
                'lancer', 'lever', 'lire', 'maintenir', 'manger', 'manquer', 'marcher', 'marier', 'mener', 'mentir',
                'mettre', 'monter', 'montrer', 'mourir', 'naitre', 'obliger', 'occuper', 'offrir', 'oser', 'oublier',
                'ouvrir', 'paraitre', 'parler', 'partir', 'passer', 'payer', 'penser', 'perdre', 'permettre', 'plaire',
                'pleurer', 'porter', 'poser', 'pousser', 'pouvoir', 'preferer', 'prendre', 'preparer', 'presenter',
                'prevenir', 'prier', 'promettre', 'proposer', 'proteger', 'quitter', 'raconter', 'ramener', 'rappeler',
                'recevoir', 'reconnaitre', 'reflechir', 'refuser', 'regarder', 'rejoindre', 'remarquer', 'remettre',
                'remonter', 'rencontrer', 'rendre', 'rentrer', 'repeter', 'repondre', 'reposer', 'reprendre',
                'ressembler', 'rester', 'retenir', 'retirer', 'retourner', 'retrouver', 'reussir', 'reveiller',
                'revenir', 'rever', 'revoir', 'rire', 'risquer', 'rouler', 'sauter', 'sauver', 'savoir', 'sembler',
                'sentir', 'separer', 'serrer', 'servir', 'sortir', 'souffrir', 'sourire', 'souvenir', 'suffire',
                'suivre', 'taire', 'tendre', 'tenir', 'tenter', 'terminer', 'tirer', 'tomber', 'toucher', 'tourner',
                'trainer', 'traiter', 'travailler', 'traverser', 'tromper', 'trouver', 'tuer', 'utiliser', 'valoir',
                'vendre', 'venir', 'vivre', 'voir', 'voler', 'vouloir']
    return tab_mots[random.randint(0,len(tab_mots))]
