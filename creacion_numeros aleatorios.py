import random #libreria para llamar y crear numeros random

numeros=[] #coleccion vacia

for i in range(10): #ciclo para repetir 100 veces las interaciones
    n = random.randint(1,100) #crea el numero entre 1 y 100
    numeros.append(n) #guardamos en la lista el numero aleatorio

print(numeros) #visualisamos lista

cont=0

for i in range(len(numeros)):
    if numeros [i]%2==0:
        cont+=1
        print(f"cantidad de numeros pares : {cont}")