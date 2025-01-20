# ************* LinkedList *************
# Create LinkedList and Node classes
# LinkedList class should have append, prepend, pop_first, pop, get, set_value, insert, remove, reverse, and print_list methods
""" Also do
    find_middle_node()
    has_loop()
    find_kth_from_end()
    partition_list()
    remove_duplicates()
    binary_to_decimal()
    reverse_between()
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def pop(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is None:
            return False
        temp.value = value
        return True
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        pre = self.get(index - 1)
        new_node = Node(value)
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def partition_list(self):
        pass

    def reverse_between(self, start, end):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(start):
            prev = prev.next

        current = prev.next

        for _ in range(end - start):
            node_to_move = current.next #4
            current.next = node_to_move.next #5
            node_to_move.next = prev.next #3
            prev.next = node_to_move
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.append(5)
my_ll.print_list()
print('-------')
print(my_ll.find_middle_node())
my_ll.reverse()
my_ll.print_list()

# ************* Doubly Linked List *************
# Create DoublyLinkedList and Node classes
# DLL class should have append, pop, prepend, pop_first, get, set_value, insert, remove, and print_list methods
""" Also do
    swap_first_last()
    reverse()
    is_palindrome()
    pairwise_swap_values()
    pairwise_swap_nodes()
"""

# ************* Stacks & Queues *************
# Create Stack, Queues, and Node classes
# Stack class should have push, pop, and print_stack
# Queue class should have enqueue, dequeue, and print_queue
""" Also do for stack
    is_balanced_parentheses()
    reverse_string()
    sort_stack()
    size()
    is_empty()
"""
""" Also do for queue usiing stack (e.g. stack1, stack2)
    enqueue()
    dequeue()
    peek()
    is_empty()
"""

# ************* Trees *************
# Create BinarySearchTree and Node classes
# BinarySearchTree class should have insert and contains

# ************* Hash Tables *************
# Create HashTable class
# HashTable class should have __hash, set_item, get_item, get_keys, print_table
""" Also outside HashTable class do
    item_in_common
    find_duplicates
    first_non_repeating_char
    group_anagrams
    two_sum
    subarray_sum
    remove_duplicates
    has_unique_chars
    find_pairs
    longest_consecutive_sequence
"""

# ************* Graphs *************
# Create Graph class
# Graph class should have add_vertex, add_edge, remove_edge, remove_vertex, print_graph
""" Also outside HashTable class do
    item_in_common
    find_duplicates
    first_non_repeating_char
    group_anagrams
    two_sum
    subarray_sum
    remove_duplicates
    has_unique_chars
    find_pairs
    longest_consecutive_sequence
"""
