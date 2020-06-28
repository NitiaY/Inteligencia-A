# -*- coding: utf-8 -*-
"""
Created on Sat Jun 1 20:58:48 2020

@author: Usuario
"""


import random
modeloVector=[1,1,1,1]
#modeloVector=[1,1,1,1,1,1,1,1,1]

largoIndividuo=4#10
num=10                         #cantidad de individuos
generaciones=6                 #Generaciones
seleccion_individuos=2         #individuos>2
mutacion_probabilidad=0.3      #0.2

def individuo(max,tam):
    return (random.sample(range(max),tam))

def newpoblacion():
    return individuo(15, num) 

def decabin(n):
    binario = ''
    while n // 2 != 0:
        binario = str(n % 2)+binario
        n = n // 2          
    binario=str(n)+binario
    if((len(binario)<largoIndividuo)):     #5->4,9->8
        for i in range((largoIndividuo)-(len(binario))):
            binario=str('0')+binario      
    return [ int(binario[i:i+1]) for i in range(len(binario))]

def newpoblacionb(individuo):
    VectorB=[]
    for i in range(len(individuo)):
        h=(decabin(individuo[i]))
        VectorB.append(h)
    return VectorB
    

#la cantidad de 1 que se asemeja a nuestro modelo del vector
def funcion_objetivo(VectorB):
        aptitudFisica=0
        for j in range(len(VectorB)):
            if(VectorB[j]==modeloVector[j]):
                aptitudFisica=aptitudFisica+1     
        return aptitudFisica 

#Funcion Objetivo de f(x^2)
#uso de la funcion
# def funcion_objetivo(individuo):
#     for i in range(len(individuo)):
#         individuo[i]=individuo[i]*individuo[i]
#     return individuo

#------- 2da forma
# def funcion_objetivo(VectorB):
#     numerofinal=int("".join(map(str,VectorB)),2)
#     print(numerofinal*numerofinal)
#     return numerofinal*numerofinal 


def seleccion_y_reproduccion(VectorB):
    evaluacion=[(funcion_objetivo(i),i) for i in VectorB]
    #print("eval",evaluacion)
    #ordena la evaluacion, por cuantos 1 tiene en el VectorBinario
    evaluacion=[i[1]for i in sorted(evaluacion)]
    #print("eval",evaluacion)
    VectorB=evaluacion
    #print("tam",len(evaluacion)-seleccion_individuos)
    selected=evaluacion[(len(evaluacion)-seleccion_individuos):]
    #print("Selecciona",selected)
    #print("poblacion",VectorB)
    #punto de cambio estatico para todos como pude ser random para cada uno
    puntoCambio=random.randint(0, 3)#0,8
    # print(puntoCambio)
    # print("Evaluacion: ",evaluacion)
    for i in range(len(VectorB)-seleccion_individuos):
            padre=random.sample(selected, 2)
            #print("padre",padre)
            VectorB[i][:puntoCambio]=padre[0][:puntoCambio]
            VectorB[i][puntoCambio:]=padre[1][puntoCambio:]
    #print("aca",poblacion)
    return VectorB

def mutacion(VectorB):
    for i in range(len(VectorB)-seleccion_individuos):
        
        if random.random()<=mutacion_probabilidad:
            puntoCambio=random.randint(1, 3)#largoIndividuo-1
            nuevo_valor=random.randint(0, 1)
            while nuevo_valor == VectorB[i][puntoCambio]:
                nuevo_valor=random.randint(0, 1)
            # print("Cambio :",puntoCambio,"Nuevo Valor :",nuevo_valor)
            # print("Inicial",i," ",VectorB[i])
            VectorB[i][puntoCambio]=nuevo_valor
            #print("Final",VectorB[i])
    return VectorB


#Main
p=newpoblacion()
for i in range(generaciones): 
    print("\nPoblacion Inicial:\n%s"%(p))
    p=newpoblacionb(p)
    print("\nPoblacion Binaria:\n%s"%p)
    p=seleccion_y_reproduccion(p)
    print("\nSeleccion :\n%s"%(p))
    p=mutacion(p)
    print("\nMutacion :\n%s"%(p))
    print("..... poblacion Final..........")
    p=[int("".join(map(str,i)),2) for i in p]
    print(p)


# p=newpoblacion()
# for i in range(generaciones):
#     print("\nPoblacion Inicial:\n%s"%(p))
#     p=funcion_objetivo(p)#para el caso de la f(x^2)
#     p=newpoblacionb(p)
#     print("\nPoblacion Binaria:\n%s"%p)
#     p=seleccion_y_reproduccion(p)
#     print("\nSeleccion :\n%s"%(p))
#     p=mutacion(p)
#     print("\nMutacion :\n%s"%(p))
#     print("..... poblacion Final..........")
#     p=[int("".join(map(str,i)),2) for i in p]
#     print(p)

