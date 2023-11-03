
L1 = [1, 3, 6, 78, 35, 88, 55]
L2 = [12, 24, 35, 24, 88, 120, 155]
L3 = []
for el in L1 :
    for le in L2 :
        if el == le and el not in L3 :
            L3.append(el)
print(L3)

