#autor:carlos ruben potrero corona
#fecha:14_ agosto_ 2018
#actividad:trabajo para un 8 xdxdxdxd  


def isPrimefor(num):  
    if num<2:
       flag=False
    elif num==2:
       flag=True
    else:
      flag=True
      for i in range (2, num-1/2):
         if num%i==0: 
            flag=False
            break
    return flag
p=input ("dame un numero: ")
if isPrimefor(p):
   print("el numero es primo")
else:
   print ("el numero no es primo")

