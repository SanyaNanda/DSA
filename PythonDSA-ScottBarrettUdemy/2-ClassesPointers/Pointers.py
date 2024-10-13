num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2)) 

num2 = 22 

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2) 

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))


# OUTPUT 1:
# Before num2 value is updated:
# num1 = 11
# num2 = 11

# num1 points to: 140714625420024
# num2 points to: 140714625420024

# After num2 value is updated:
# num1 = 11
# num2 = 22

# num1 points to: 140714625420024
# num2 points to: 140714625420376

# Conclusion - Numbers are immutable


#####################################


dict1 = {
         'value': 11
        }

dict2 = dict1 

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# OUTPUT 2:
# Before value is updated:
# dict1 = {'value': 11}
# dict2 = {'value': 11}

# dict1 points to: 2188871626240
# dict2 points to: 2188871626240

# After value is updated:
# dict1 = {'value': 22}
# dict2 = {'value': 22}

# dict1 points to: 2188871626240
# dict2 points to: 2188871626240

# Conclusion -  dictionary is immutable