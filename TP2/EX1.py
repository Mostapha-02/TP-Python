k=input("donner un valeur numerique : ")
sm =0
exp =""
for i in range(1,5):

    trm = int(str(k)*i)
    sm = sm + trm

    exp = exp+ str(trm)
    if i < 4:  # Cette condition ajoute le signe "+" entre les termes, sauf pour le dernier
        exp += " + "

print(f"la somme {exp} = {sm}")
