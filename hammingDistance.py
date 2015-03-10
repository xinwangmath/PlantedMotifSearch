
def hammingDistance(s1, s2): 
	l = len(s1); 
	if l != len(s2): 
		raise ValueError('hammingDistance(s1, s2): s1 and s2 have different length')
	else: 
		return sum( s1[i] != s2[i] for i in range(l) )