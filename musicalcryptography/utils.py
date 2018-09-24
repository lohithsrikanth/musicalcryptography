#!/usr/bin/env python

from ga import *
import itertools

def make_generate_function():
    def generate(seed_generation):
        """
        Given a seed generation will return a new generation of candidate solutions
        """
        length = len(seed_generation)
        # Keep the fittest 50%
        new_generation = seed_generation[:length/2]
        
        offspring = []
        while len(offspring) < length / 2:
            mum = roulette_wheel_selection(seed_generation)
            dad = roulette_wheel_selection(seed_generation)
            if similarity(mum, dad) > len(mum) /2:
                continue
            children = mum.breed(dad)
            offspring.extend(children)
            
               
         
        # Ensure the new generation is the right length
        new_generation.extend(offspring)
        new_generation = new_generation[:length]
        
        return new_generation
    
    return generate

def similarity(list1, list2):
	leven = []
	
	for i in range(len(list1)):
		dif = list1[i] - list2[i]
		leven.append(dif)
		
	return leven.count(0)
