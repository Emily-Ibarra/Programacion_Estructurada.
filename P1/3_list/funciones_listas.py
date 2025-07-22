"""
List (Array)
son colleciones o conjunto de datos/ valores bajo
un mismo nombre, para acceder a los valores se hace un indice numerioco 

Nota: sus valores si son modificables 

La lista es una collecion ordenada y modificable permite miembros duplicados.

"""

import os
os.system("cls")

#Funciones mas comunes en las listas 

paises=["Mexico", "Brasil", "España","Canada"]
numeros=[23,45,8,24,23,56]
varios=["hola",3.1416,33,True]

#Imprimir 
print(paises)
print(numeros)
print(varios)

#Recorrer una lista e imprimir el contenido 
#1er forma

for i in paises:
    print(i)

lista="["
for i in paises:
    lista=lista+f"{i},"
print(lista+"]")

#2daa forma
for i in range(0,len(paises)):
    print(paises[i])

lista="["
for i in range(0,len(paises)):
    lista=lista+f"{paises[i]},"
print(lista+"]")

os.system("cls")

#ordenar los elementos de las lisats 

print(paises)
print(numeros)
print(varios)

paises.sort()
print(paises)
numeros.sort()
print(numeros)

#dar la vuelta a las listas 

varios.reverse()
print(varios)
paises.reverse()
print(paises)
numeros.reverse()
print(numeros)

#Buscar un elemneto dentro de una lista 
print("España" in paises)

#iNsertar ,añadir , agregar un elem enbto a la lista 
os.system("cls")
print(paises)

#1er forma 
paises.append("México")
print(paises)

#2da forma
paises.insert(1,"México")
print(paises)

#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4)
print(paises)

#2da forma 
paises.remove("Honduras")
print(paises)

#Buscar un elemento dentro de la lista
print(paises)

print("Brasil" in paises)

#Contar el numeros de veces que aparece un elemento dentro de una lista

print(numeros)

cuantos=numeros.count(23)
print(cuantos)

numeros.append(23)
cuantos=numeros.count(23)
print(cuantos)

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
paises.reverse()
print(paises)

posicion=paises.index("Canada")
print(f"El valor de Canada lo encontro en la posicion: {posicion}")

#Unir el contenido de una lista dentro de otra lista
os.system("clear")
print(numeros)
numeros2=[100,200]

print(numeros2)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente


numeros.extend(numeros2)
print(numeros)

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)

