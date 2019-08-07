'''
EJ1. Crea un programa que pregunte al usuario que introduzca su nombre y su edad. 

Muestra por pantalla que edad tendrá dentro de 100 años.

EJ2. Crea un programa que pregunte al usuario por un número y compruebe si el número es par o impar y muestre por pantalla si lo es o no lo es.
    EJ2.1: Si el numero es multiplo de cuatro imprime un mensaje diciendo que es multiplo de 4
'''
'''
num=int(input("Introduce un número: "))
print("El número es:",num)
if int (num)%2==0:
    print("El número es PAR")
elif int(num)%2!=0:
	print("El número es IMPAR")
elif int(num)//4==0:
	    print("El número es MÚLTIPLO DE 4")
else:
    print("Algo ha salido malísimamente mal")
'''


print("---START---")

nombre_usuario=input("Introduce nombre: ")
edad_usuario=int(input("Introduce tu edad: "))
edad_usuario+=100
print(nombre_usuario + ", en 100 anyos tendrás " + str(edad_usuario))

num=int(input("Introduce un número: "))
if int(num)==0:
	print("Tu número es 0")
else:
	print("Comprobando número elegido... ",num)

if int (num)%2==0:
	print("El número es PAR")
elif int(num)%2!=0:
	print("El número es IMPAR")
else:
	print("se jodió la wea ni par ni impar, pero no sé como cerrar esto")

if int(num)%4==0 and (num)>=4:
	print("El número ES MÚLTIPLO DE 4")
else:
    print("El número NO es múltiplo de 4")

print("---FINISH---")