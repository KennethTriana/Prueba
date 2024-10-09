# -*- coding: utf-8 -*-
"""
Ejercicio nivel 2: Agenda de peliculas.
Módulo de cálculos.

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

NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    pelicula = {"nombre":nombre,
                  "genero":genero,
                  "duracion":duracion,
                  "anio":anio,
                  "clasificacion":clasificacion,
                  "hora":hora,
                  "dia":dia}
    return  pelicula
    
    

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    peli_buscada=None
    if p1["nombre"]==nombre_pelicula:
        peli_buscada=p1
    elif  p2["nombre"]==nombre_pelicula:
        peli_buscada=p2
    elif  p3["nombre"]==nombre_pelicula:
        peli_buscada=p3   
    elif  p4["nombre"]==nombre_pelicula:
        peli_buscada=p4
    elif  p5["nombre"]==nombre_pelicula:
        peli_buscada=p5
    return peli_buscada    
    
 

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    p_larga=p1["duracion"]
    nombre_mayor=p1["nombre"]
    if p2["duracion"]>p_larga:
        p_larga=p2["duracion"]
        nombre_mayor=p2["nombre"]
    if p3["duracion"]>p_larga:
        p_larga=p3["duracion"]
        nombre_mayor=p3["nombre"]
    if p4["duracion"]>p_larga:
        p_larga=p4["duracion"]
        nombre_mayor=p4["nombre"]
    if p5["duracion"]>p_larga:
        p_larga=p5["duracion"]
        nombre_mayor=p5["nombre"]   
    return nombre_mayor

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:   
    promedio=(p1["duracion"]+p2["duracion"]+p3["duracion"]+p4["duracion"]+p5["duracion"])/5  
    promedio1=round(promedio)
    return str(promedio1)

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    
    mayor=anio
    msg=""
    

    if p1["anio"]>mayor:
        msg=str(p1["nombre"]+",")
   
    
    if p2["anio"]>mayor:
       msg=msg+str(p2["nombre"]+",")
    
    if p3["anio"]>mayor:
        msg=msg+str(p3["nombre"]+",")
   
    
    if p4["anio"]>mayor:
       msg=msg+str(p4["nombre"]+",")
   
    
    if p5["anio"]>mayor:
       msg=msg+str(p5["nombre"])
   
    return msg  




def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    
    """
    
    contador=0
    if p1["clasificacion"]=="18+":
        contador=1
    if p2["clasificacion"]=="18+":
        contador=contador+1 
    if p3["clasificacion"]=="18+":
        contador=contador+1
    if p4["clasificacion"]=="18+":
        contador=contador+1
    if p5["clasificacion"]=="18+":
        contador=contador+1
    
    return contador

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool:
    
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    if control_horario==True:
       
        if nueva_hora==p1["hora"] or nuevo_dia==p1["dia"]: 
              resultado=False
            
        if nueva_hora==p2["hora"] or nuevo_dia==p2["dia"]:
              resultado=False
            
        if nueva_hora==p3["hora"] or nuevo_dia==p3["dia"]:
              resultado=False
                
        if nueva_hora==p4["hora"] or nuevo_dia==p4["dia"]:
              resultado=False
            
        if nueva_hora==p5["hora"] or nuevo_dia==p5["dia"]:
              resultado=False
        else:
             peli["hora"]=nueva_hora
             peli["dia"]=nuevo_dia
             resultado=True
              
    else:
        peli["hora"]=nueva_hora
        peli["dia"]=nuevo_dia
        resultado=True


    return resultado
    
    
    
        
    
    
    
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto
    
    resultado=False
    if edad_invitado>=18: 
        resultado=True
    
    if "error" in peli["genero"] and edad_invitado<15:
        resultado=False    
    
    if "amiliar" in peli["genero"] and edad_invitado<=10:
       resultado=True
    
       
    
    if peli["clasificacion"]=="7+" and edad_invitado<7 and autorizacion_padres==False:
        resultado=False 
    else:
        resultado=True
        
    if peli["clasificacion"]=="13+" and edad_invitado<13 and autorizacion_padres==False:
        resultado=False 
    else:
        resultado=True 
        
    if peli["clasificacion"]=="16+" and edad_invitado<16 and autorizacion_padres==False:
         resultado=False 
    else:
         resultado=True 
         
    if peli["clasificacion"]=="18+" and edad_invitado<18 and autorizacion_padres==False:
          resultado=False 
    else:
          resultado=True    
         
         
        
    
    if  "ocumental" in peli["genero"] and peli["clasificacion"]=="7+" and edad_invitado<7:
        resultado=True
    
    if  "ocumental" in peli["genero"] and peli["clasificacion"]=="13+" and edad_invitado<13:
        resultado=True
    
    
    if  "ocumental" in peli["genero"] and peli["clasificacion"]=="16+" and edad_invitado<16:
        resultado=True
    
    if  "ocumental" in peli["genero"] and peli["clasificacion"]=="18+" and edad_invitado<18:
        resultado=True
    
    
    
    
    return resultado









