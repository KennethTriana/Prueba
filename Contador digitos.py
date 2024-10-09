def contar_digitos(numero:int)->int:
    contador = 0 
    terminar = False

    while terminar == False:
        if numero == 0:
            terminar = True
        else:
            contador += 1
            numero //= 10 

    return contador

num = int(input("Ingrese un numero entero: "))
digitos = contar_digitos(num)
print("La cantidad de digitos del numero es", digitos)