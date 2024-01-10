import math

# Fonction pour calculer le discriminant
def conversion_temps(h, m, s) :
    return h*3600 + m*60 + s

heures1 = int(input("donner la premier heure : "))
minutes1 = int(input("donner la premier minute : "))
secondes1 = int(input("Entrez la première seconde :  "))
temps1=conversion_temps(heures1,minutes1,secondes1)
heures2 = int(input("donner la dexiemme heure : "))
minutes2 = int(input("donner la dexiemme minute : "))
secondes2 = int(input("Entrez la dexiemme seconde :  "))
temps2= conversion_temps(heures2,minutes2,secondes2)
k=temps1-temps2
print(f"Le temps écoulé entre les deux horaires est de {k} secondes.")
