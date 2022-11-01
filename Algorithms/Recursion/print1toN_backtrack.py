def name(i,n):
	if i<1:
		return
	name(i-1,n)
	print(i) 
	
if __name__ == "__main__":
	n = int(input("Enter N: "))
	name(n,n)
	
# Recursion Tree
# let n=3
# f(3,3) -> f(2,3) -> f(1,3) -> f(0,3) Base Condition True 
# Then print 1 -> 2 -> 3
# Last function call executes first

# TC = O(n) Time Complexity
# SC = O(n) Space Complexity/ Stack Space used
