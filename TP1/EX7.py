nombre1 = float(input("donner un nombre1 :" ))
nombre2 = float(input("donner un nombre2 :" ))
oper=input("donner un operateur soit + ou - ou * ou % / : ")
if oper== '+' :
    sum = nombre2 + nombre1
    print(f"la somme est {sum}")
elif oper== '-' :
    result = nombre1 - nombre2
    print(f"la soustraction est {result}")
elif oper == '*' :
    result = nombre1 * nombre2
    print(f"la multiplication est {result}")
elif oper == '/' :
    result = nombre1/nombre2
    print(f"la division est {result}")
else:
    print("loperation n'est pas valide")


