def name(i,n):
	if i>n:
		return
	print(i)
	name(i+1,n)
	
if __name__ == "__main__":
	n = int(input("Enter N: "))
	name(1,n)
	
# Recursion Tree
# let n=3
# f(1,3) -> f(2,3) -> f(3,3) -> f(4,3) Base Condition True

# TC = O(n) Time Complexity
# SC = O(n) Space Complexity/ Stack Space used
