def name(one,i):
	if i<one:
		return
	print(i)
	name(one,i-1)
	
# Recursion Tree
# let n=3
# f(1,3) -> f(1,2) -> f(1,1) -> f(1,0) Base Condition True

# TC = O(n) Time Complexity
# SC = O(n) Space Complexity/ Stack Space used

# OR

def name1(i,n):
	if i<1:
		return
	print(i)
	name1(i-1,n)
	
if __name__ == "__main__":
	n = int(input("Enter N: "))
	name(1,n)
	print("----")
	name1(n,n)
	
# Recursion Tree
# let n=3
# f(3,3) -> f(2,3) -> f(1,3) -> f(0,3) Base Condition True

# TC = O(n) Time Complexity
# SC = O(n) Space Complexity/ Stack Space used

