import numpy as np
import re as re

def calculate(list):
	if len(list)!=9:
		raise ValueError("List must contain nine numbers.")
	for num in list: 
		if re.match(str(num), '\D')!= None: 
			raise ValueError("List must only contain numbers.")
	matrix = np.array(list).reshape(3,3)
	calculations = {}
	calculations['mean'] = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix)]
	calculations['variance'] = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix)]
	calculations['standard deviation'] = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix)]
	calculations['max'] = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix)]
	calculations['min'] = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix)]
	calculations['sum'] = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix)]
	return calculations