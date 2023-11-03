l= [2,4,7,4,8,4]
nb=int(input("donner le nombre suprimer : "))
lv=[]
for el in l :
    if el != nb:
        lv.append(el)

print(f"Nouvelle liste après suppression des occurrences de {nb} : {lv}")

