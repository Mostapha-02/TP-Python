

for i in range(7):
    for j in range(7):
        if j == 0 or j == i or i == 6 or i>j:
            print("*", end=" ")# utilisons end=" " pour séparer les astérisques par des espaces et eviter saut de ligne authomatiquement
        else:
            print(" ", end=" ")
    print()
