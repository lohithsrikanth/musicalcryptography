import os
from collections import *
from itertools import *


def counting_transitions(sequences):
	counts = Counter()
	entries = set()
	for seq in sequences:
		entries.update(seq)
		for a, b in zip(seq, islice(seq, 1, None)):
			if a == b and counts[a,b] > 4000:
				continue
			counts[a, b] += 1
			
	probs = {}
	for a in entries:
		probs.update(((a,b), counts[a,b]) for b in entries if counts[a,b])
	
	return probs

rootdir = "/home/lohith/Documents/Project/note_lists/note_list10"
note_list = []
for subdir, dirs, files in os.walk(rootdir):
	for file1 in files:
		f = open(os.path.join(subdir, file1), 'r')
		var1 = eval(f.read())
		f.close()
		note_list.extend(var1)

data = note_list	
transitions = {}		
transitions = counting_transitions([data])
counting_matrix = []
for i in range(128):
	cols = []
	for j in range(128):
		try:
			cols.append(transitions[(i,j)])
		except KeyError:
			cols.append(0)
	counting_matrix.append(cols)
	
	
f = open("/home/lohith/Documents/Project/jythonMusic/count_lists/count_matrix10.txt", "w")
f.write(str(counting_matrix))
f.close()
cProfile.run('counting_transitions([data])', 'stats.txt')
