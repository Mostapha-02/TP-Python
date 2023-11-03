grad= input("dooner votre grade : ")
heure = int(input("donner les nombre des heures qui travaille : "))
if grad == 'A' :
    res=float( heure*200 + ((heure/20)*1000))
    print(f"votre salaire et {res}DH")
elif grad == 'B' :
    res = float(heure*150) + ((heure/20)*800)
    print(f"votre salaire et {res}DH")
elif grad == 'C' :
    res = float(heure*120) + ((heure/15)*500)
    print(f"votre salaire et {res}DH")
elif grad == 'D' :
    res = float(heure*100) + ((heure/15)*350)
    print(f"votre salaire et {res}DH")
elif grad == 'E' :
    res = float(heure*80) + ((heure/10)*100)
    print(f"votre salaire et {res}DH")