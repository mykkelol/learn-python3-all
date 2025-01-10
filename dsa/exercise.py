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
        pass

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

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            new_node.prev = self.tail
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
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is None:
            return False
        temp.value = value
        return True
    
    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index)

        new_node.next = temp
        new_node.prev = temp.prev
        temp.next = None
        
        self.length += 1
        return new_node
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return True
    
    def swap_first_last(self):
        if self.length <= 1:
            return False
        self.head.value, self.tail.value = self.tail.value, self.head.value
        return True
    
    def reverse(self):
        temp = self.head
        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        self.head, self.tail = self.tail, self.head
        return True

    def reverse_values(self):
        if self.length <= 1:
            return False
        nodes = {}
        current = self.head
        length = self.length
        for i in range(length):
            if i < length // 2: 
                nodes[length - i - 1] = current
            else:
                if nodes.get(i):
                    nodes[i].value, current.value = current.value, nodes[i].value
            current = current.next
        return True
    
    def is_palindrome(self):
        if self.length <= 0:
            return True
        front = self.head
        back = self.tail
        for _ in range(self.length // 2):
            if front.value is not back.value:
                return False
            front = front.next
            back = back.prev
        return True
    
    def pairwise_swap_values(self):
        temp = self.head
        while temp and temp.next:
            temp.value, temp.next.value = temp.next.value, temp.value
            temp = temp.next

    def pairwise_swap_nodes(self):
        # 1 ↔ 2 ↔ 3 ↔ 4
        # dummy → 1 ↔ 2 ↔ 3 ↔ 4
        dummy_node = Node(0)
        dummy_node.next = self.head
        previous_node = dummy_node

        while self.head and self.head.next:
            first_node = self.head
            second_node = self.head.next

            # dummy → 2 → 1 → 3 ↔ 4
            previous_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # dummy ↔ 2 ↔ 1 → 3 ↔ 4
            second_node.prev = previous_node
            first_node.prev = second_node

            # dummy ↔ 2 ↔ 1 ↔ 3 ↔ 4
            if first_node.next:
                first_node.next.prev = first_node

            # 1 ↔ 3 ↔ 4
            self.head = first_node.next
            previous_node = first_node

        # 2 ↔ 1 ↔ 4 ↔ 3
        self.head = dummy_node.next

        if self.head:
            self.head.prev = None

    def pairwise_swap(self):
        # dummy → 1 ↔ 2 ↔ 3 ↔ 4
        dummy_node = Node(0)
        dummy_node.next = self.head
        prev = dummy_node

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # dummy → 2 → 1 → 3 ↔ 4
            prev.next = second
            first.next = second.next
            second.next = first
            
            # dummy ↔ 2 ↔ 1 ↔ 3 ↔ 4
            second.prev = prev
            first.prev = second
            if first.next:
                first.next.prev = first

            prev = first

        # 2 ↔ 1 ↔ 4 ↔ 3
        self.head = dummy_node.next
        self.head.prev = None
        
    def print_doubly(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)
my_dll.print_doubly()
my_dll.pairwise_swap()
my_dll.print_doubly()

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
