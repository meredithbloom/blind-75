# 98. Validate Binary Search Tree
'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

# Constraints
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


		
# using breadth first search
def isValidBST(root: [TreeNode]):
	# current = root[0]
	# mylist = root
	# myqueue = []
	# myqueue.append(current)
	depth = log2(len(root)+1) 
	
	print(depth)
		
	
	
	
	
	






# list is BFS

# using a stack and queue
	
tree1 = [2,1,3]
tree2 = [5,1,4,'null','null',3,6]

isValidBST(tree1)
isValidBST(tree2)