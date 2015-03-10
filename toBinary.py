
def toBinary(a,n): 
	""" convert an integer n into a n-bit string of 0 and 1 representing the binary of a """
	s = bin(a)[2:]; 
	if len(s) < n: 
		s1 = '0'*(n-len(s)); 
		s = s1 + s; 
	return s; 


# end of function definition #

if __name__ == '__main__': 
	a = (int)(raw_input("please enter an integer")); 
	n = 10; 
	print toBinary(a, n); 
