import math

# Fonction pour calculer le discriminant
def conversion_temps(h, m, s) :
    return h*3600 + m*60 + s
r=conversion_temps(10,4,33)
heures = 2
minutes = 30
secondes = 45
r=conversion_temps(heures,minutes,secondes)
print(f"{heures}heures {minutes}minutes {secondes}secondes est secondes est egale : {r}s")

