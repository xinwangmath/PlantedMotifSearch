# create common data structures

class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self._items = []; 
		self._size = 0; 

	def push(self, item):
		self._items.append(item);
		self._size += 1

	def pop(self):
		if self._size == 0: 
			raise KeyError('pop(): stack is empty'); 
		else: 
			self._size -= 1
			return self._items.pop()

	def isEmpty(self): 
		return (self._size == 0); 

	def __str__(self):
		return str(self._items); 


# End of stack definition #

if __name__ == '__main__': 
	a = Stack()
	a.push(2)
	a.push('c')
	a.push(2.5)
	print a
	print a.isEmpty(); 

	a.pop(); 
	a.pop(); 
	print a
	a.pop()
	print a

	print a.isEmpty(); 
		
