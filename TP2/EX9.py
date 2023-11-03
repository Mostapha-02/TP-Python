
k =int(input("e choisir la direction de la convention if « euro_en_mad » tapez 1 ou if « mad en euro » tapez 2 : "))
if k == 1 :
    r= int(input("donner la valeur qui va convertir : "))
    while True :
        if r > 0:
            c=r * 10.86
            print(f"donc la valeur de {r} euro en mad est {c}mad")
            r=int(input("donner un autre val"))
        else:
            break
elif k == 2 :
    b = int(input("donner la valeur qui va convertir : "))
    while True :
        if b > 0:
            c=  0.092 * b
            print(f"donc la valeur de {b} mad en euro est {c}euro")
            b=int(input("donner un autre val"))
        else:
            break

