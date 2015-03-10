# a simple motif search implementation
from dataStructures import Stack
from hammingDistance import hammingDistance
from treeNode import TreeNode
from toBinary import toBinary
from flipBit import flipBit

def stackPMS(integerList, l, d):

	n = len(integerList); 
	a = integerList[0]; 
	a = toBinary(a, l); 

	treeStack = Stack()
	candidate = Stack()
	solution = Stack()

	
	c = TreeNode(a[0], 0)
	treeStack.push(c); 
	c = TreeNode(flipBit(a[0]), 1)
	treeStack.push(c); 


	while not treeStack.isEmpty(): 
		c = treeStack.pop();
		cs = c.getValue(); 
		cc = c.getCount(); 

		if (c.getCount() < d and len(cs) < l): 
			b1s = cs + a[len(cs)]; 
			b1c = cc; 
			b2s = cs + flipBit(a[len(cs)]); 
			b2c = cc + 1; 
			treeStack.push(TreeNode(b1s, b1c))
			treeStack.push(TreeNode(b2s, b2c))
		else: 
			if len(cs) < l: 
				cand = cs + a[len(cs):]
			else: 
				cand = cs; 

			candidate.push(cand); 


	while not candidate.isEmpty(): 
		cand = candidate.pop()
		flag = True
		j = 1; 
		while flag and (j < n): 
			flag = ( hammingDistance(cand, toBinary(integerList[j], l)) <= d )
			j += 1; 
		if flag: 
			solution.push(cand)

	return solution; 


# function definition ends #

if __name__ == "__main__": 
	integerList = [0, 15, 5]
	l = 4; 
	d = 2; 
	solution = stackPMS(integerList, l, d); 
	print solution; 








