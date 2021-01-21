#!/usr/bin/env python

from transition_matrix import *
import string
from my_own_product import *
from first_species import *
from ga import *
from index import *

user_input = string.lower(raw_input("Enter the message you wish to encrypt: "))
length = len(user_input)
playable_notes = []
playable_channels = []
candidate_channels = []
duration_list = []
dynamics_list = []

word_list = user_input.split(' ')       # splitting a sentence according to the spaces
word_list_length = []

def get_candidate_notes(word1):
    global candidate_channels
    candidate_channels = []
    candidate_note_list = []            
    candidate_note_pitches = []
    for i in range(len(word1)):
        if i == 0:
            candidate_note_list.append(key[ord(random.choice('a')) - ord('a')][ord(word1[i]) - ord('a')])
        current = word1[i]
        if i == len(word1) - 1:
            break
        next = word1[i+1]    
        candidate_note_list.append(key[ord(current) - ord('a')][ord(next) - ord('a')])

    for i in range(len(word1)):
        nested = []
        nested2 = []
        for j in range(len(candidate_note_list[i])):
            nested.append(candidate_note_list[i][j][0])
            nested2.append(candidate_note_list[i][j][1])
        candidate_note_pitches.append(nested)
        candidate_channels.append(nested2)
        
    return candidate_note_pitches

def generate_multi_chromosomes(word1):
    c = get_candidate_notes(word1)
    multi_chromosomes = list(product(*c))
    for i in range(len(multi_chromosomes)):
        multi_chromosomes[i] = list(multi_chromosomes[i])
    return multi_chromosomes

for word in word_list:
    word_list_length.append(len(word))


generate_function = make_generate_function()    
for word in word_list:
    real_notes = []
    real_channels = []
    word1 = []
    '''
    if len(word) == 1:
        c = get_candidate_notes(word)
        print c
        playable_notes.append(random.choice(c[0]))
        index = find(playable_notes[-1], c[0])
        playable_channels.append(candidate_channels[0][index[0]])
        continue
    '''
    if ',' in word:
        word1 = word.split(',')
        multi_chromosomes = generate_multi_chromosomes(word1[0])
    elif '.' in word:
        word1 = word.split('.')
        multi_chromosomes = generate_multi_chromosomes(word1[0])
    elif '?' in word:
        word1 = word.split('?')
        multi_chromosomes = generate_multi_chromosomes(word1[0])
    elif '!' in word:
        word1 = word.split('!')
        multi_chromosomes = generate_multi_chromosomes(word1[0])
    elif ':' in word:
        word1 = word.split(':')
        multi_chromosomes = generate_multi_chromosomes(word1[0])
    elif ';' in word:
        word1 = word.split(';')
        multi_chromosomes = generate_multi_chromosomes(word1[0])
    else:
        multi_chromosomes = generate_multi_chromosomes(word)
    initial_population = create_population(multi_chromosomes)
    g_a = genetic_algorithm(initial_population, fitness_function, generate_function, halt)
    fitness = 0.0
    counter = 0
    for generation in g_a:
        counter += 1
        print "--- Generation %d ---"% counter
        real_notes = generation[0]
    
    print    
    # extend the playable notes list by the fittest member of nth generation
    playable_notes.extend(real_notes)
    if ',' in word or '.' in word or '?' in word or '!' in word or ';' in word or ':' in word:
        c = get_candidate_notes(word1[0])
    else:
        c = get_candidate_notes(word)
    
    for i in range(len(real_notes)):
        index = find(real_notes[i], c[i])
        real_channels.append(candidate_channels[i][index[0]])
    playable_channels.extend(real_channels)
    if ',' in word:
        playable_notes.append(-44)
        playable_channels.append(9)
    if '.' in word:
        playable_notes.append(-46)
        playable_channels.append(0)
    if '!' in word:
        playable_notes.append(-33)
        playable_channels.append(9)
    if '?' in word:
        playable_notes.append(-63)
        playable_channels.append(9)
    if ';' in word:
        playable_notes.append(-59)
        playable_channels.append(9)
    if ':' in word:
        playable_notes.append(-58)
        playable_channels.append(9)
    
def check(list1, list2):
    return len(list1) == len(list2)

if not check(playable_notes, playable_channels):
    raise Exception("The lengths of lists playable_notes and playable_channels are not equal")

for i in range(len(playable_notes)):
    duration_list.append(1.5)
    dynamics_list.append(85)

def mutate():
    global duration_list
    global dynamics_list
    for i in range(len(playable_notes)):
        if i == len(playable_notes) - 1:
            break
        if fitness_matrix[playable_notes[i]][playable_notes[i+1]] < 0.2:
            duration_list[i] -= random.random()   
            dynamics_list[i] -= random.randint(30, 50)
            
        if 0.2 < fitness_matrix[playable_notes[i]][playable_notes[i+1]] < 0.6:
            duration_list[i] += random.random()
            dynamics_list[i] += random.randint(15, 25)
        else:
            duration_list[i] += random.random()
            dynamics_list[i] += random.randint(25, 35)

# Mutation of durations and dynamics happens here
mutate()
# print playable_notes
# print playable_channels

f = open("playable_notes.txt", "w")
f.write(str(playable_notes))
f.close()

f = open("playable_channels.txt", "w")
f.write(str(playable_channels))
f.close()

f = open("duration_list.txt", "w")
f.write(str(duration_list))
f.close()

f = open("dynamics_list.txt", "w")
f.write(str(dynamics_list))
f.close()

f = open("word_list_length.txt", "w")
f.write(str(word_list_length))
f.close()

    


