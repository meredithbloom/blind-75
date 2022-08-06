# 104. Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Constraints
'''
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''

import math

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class BinaryTree:
	def __init__(self):
		self.root = None
		self.depth = 0

	def insert(self, val):
		new = TreeNode(val)
		if self.root == None:
			self.root = new
			return
		temp = self.root
		while True:
			if val < temp.val:
				if temp.left == None:
					temp.left = new
					return 
				else: 
					temp = temp.left
			elif val > temp.val:
				if temp.right == None:
					temp.right = new
					return
				else:
					temp = temp.right

	def traverse(self):
		if self.root != None:
			start = self.root
			temp = self.root
			while True:
				
				
				







def maxDepth(root):
	total = len(root) + 1
	print(int(math.log2(total)))
	return int(math.log2(total))
	



root1 = [3,9,20,None,None,15,7]
root2 = [1,None,2]

maxDepth(root1)
maxDepth(root2)