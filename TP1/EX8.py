# Initialiser les listes pour stocker les notes et les coefficients avec des éléments vides
notes = [0] * 4
coefficients = [0] * 4

# Saisir les notes et les coefficients au clavier
for i in range(4):
    notes[i] = float(input(f"Entrez la note {i + 1} : "))
    coefficients[i] = int(input(f"Entrez le coefficient de la note {i + 1} : "))

somme_produits = 0
somme_coefficients = 0

# Calculer la somme des produits et la somme des coefficients
for i in range(4):
    somme_produits += notes[i] * coefficients[i]
    somme_coefficients += coefficients[i]

# Calculer la moyenne pondérée
moyenne = somme_produits / somme_coefficients

# Afficher les notes et coefficients
for i in range(4):
    print(f"La note {i + 1} est {notes[i]}")
    print(f"Le coefficient est {coefficients[i]}")

# Afficher la moyenne pondérée
print(f"La moyenne pondérée est : {moyenne}")
