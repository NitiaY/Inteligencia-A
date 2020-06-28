# -*- coding: utf-8 -*-
"""
Created on Sat Jun 9 20:57:01 2020

@author: Usuario
"""
import array
import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
# weights=(1.0,) 1 maximizar, -1 minimizar
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Attribute generator
toolbox.register("attr_bool", random.randint, 0, 1)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 100)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
#Funcion de evaluacion
#def evalOneMax(individual):
def funObjetivo(individual):
   # print(individual)
    #return sum(individual),
    numerofinal=int("".join(map(str,individual)),2)
    print(numerofinal*numerofinal,)
    return numerofinal*numerofinal,

toolbox.register("evaluate", funObjetivo)
#cruzar
toolbox.register("mate", tools.cxTwoPoint)
#mutar con una probabilidad de 0.05
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
#Seleccion es por torneo cada 3
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    #es para que no exista repeticiones
    random.seed(64)
    #poblacion
    pop = toolbox.population(n=300)
    #salon de la fama=el mejor
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    #media
    stats.register("avg", numpy.mean)
    #desviacion standar
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=40, 
                                   stats=stats, halloffame=hof, verbose=True)
    
    return pop, log, hof

if __name__ == "__main__":
    #main()
    pop,log,hof=main()
    #print(pop)
    #print(log)#resumen de los datos
    #print(hof)#mejor individuo
    

