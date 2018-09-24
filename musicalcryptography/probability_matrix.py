#!/usr/bin/env python

from markov_chain import *

f = open("/home/lohith/Documents/Project/jythonMusic/prime_note_list.txt")
var1 = f.read()
data = eval(var1)
prob_dict = cond_probs_np([data])

f2 = open("probability_dictionary.txt", "w")
f2.write(str(prob_dict))
f2.close()