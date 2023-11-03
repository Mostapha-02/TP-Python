L = [1, -30, 0, -2, 500, 4, 2, 100]
M = []
for el in L:
    if el < 0:
        M.append(el)

for el in L:
    if el >= 0:
        M.append(el)

print(M)