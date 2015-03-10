
class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, v = None, t = 0):
		self._value = v; 
		self._count = t; 
	def getValue(self): 
		return self._value; 
	def setValue(self, s): 
		self._value = s; 
	def getCount(self):
	    return self._count; 
	def setCount(self, t): 
	    self._count = t; 	