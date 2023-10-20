def calculeimc(poids, taille):
    imc = poids / (taille * taille)
    return imc

def vimv(imc):
    if imc > 40:
        return "obésité morbide ou massive"
    elif imc > 35 :
        return "obésité sévère"
    elif imc > 30 :
        return "obésité modérée"
    elif imc > 25:
        return "Surpoids"
    elif imc > 18.5:
        return "corpulence normale"
    elif imc > 16.5:
        return "Maigreur"
    else:
        return "Famine"

p = float(input("Donnez votre poids (en kg) : "))
t = float(input("Donnez votre taille (en m) : "))
imc = calculeimc(p, t)
resultat = vimv(imc)
print(f"Votre IMC est {imc:.2f}, ce qui correspond à une {resultat}.")

