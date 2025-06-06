from random import randint

numeros=[]

cont=0
for i in range(100):
    numeros.append(randint(0,10))
    for i in range(len(numeros)):
        if i %2==0: #solo muestra numeros pares
            print(f"posicion {i}    {numeros[i]}")

#.mostrar numero mayor
mayor=max(numeros)
print(f"numero mayor {mayor}")
for i in range(len(numeros)):
    if numeros[i]==max(numeros):
        print(i, end="🌻")

#.mostrar el indice (posicion) del elemento mayor
print("indice donde se encuentra numero mayor")
for i in range(len(numeros)):
    if  numeros[i]==max(numeros):
        print(i, end= "-")


#.mostrar numero menor
menor=min(numeros)
print(f"numero menor {menor}")
for i in range(len(numeros)):
    if numeros[i]==min(numeros):
        print(i, end="🌸")

#. Crear un Lista de tamaño 10 que almacene nombres de personas

