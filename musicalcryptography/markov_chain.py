from collections import *
from itertools import *

def cond_probs_np(sequences):
	counts = Counter()
	entries = set()
	for seq in sequences:
		entries.update(seq)
		for a, b in zip(seq, islice(seq, 1, None)):
			counts[a, b] += 1
	probs = {}
	for a in entries:
		suma = float(sum(counts[a, b] for b in entries))
		if suma != 0:
			probs.update(((a,b), counts[a, b] / suma) for b in entries if counts[a,b])

	return probs

'''	
data = [6, 6 ,3, 1, 9, 10]
prob_dict = cond_probs_np([data])

list_of_lists = []
for i in range(0,127):
	cols = []
	for j in range(0,127):
		try:
			cols.append(prob_dict[(i,j)])
		except KeyError:
			cols.append(0)
	list_of_lists.append(cols)
	
print list_of_lists
'''	