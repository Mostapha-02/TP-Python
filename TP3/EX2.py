import  math
def desc(a, b, c):
   return b**2 - 4*a*c
def nombre_solution(a , b ,c):
  D = desc(a, b, c)
  if D > 0:
    return  2
  elif D == 0:
    return  1
  else:
    return  0
def affiche_nombre(a , b , c):
  k = nombre_solution(a ,b,c)
  if k == 2 :
    print("le nombre des racine est : 2")
  elif k == 1 :
    print("le nombre de soltion est : 1 ")
  else:
    print("elle n'est pas des solition")
def Racin1(a , b ,c):
  des = desc(a,b,c)
  if des >= 0 :
      return (-b - math.sqrt(des))/2*a
  else:
      return None
def Racin2(a,b,c):
  ds = desc(a,b,c)
  if ds >= 0 :
      return  (-b+math.sqrt(ds))/2*a
  else:
      return None
affiche_nombre(1 , 5 , 1)
r=Racin1(1 , 5 , 1)
s=Racin2(1 , 5 , 1)
print(f"la racin1 est : {r} est la racin2 est : {s}")

