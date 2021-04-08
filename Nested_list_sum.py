# Python Program to find sum 
# of nested list using Recursion 

# this will store the required sum 
total = 0

def sum_nestedlist( l ): 
	
	# specify that global variable is 
	# referred to here in this function 
	global total 
	
	for j in range(len(l)): 
		
		if type(l[j]) == list : 
			
			# call the same function if 
			# the element is a list 
			sum_nestedlist(l[j]) 
		else: 
			
			# if it's a single element 
			# and not a list, add it to total 
			total += l[j] 
			
sum_nestedlist([[1,2,3],[4,[5,6]],7]) 
print(total) 
