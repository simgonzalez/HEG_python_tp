"""
Normes de programmation à respecter : Modules 63-11

Andi RAMIQI
"""

# -----------------------------------
# Déclaration, typage, initialisation des variables
# -----------------------------------

# Le but du typage vous permettra de mieux comprendre l'utilité de vos variables
# Gestion des espaces : Mettre des espace autour d’un opérateur arithmétique et
# mettre un espace après le « : » (pas avant)

# Constantes : lorsqu'une variable ne changera pas dans la suite du code : MAJUSCULES
COURS:str = "Programmation"
MODULE:int = 6311

# Variables...
nom: str = "John"  # une chaîne de caractères
age: int = 25  # un nombre entier
taille: float = 1.80  # un nombre à virgule flottante

# Utilisation des variables
# Utiliser des espaces autour des opérateurs.
result = age + 5

# -----------------------------------
# Nom des variables explicite
# -----------------------------------

# Il est préférable d'utiliser des noms de variables explicites pour une meilleure compréhension.
# Nom identificateur aussi explicite que possible
# Comporte des lettres [a...z,A...Z,_] et des chiffres [0...9]
# Commence impérativement par une lettre ou _
# La casse est importante !
# utiliser un underscore "_" à la place des espaces si la variables est composé de plusieures mots
user_first_name = "Alice"
user_last_name = "Smith"

# Mauvais exemple : x1, y2b, n

# -----------------------------------
# Inputs : Données d'entrées par un utilisateur
# -----------------------------------
# Pour obtenir une entrée utilisateur, on utilise la fonction input() qui renvoie une chaine de caractères.
# Toujours typer les inputs selon le type retourné
# Vous pouvez initialiser et déclarer la variable en une ligne

# Exemple de base pour obtenir une entrée utilisateur :
input_nom:str = input("Veuillez entrer un nom : ")
print(input_nom)
# Exemple de base pour obtenir une entrée utilisateur d'un autre type:
input_age:int = int(input("Veuillez entrer un age : "))
print(input_age)

# -----------------------------------
# Commenter son code
# -----------------------------------

# Les commentaires sont utilisés pour expliquer le code pour les futurs lecteurs.
# Il est bon de bien commenter, surtout lors de la création de fonctions ou de classes.

# 1. Commentaires de ligne unique
# Utilisez un dièse (#) suivi d'un espace pour les commentaires de ligne unique.

# Cette variable stocke le nom de l'utilisateur
username = "Alice"

# 2. Commentaires multi-lignes
# Pour les commentaires qui s'étendent sur plusieurs lignes,
# vous pouvez utiliser plusieurs dièses (#) à la suite.

# Cette variable stocke l'adresse e-mail de l'utilisateur.
# Il est important de noter que l'adresse e-mail doit être valide
# et que l'utilisateur doit avoir accès à cette adresse.
user_email = "alice@example.com"

# 3. Commentaires pour séparer les sections
# Utilisez des commentaires pour séparer différentes sections de votre code,
# ce qui rendra votre code plus organisé et plus facile à lire.

# --------------- Section 1 ---------------
# ...

# --------------- Section 2 ---------------
# ...

# 4. Blocs de commentaires avec triples guillemets
"""
Les triples guillemets peuvent être utilisés pour des commentaires multi-lignes. 
C'est généralement utilisé pour des docstrings, mais il est aussi possible 
de les utiliser pour des grands commentaires. 
"""

# 5. évitez les commentaires évidents
# Au lieu de commenter chaque ligne, commentez uniquement les parties du code
# qui pourraient être complexes ou qui nécessitent une explication.

# Mauvais :
x = 5  # Assigne 5 à x
y = 10 # Assigne 10 à y
calculation_result = x + y # Additionne x et y

# Bon :
calculation_result = x + y  # Additionne les valeurs de x et y


