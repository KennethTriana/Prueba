# -*- coding: utf-8 -*-
"""
Ejercicio nivel 2: Agenda de peliculas.
Modulo de interacci0n por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2
"""
import modulo_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict)-> None:
          
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" )
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)
  
    if (hora//100 < 10):
        hora_formato = "0"+ str(hora//100)
    else:
        hora_formato = str(hora//100)
    
    if (hora%100 < 10):
        min_formato = "0"+ str(hora%100)
    else:
        min_formato = str(hora%100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)

def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
        nombre_mayor=mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
     
        print("El nombre de la pelicula con mayor duracion es: " , nombre_mayor )
       
     
def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
  
    promedio=mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    hora=int(promedio)    
    horas=hora//60
    minutos=hora%60
    print(f' El promedio de duracion de las 5 peliculas es:  {horas}{":"}{minutos}')
    
    
    

def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    
   
    #import re
    anio = int(input("Ingrese el anio de estreno de una pelicula : "))
    msg=mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio)
    if msg=="":
       print("Ninguno")
    else:
         #msg=re.findall('([\d+]{4})', msg)
         print(msg)
    
          

def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    
   
    numero=mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    print(numero)
    
def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de reagendar una pelicula
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Reagendar una pelicula de la agenda")

    nombre = input("Ingrese el nombre de la pelicula que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre,p1,p2,p3,p4,p5)
    
    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        peli=pelicula
        print("-"*50)
        nombre = pelicula["nombre"]
        genero = pelicula["genero"]
        duracion = pelicula["duracion"]
        anio = pelicula["anio"]
        clasificacion = pelicula["clasificacion"]
        hora = pelicula["hora"]
        dia = pelicula["dia"]
        
        print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" )
        print("Genero: " + genero + " - Clasificacion: " + clasificacion)
      
        if (hora//100 < 10):
            hora_formato = "0"+ str(hora//100)
        else:
            hora_formato = str(hora//100)
        
        if (hora%100 < 10):
            min_formato = "0"+ str(hora%100)
        else:
            min_formato = str(hora%100)

        print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)
        print("-"*50)
        print("si desea reagendar esta pelicula debe proporcionar los siguientes datos")
        
        
        control_horario=input("Desea controlar los horarios de las peliculas Si:1 NO:2 : ").strip()
        nueva_hora = int(input("Nueva Hora, ejemplo 1530:"))
        nuevo_dia=input("Nuevo dia de la semana:")
        print(control_horario)
        
        
        
        if control_horario=="1":
           control_horario=True
        else:
            control_horario=False
            
        
            
        
        
        resultado=mod.reagendar_pelicula(peli, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5)
        if resultado==False:
            print("No es posible reagendar esta pelicula")
        if resultado==True:
             print("reagendada correctamente")
             
        
        
def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de decidir si se puede invitar a alguien a ver una pelicula o no.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Decidir si se puede invitar a alguien a ver una pelicula")

    nom_peli = input("Ingrese el nombre de la pelicula: ")
    pelicula = mod.encontrar_pelicula(nom_peli,p1,p2,p3,p4,p5)

    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        peli=pelicula
        print("-"*50)
        nombre = pelicula["nombre"]
        genero = pelicula["genero"]
        duracion = pelicula["duracion"]
        anio = pelicula["anio"]
        clasificacion = pelicula["clasificacion"]
        hora = pelicula["hora"]
        dia = pelicula["dia"]
        
        print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" )
        print("Genero: " + genero + " - Clasificacion: " + clasificacion)
      
        if (hora//100 < 10):
            hora_formato = "0"+ str(hora//100)
        else:
            hora_formato = str(hora//100)
        
        if (hora%100 < 10):
            min_formato = "0"+ str(hora%100)
        else:
            min_formato = str(hora%100)

        print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)
        print("-"*50)
        print("Si desea ver esta pelicula debe proporcionar los siguientes datos: ")
        
        edad_invitado = int(input("Digite Edad: "))
        if edad_invitado>=11:
            autorizacion_padres=False
             
        else:
           autorizacion_padres=input("Tiene autorizacion de sus padres para ver la pelicula Si:1 NO:2 : ").strip()
           if autorizacion_padres=="1":
                autorizacion_padres=True
           else:
                autorizacion_padres=False
                
        pelicula=mod.decidir_invitar(peli, edad_invitado, autorizacion_padres)
            
       
        
        if pelicula==True:
            print("Si puede ver la pelicula")
        else:
            print("No puede ver la pelicula")
        
        
            
  
def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola.
    Esta funcion primero crea las cinco peliculas que se van a manejar en la agenda.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    pelicula1 = mod.crear_pelicula("Coco",  "Familiar, Aventura", 105, 2017, "18+", 1301, "miércoles")
    pelicula2 = mod.crear_pelicula("A Quiet Place",  "Terror, Suspenso", 90, 2018, "13+", 1302, "jueves")  
    pelicula3 = mod.crear_pelicula("The Social Dilemma",  "Documental, Drama", 94, 2020, "13+", 1303, "viernes")
    pelicula4 = mod.crear_pelicula("Mad Max: Fury Road",  "Acción, Ciencia-Ficción", 120, 2015, "16+", 1304, "sábado")
    pelicula5 = mod.crear_pelicula("Finding Nemo",  "Familiar, Aventura", 100, 2003, "18+", 1305, "domingo")

    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de peliculas para la semana de receso" +"\n"+("-"*50))
        print("Pelicula 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-"*50)
        
        print("Pelicula 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-"*50)
        
        print("Pelicula 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-"*50)
        
        print("Pelicula 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-"*50)
        
        print("Pelicula 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-"*50)
        
        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4:dict, p5:dict) -> bool:
    """Le muestra al usuario las opciones de ejecución disponibles.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente 
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opción para salir 
        de la aplicacion.
    """
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")    
    print(" 7 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)        
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando


iniciar_aplicacion()
