
def flipBit(a): 
	if a == '1': 
		return '0'; 
	elif a == '0': 
		return '1'; 
	else: 
		raise ValueError('flipBit(): this bit is not 0 or 1'); 
