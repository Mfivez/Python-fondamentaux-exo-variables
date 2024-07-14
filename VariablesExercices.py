
# 1. Création des variables
age = 25
nom = "Alice"
prix = 19.99

# 2. Affichage des types et des valeurs de Variables
print("### Affichage des Types et des Valeurs de Variables ###")
print("Type de age:", type(age))
print("Type de nom:", type(nom))
print("Type de prix:", type(prix), end="\n\n")

print("Valeur de age:", age)
print("Valeur de nom:", nom)
print("Valeur de prix:", prix, end="\n\n")

# 3. Affichage des références mémoire avant modification
print("### Affichage des Références Mémoire avant Modification ###")
print("Référence mémoire de age avant modification:", id(age))
print("Référence mémoire de nom avant modification:", id(nom))
print("Référence mémoire de prix avant modification:", id(prix), end="\n\n")

# Modification des variables
age = 26
nom = "Bob"
prix = 29.99

# 4. Affichage des nouveaux types et valeurs
print("### Affichage des Nouveaux Types et Valeurs ###")
print("Nouveau type de age:", type(age))
print("Nouvelle valeur de age:", age, end="\n\n")
print("Nouveau type de nom:", type(nom))
print("Nouvelle valeur de nom:", nom, end="\n\n")
print("Nouveau type de prix:", type(prix))
print("Nouvelle valeur de prix:", prix, end="\n\n")

