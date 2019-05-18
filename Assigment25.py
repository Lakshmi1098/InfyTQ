

# Function to demonstrate printing pattern 
def pypart(n): 
	myList = [] 
	for i in range(n,0,-1): 
		myList.append("*"*i) 
	print("\n".join(myList)) 

# Driver Code 
n = 5
pypart(n) 
