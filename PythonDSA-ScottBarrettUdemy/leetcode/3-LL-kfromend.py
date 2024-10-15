class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

def find_kth_from_end(ll, k):
    slow = fast = ll.head   
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
 
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)
print(result.value)  
# Output: 4

# Refer - To remove the kth node on leetcode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Slight logic change

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(self, n: int):
    slow = fast =  self.head
    if fast.next is None:
        return None
    for _ in range(n):
        fast = fast.next
    if fast == None:
        return head.next
    while(fast and fast.next):
        fast = fast.next
        slow = slow.next
    if slow.next and slow.next.next:
        slow.next = slow.next.next
    else:
        slow.next = None
    return self.head