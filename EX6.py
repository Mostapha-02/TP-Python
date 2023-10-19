nombre1 = float(input("donner un nombre1"))
nombre2=float(input("donner un nombre 2"))
if (nombre1 >0 and nombre2>0) or (nombre1 <0 and nombre2<0):
    print("le produits est positif")
elif (nombre1==0 or nombre2==0) :
    print("le produit est nul")
else:
    print("le produit est negatif")
