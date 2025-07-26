lista=[23,44,23,-10,100,0,8,8]

def mostrar():
    for i in lista:
        print(i)

def buscar():
    numero=int(input("Ingrese un numero: ").strip())
    if numero in lista:       
      for i in range(0,len(lista)):
          if numero==lista[i]:
              print(f"El numero {numero} se encuentra en la posicion: {i}")
    else:
        print("No existe ese a buscar")  

mostrar()
buscar()          