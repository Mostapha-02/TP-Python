chiffre = input("Saisissez un chiffre : ")

somme = 0
expression = ""

for i in range(1, 5):
    terme = int(str(chiffre) * i)  # Cette ligne crée un terme en répétant le chiffre 'i' fois
    somme += terme
    expression += str(terme)
    if i < 4:  # Cette condition ajoute le signe "+" entre les termes, sauf pour le dernier
        expression += " + "

print(f"La somme {expression} = {somme}")
