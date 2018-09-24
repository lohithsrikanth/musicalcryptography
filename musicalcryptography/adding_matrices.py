import os
import numpy as np

rootdir = "/home/lohith/Documents/Project/jythonMusic/count_lists"
count_matrix = np.zeros((128, 128))

for subdir, dirs, files in os.walk(rootdir):
	for file1 in files:
		f = open(os.path.join(subdir, file1), "r")
		var1 = eval(f.read())
		f.close()
		a = np.array(var1)
		count_matrix = count_matrix + a

np.set_printoptions(threshold = 'nan')
count_matrix = count_matrix.tolist()
transition_matrix = []
for i in range(128):
	suma = sum(count_matrix[i])
	if suma == 0:
		transition_matrix.append(count_matrix[i])
		continue
	cols = []
	for j in range(128):
		cols.append(count_matrix[i][j] / suma)
		
	transition_matrix.append(cols)
	
f = open("transition_probability_matrix.txt", "w")
f.write(str(transition_matrix))
f.close()


