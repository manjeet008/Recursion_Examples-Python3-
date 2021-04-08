def power(N, P): 

	# if power is 0 or 1 then number is returned 
	if(P == 1): 
		return N
	elif(P == 0):
		return (1)
	else: 
		return (N*power(N, P-1)) 

# Driver program 
N = 5
P = 0

print(power(N, P))
