def calcular_factorial(n:int)->int:
    terminar = False
    factorial = 1 

    while terminar == False:
        if n == 0:
            terminar = True
        else:
            factorial *= n 
            n -= 1
    return factorial

numero = int(input("Ingrese un numero positivo: "))

while numero < 0:
    print ("No se permiten numeros negativos")
    numero = int(input("Ingrese un numero positivo: "))

print(numero, "! es igual a", calcular_factorial(numero))