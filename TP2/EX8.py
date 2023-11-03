
L = [1, 2, 3, 6, 6, 9]
M =int(input("donner un valeur  : "))
k=0
for i in range(len(L)):
    if M == L[i] :
        k = k+1
        r=i
        print(f"l indece de {k} oucernce est {r}")

print(f"le nombre de ouccrence de ce nombre {M} est {k}")

