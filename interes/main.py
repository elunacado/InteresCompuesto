import math

invertido=int(input("Ingresa cuanto invertiste "))
porcentaje=float(input("Ingresa cuanto es el porcentje de regreso mensual"))
años=int(input("Ingresa los años por los que lo vas a invertir "))
decimal=float(porcentaje/100+1)

first=float(decimal)*float(invertido)
result=math.floor(float(decimal)**int(años)*float(invertido))

print("el primer año tu inversion valdra "+ str(first))
print("si lo multiplicas por la cantidad de años que es igual a "+str(años)+" el valor final de tu inversion sera de "+str(result))

input("de click a enter para salir")

#sresultado=float(invertido*)