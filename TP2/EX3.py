import random

nb = random.randint(1, 100)

for i in range(8):
    k = int(input("Donnez une valeur entre 1 et 100 : "))

    if k == nb:
        print("Bravo !")
        c = i + 1  # Vous devez ajouter 1 à i pour obtenir le nombre d'essais correct
        print(f"Vous avez gagné en {c} essais.")
        break
    elif k < 1 or k > 100:
        print("Vous avez saisi un nombre en dehors de l'intervalle.")
    elif k < nb:
        print("Oups ! Entrez un nombre plus grand.")
    elif k > nb:
        print("Oups ! Entrez un nombre plus petit")

if k!=nb :
 print("vous navez pas ganger en 7 essai")



