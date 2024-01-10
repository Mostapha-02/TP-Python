import math

# Fonction pour calculer le discriminant
def conversion_temps(km ,m, cm) :
    return km*1000 + m + (cm/100)
kilometres= int(input("donner nombre de km : "))
metres= int(input("donner nombre de m : "))
centimetres= int(input("donner nombre de cm : "))
r=conversion_temps( kilometres,metres, centimetres)
print(f"{kilometres}kilometres {metres}metres {centimetres}centimetres esgale en kilometres {r}")


