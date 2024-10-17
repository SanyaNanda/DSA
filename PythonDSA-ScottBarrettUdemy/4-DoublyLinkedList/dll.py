class Node:
    """This class creates a node that is used to 
    create the nodes in the linked list"""

    # Constructor
    def __init__(self, value):
        self.value = value # value
        self.next = None # next pointer
        self.prev = None # previous pointer
        

class DoublyLinkedList:
    # Constructor
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Method 1: Print the DLL
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    # Method 2: Append to the DLL
    def append(self, value):
        new_node = Node(value)
        # When DLL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # When DLL is not empty
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # Method 3: Pop from DLL
    def pop(self):
        # When DLL is empty
        if self.length == 0:
            return None
        temp = self.tail  
        # When DLL has 1 node
        if self.length == 1:
            self.head = None
            self.tail = None 
        # When DLL has 2 or more nodes
        else:     
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    # Method 4: prepend to the DLL
    def prepend(self, value):
        new_node = Node(value)
        # When DLL is empty, simple add the new node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # else, place the new node at the start of the list
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    # Method 5: pop first node from DLL
    def pop_first(self):
        # DLL is empty
        if self.length == 0:
            return None
        temp = self.head
        # DLL has 1 node
        if self.length == 1:
            self.head = None
            self.tail = None
        # DLL has 2 or more nodes
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None      
        self.length -= 1
        return temp

    # Method 6: get the value on the given index
    # Regular LL method works, but this is further optimized
    def get(self, index):
        # check validity of bounds of index
        if index < 0 or index >= self.length:
            return None
        # if index in first half of the DLL, use head
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        # if index in second half of the DLL, use tail
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
        
    # Method 7: set value on a given index using get
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    # Method 8: Insert at a given index
    def insert(self, index, value):
        # Index validity
        if index < 0 or index > self.length:
            return False
        # Insert in the start, use prepend
        if index == 0:
            return self.prepend(value)
        # Insert at the end, use append
        if index == self.length:
            return self.append(value)

        # Insert in middle
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        
        self.length += 1   
        return True  

    # Method 9: Remove the node from the given index
    def remove(self, index):
        # check index validity
        if index < 0 or index >= self.length:
            return None
        # use pop_first to remove from the start of DLL
        if index == 0:
            return self.pop_first()
        # use pop to remove the last node
        if index == self.length - 1:
            return self.pop()

        # logic to remove a node from the middle of DLL
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
 
        self.length -= 1
        return temp
        
print("Construct a DLL")
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.print_list()
# 1

print("Append to the DLL")
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.print_list()
# 1 - 2 - 3 - 4 - 5

print('Pop from the DLL')
my_doubly_linked_list.pop()
my_doubly_linked_list.print_list()
# 1 - 2 - 3 - 4

print('Prepend to the DLL')
my_doubly_linked_list.prepend(7)
my_doubly_linked_list.print_list()
# 7 - 1 - 2 - 3 - 4

print('pop first from the DLL')
my_doubly_linked_list.pop_first()
my_doubly_linked_list.print_list()
# 1 - 2 - 3 - 4

print('get from the DLL')
print(my_doubly_linked_list.get(3).value)
# 4

print('set from the DLL')
my_doubly_linked_list.set_value(2,4)
my_doubly_linked_list.print_list()
# 1 - 2 - 4 - 4

print("insert to the DLL")
print(my_doubly_linked_list.insert(3,3))
print(my_doubly_linked_list.insert(4,6))
print(my_doubly_linked_list.insert(0,7))
print(my_doubly_linked_list.insert(20,7))
my_doubly_linked_list.print_list()
# 7 - 1 - 2 - 4 - 3 - 6 - 4

print('removed from DLL:')
print(my_doubly_linked_list.remove(2).value)
print(my_doubly_linked_list.remove(0).value)
print(my_doubly_linked_list.remove(2).value)
my_doubly_linked_list.print_list()
# 1 - 4 - 6 - 4

# Expected Output:
# Construct a DLL
# 1
# Append to the DLL
# 1
# 2
# 3
# 4
# 5
# Pop from the DLL
# 1
# 2
# 3
# 4
# Prepend to the DLL
# 7
# 1
# 2
# 3
# 4
# pop first from the DLL
# 1
# 2
# 3
# 4
# get from the DLL
# 4
# set from the DLL
# 1
# 2
# 4
# 4
# insert to the DLL
# True
# True
# True
# False
# 7
# 1
# 2
# 4
# 3
# 6
# 4
# removed from DLL:
# 2
# 7
# 3
# 1
# 4
# 6
# 4