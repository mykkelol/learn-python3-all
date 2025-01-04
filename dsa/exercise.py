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
        self.length -= 1
        return temp
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = None
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
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
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length - 1:
            self.append(value)
        new_node = Node(value)
        pre = self.get(index - 1)
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.pop_first()
        if index == self.length - 1:
            self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self):
        slow = slow.head
        fast = fast.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def find_kth_from_end_naive(self, k):
        if k < 0:
            return -1
        if k == 1:
            return self.tail
        if k == self.length:
            return self.head 
        i = 0
        temp = self.head
        while temp:
            if self.length - i == k:
                return temp
            else:
                i += 1
                temp = temp.next
        return -1
    
    def find_kth_from_end(self, k):
        if k < 0:
            return -1
        if k == 1:
            return self.tail
        if k == self.length:
            return self.head
        slow = fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
    
    def partition_list(self, x):
        current = self.head
        if current is None:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        prev1.next = None
        prev2.next = None

    def remove_duplicates(self):
        if self.head is None:
            return None
        current = self.head
        prev = None
        values = set()
        while current:
            if current.value in values:
                prev.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
            prev = current
            current = current.next

    def binary_to_decimal(self):
        pass

    def reverse_between(self, start, end):
        if self.length <= 1:
            return None
        if end >= self.length or start < 0 or start >= end:
            return None

        dummy_node = Node(0)
        dummy_node.next = self.head
        prev = dummy_node

        """ 
        1 > 2 > 3 > 4 > 5
        0 > 1 > 2 > 3 > 4
        (1,3)

        prev = NULL
        
        prev = 0(1)
        current = 1(2)
        temp = 2(3)

        1st iteration: 0 > 1 > 2 > 1 > 4 and prev.next becomes node 2
        2nd iteration: 0 > 1 > 2 > 1 > 4 and prev.next becomes node 2
        """

        for _ in range(start):
            prev = prev.next
        
        # node 2(3)
        current = prev.next

        for _ in range(end - start):
            # node 3(4)
            temp = current.next
            # node 3(4) becomes node 4(3)
            current.next = temp.next
            # node 4(3) becomes node 4(3)
            temp.next = prev.next
            prev.next = temp

    def print_linked_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.append(4)
my_ll.append(5)
my_ll.print_linked_list()
my_ll.remove_duplicates()
my_ll.print_linked_list()

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
        dummy_node = Node(4)
        pass
    
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
my_dll.reverse()
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
