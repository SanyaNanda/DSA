class Node:
    """This class creates a node that is used to 
    create the nodes in the linked list"""

    # Constructor
    def __init__(self, value):
        self.value = value # value
        self.next = None   # pointer
        

class LinkedList:
    # Constructor
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Method 1: Print the linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    # Method 2: Append to the LL
    def append(self, value):
        # create new node
        new_node = Node(value)
        # when LL is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # When LL is not empty
        else:
            self.tail.next = new_node
            self.tail = new_node
        # Increment length of LL
        self.length += 1
        # return true used by insert method later
        return True

    # Method 3: Pop last node from LL
    def pop(self):
        # Case 1: LL has no nodes
        if self.length == 0:
            return None
        # Case 2: LL has 2 or more nodes
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # Case 3: LL has only 1 node
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    # Method 4: Prepend to the LL
    def prepend(self, value):
        new_node = Node(value)
        # Case 1: LL is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # Case 2: LL is not empty
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # Method 5: Pop the first node from LL
    def pop_first(self):
        # Case 1: LL is empty
        if self.length == 0:
            return None
        # Case 2: LL has 2 or more node
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # Case 3: LL has 1 node
        if self.length == 0:
            self.tail = None
        return temp
    
    # Method 6: Get the value at a given index
    def get(self, index):
        # Check validity of the index provided
        if index < 0 or index >= self.length:
            return None
        # Get the node on the index position provided
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    # Method 7: Set the value at a given index    
    def set_value(self, index, value):
        # Use the get method to get the node at the given index and update its value
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # Method 8: Insert a node at the given index (beginning, middle or end)    
    def insert(self, index, value):
        # check the the index is in valid bounds
        if index < 0 or index > self.length:
            return False
        # To insert in the beginning, use preprend (note prepend return true)
        if index == 0:
            return self.prepend(value)
        # To insert in the end, use append (note append return true)
        if index == self.length:
            return self.append(value)
        # To insert in the middle
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    # Method 9: Remove a node from the given index (beginning, middle or end)  
    def remove(self, index):
        # check the index is in valid bounds
        if index < 0 or index >= self.length:
            return None
        # To remove from the beginning (note the removed node is returned)
        if index == 0:
            return self.pop_first()
        # To remove from the end (note the removed node is returned)
        if index == self.length - 1:
            return self.pop()
        # To remove from the middle
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # Method 10: Reverse the LL
    def reverse(self):
        # swap head and tail using temp
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        # create 3 pointers before, temp and after
        after = temp.next
        before = None

        # Follow this to reverse the order of list
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

# Using the above defined classes and their methods
print("Constructing the LL")
my_linked_list = LinkedList(1)
my_linked_list.print_list()
# 1 -> None

print("Append to the LL")
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
# 1 -> 2 -> 3 -> 4 -> None

print("Pop from the LL")
print(my_linked_list.pop())
my_linked_list.print_list()
# 1 -> 2 -> 3 -> None

print("Prepend to the LL")
my_linked_list.prepend(0)
my_linked_list.print_list()
# 0 -> 1 -> 2 -> 3 -> None

print("Pop First from the LL")
my_linked_list.pop_first()
my_linked_list.print_list()
# 1 -> 2 -> 3 -> None

print("Get 5th node from the LL")
print(my_linked_list.get(5))
# None
print("Get -1 node from the LL")
print(my_linked_list.get(5))
# None
print("Get 2nd node from the LL")
print(my_linked_list.get(2).value)
# 3

print("Set 2nd node in the LL")
print(my_linked_list.set_value(2,50))
my_linked_list.print_list()
# 1 -> 2 -> 50 -> None

print("Insert in the LL")
print(my_linked_list.insert(4,11)) # False
print(my_linked_list.insert(3,11)) # True
print(my_linked_list.insert(0,12)) # True
print(my_linked_list.insert(10,12)) # False
print(my_linked_list.insert(-1,12)) # False
my_linked_list.print_list()
# 12 -> 1 -> 2 -> 50 -> 11 -> None

print("Insert in the LL")
print(my_linked_list.remove(4).value)
print(my_linked_list.remove(4))
print(my_linked_list.remove(-1))
my_linked_list.print_list()
# 12 -> 1 -> 2 -> 50 -> None

print("Reverse the LL")
my_linked_list.reverse()
my_linked_list.print_list()
# 50 -> 2 -> 1 -> 12


# OUTPUT:
# Constructing the LL
# 1
# Append to the LL
# 1
# 2
# 3
# 4
# Pop from the LL
# <__main__.Node object at 0x000002563B8C9EE0>
# 1
# 2
# 3
# Prepend to the LL
# 0
# 1
# 2
# 3
# Pop First from the LL
# 1
# 2
# 3
# Get 5th node from the LL
# None
# Get -1 node from the LL
# None
# Get 2nd node from the LL
# 3
# Set 2nd node in the LL
# True
# 1
# 2
# 50
# Insert in the LL
# False
# True
# True
# False
# False
# 12
# 1
# 2
# 50
# 11
# Insert in the LL
# 11
# None
# None
# 12
# 1
# 2
# 50
# Reverse the LL
# 50
# 2
# 1
# 12