#!/usr/bin/env python
"""
This module encapsulates the behaviour of first species counterpoint
"""
import random
from ga import *
from utils import make_generate_function

# some sane defaults
DEFAULT_POPULATION_SIZE = 1000

f = open("transition_probability_matrix.txt", "r")
fitness_matrix = eval(f.read())
f.close()

def create_population(multi_chromosomes):
    """
    Will create a new list of random candidate solutions
    """
    result = []
    for i in range(len(multi_chromosomes)):
        genome = Genome(multi_chromosomes[i])
        result.append(genome)
    return result


def fitness_function(genome):
    """
    Given a candidate solution will return its fitness score. Caches the fitness score in the genome.
    """
    # Save some time!
    if genome.fitness is not None:
        return genome.fitness
        
    # The fitness score to be returned.
    fitness_score = 0.0
        
    for i in range(len(genome)):
        if i == len(genome) -1:
            break
        fitness_score += fitness_matrix[genome[i]][genome[i + 1]]          
                   
    genome.fitness = fitness_score
        
    return fitness_score
    

def halt(population, generation_count):
    """
    Given a population of candidate solutions and generation count (the number of epochs
    the algorithm has run) will return a boolean to indicate if an acceptable solution has
    been found within the referenced population.
    """
    MAX_GENERATION = 0
    if len(population[0]) <= 2:
        MAX_GENERATION = 50
    if 3 <= len(population[0]) <= 5:
        MAX_GENERATION = 25
    if len(population[0]) > 5:
        MAX_GENERATION = 10
    MAX_REWARD = 0.0
    for i in range(len(population[0])):
        MAX_REWARD += 0.7
    return (population[0].fitness >= MAX_REWARD or generation_count > MAX_GENERATION)
    
