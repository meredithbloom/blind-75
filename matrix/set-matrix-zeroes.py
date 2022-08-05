# 73. Set Matrix Zeroes

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

#You must do it in place. DO NOT RETURN ANYTHING.

# Constraints
'''
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
'''

# Follow-up
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
# [[1,0,1],[0,0,0],[1,0,1]]

matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

import numpy as py




def setZeroes(matrix):
	# num rows
	m = len(matrix)
	# number of columns
	n = len(matrix[0])
	rows = {}
	cols = {}
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 0:
				rows[i] = 0
				cols[j] = 0
	print(rows, cols)
	for r in rows.keys():
		matrix[r] = [0 for x in matrix[r]]
	for c in cols.keys():
		print(f'need to change all elements in col {c} to 0')
		for row in matrix:
			row[c] = 0
	print(matrix)
	
		


setZeroes(matrix1)
setZeroes(matrix2)