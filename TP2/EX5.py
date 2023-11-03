
L = [1, 2, 3, 6, 7, 9]
M =int(input("donner un valeur qui insere : "))

index=0
while index<len(L) and L[index]<M :
    index = index+1
L.insert(index, M)

print(L)
