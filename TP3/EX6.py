import math

# Fonction pour calculer le discriminant
def conversion_viteese(km ,m, cm) :
    return km*1000 + m + (cm/100)
def conversion_temps(km ,m, cm) :
    return km*1000 + m + (cm/100)
def vie(kilometres,metres,centimetres,heure1,minutes1,secondes1):
    kilometres= int(kilometres)
    metres= int(metres)
    centimetres= int(centimetres)
    heures1 = int(heure1)
    minutes1 = int(minutes1)
    secondes1 = int(secondes1)
    r=conversion_viteese(kilometres,metres,centimetres)
    k=conversion_temps(heures1,minutes1,secondes1)
    return  r/k
kilometres1= int(input("donner nombre de km : "))
metres1= int(input("donner nombre de m : "))
centimetres1= int(input("donner nombre de cm : "))
heures2 = int(input("donner la premier heure : "))
minutes2 = int(input("donner la premier minute : "))
secondes2 = int(input("Entrez la première seconde :  "))
reslt = vie(kilometres1,metres1,centimetres1,heures2,minutes2,secondes2)
print(f"La vitesse est de {reslt} m/s.")




