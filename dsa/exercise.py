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
        if self.heaad is None:
            self.head = value
            self.tail = value
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
