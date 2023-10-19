# Initialiser les listes pour stocker les notes et les coefficients avec des éléments vides
nome = [0] * 2
prix = [0] * 2
quantité = [0] * 2
montant_ht = [0] * 2
montant_ttc = [0] * 2
total_facture = 0

# Saisir les notes et les coefficients au clavier
for i in range(2):
    nome[i] = input(f"Entrez le nom de {i + 1} article ")
    prix[i] = float(input(f"Entrez le prix de {i + 1} article "))
    quantité[i] = int(input(f"Entrez la quantité de {i + 1} article "))

    montant_ht[i] = prix[i] * quantité[i]
    montant_ttc[i] = montant_ht[i] + (montant_ht[i] * 0.2)  # Calcul du montant TTC
    total_facture += montant_ttc[i]

    print(f"Le montant total pour article {nome[i]} est {montant_ht[i]:.2f}")

# Afficher le total de la facture
print(f"Le total de la facture est {total_facture:.2f}")
