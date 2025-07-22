import os
#Ejemplo 1 crear una listav de numeros e imprimir el contenido 

os.system("cls")

numeros=[100,34]
print(numeros)

variable="["
for i in numeros:
    variable+=f"{i},"
print(f"{variable}]")

variable="["
for i in range(0,len(numeros)):
    variable+=f"{numeros[i]},"
print(f"{variable}]")

#Ejemplo 2 crear una lista de palabras y posteriormente buscar la coicidencia de una palabra 

os.system("cls")

palabras=["UTD","2023","logo","TI","2C clasica"]
palabra_buscar=input("Dame la palabra a buscar en la lista")

#1er
if palabra_buscar in palabras:
    print("Si sencontro la palabra en la lista")
else:
    print("No se encontro la palabra en la lsita")


#2da
#Ejemplo 3 anñadir elemntos a una lista 
#["UTD","2023","logo","TI","2C clasica",]
encontro=False
cuantas=0
posiciones=[]
for i in palabras:
    if i==palabra_buscar:
       encontro=True
       cuantas+=1
       posiciones.append(palabras.index(i))
if encontro:
    print("Si sencontro la palabra en la lista")
else:
    print("No se encontro la palabra en la lsita")

#3rd
encontro=False
cuantas=0
posiciones=[]
for i in range(0,len(palabras)):
    if palabras[i]==palabra_buscar:
       encontro=True
       cuantas+=1
       posiciones.append(i)
if encontro:
    print("Si sencontro la palabra en la lista")
else:
    print("No se encontro la palabra en la lsita")

#Ejemplo 4 crar una lista multidimensional para alamacenar los nombres y telefonso de unos contactos "agenda"

agenda=[
    ["Carlos","6181234567"],
    ["Carlos V","6181234567"],
    ["Carlos VI","6181234567"],
       ]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        lista+=f"{agenda[r][c]},"
    lista+="\n"
print(lista)
