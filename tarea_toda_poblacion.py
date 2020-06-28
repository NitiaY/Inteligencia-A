
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:31:41 2020

@author: Usuario
"""

import random

modeloVector = [9,9,9,9,9,9,9,9,9,9]
largoIndividuo = 10

num = 10  #Cantidad de individuos
generaciones = 100  #Generaciones
seleccion_individuos = 3 #individuos>2
mutacion_probabilidad = 0.2

def individuo(min, max):
    return [random.randint(min,max) for i in range(largoIndividuo)]

def newpoblacion():
    return [individuo(0,9) for i in range(num)]

#Funcion la que se debe cambiar en funcion a f(x)
def funcion_objetivo(individuo):
     aptitud = 0
     for i in range(len(individuo)):
         if individuo[i] == modeloVector[i]:
             aptitud += 1
     return aptitud
 

def seleccion_y_reproduccion(poblacion):
    evaluacion = [ (funcion_objetivo(i), i) for i in poblacion]
    evaluacion = [i[1] for i in sorted(evaluacion)]
    # print("eval",evaluacion)
    poblacion = evaluacion
    selected = evaluacion[(len(evaluacion)-seleccion_individuos):]
    puntoCambio = random.randint(1,largoIndividuo-1)
   # print(puntoCambio)
    #print("Evaluacion: ",evaluacion)
    for i in range(len(poblacion)-seleccion_individuos):
        padre = random.sample(selected,2)
     #   print("Padre:",padre)
        poblacion[i][:puntoCambio] = padre[0][:puntoCambio]
        poblacion[i][:puntoCambio] = padre[1][:puntoCambio]
    return poblacion

def mutacion(poblacion):
    for i in range(len(poblacion)-seleccion_individuos):
        if random.random() <= mutacion_probabilidad:
            puntoCambio = random.randint(1,largoIndividuo-1)
            nuevo_valor = random.randint(0,9)
            while nuevo_valor == poblacion[i][puntoCambio]:
                nuevo_valor = random.randint(0,9)
           # print("Cambio: ",puntoCambio, "nuevo valor: ",nuevo_valor)
            #print("Inicial: ",poblacion[i])
            #poblacion[i][puntoCambio] = nuevo_valor
            #print("Final: ",poblacion[i])
    return poblacion 

#Principal
poblacion = newpoblacion()
print("\nPoblacion Inicial:\n%s"%(poblacion))
poblacion = seleccion_y_reproduccion(poblacion)
print("\nSeleccion:\n%s"%poblacion)
poblacion = mutacion(poblacion)
print("\nMutacion:\n%s"%poblacion)

#Para todas las generaciones:
while generaciones!=0:
    print("\nPoblacion Inicial:\n%s"%(poblacion))
    poblacion=seleccion_y_reproduccion(poblacion)
    print("\nSeleccion :\n%s"%(poblacion))
    poblacion=mutacion(poblacion)
    print("\nMutacion :\n%s"%(poblacion))
    generaciones=generaciones-1
