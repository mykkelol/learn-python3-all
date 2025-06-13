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
    
    def pop(self):
        if self.length == 0:
            return None
        
        if self.length == 1:
            temp = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        
        temp = self.head
        pre = None
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
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length - 1:
            return self.append(value)
        new_node = Node(value)
        pre = self.get(index - 1)
        new_node.next = pre.next
        pre.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = pre.next.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        # 1 > 2 > 3 > 4 > None
        # None < 1 < 2 < 3 < 4
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_node(self):
        slow = fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def find_middle_node_naive(self):
        temp = self.head
        for _ in range(self.length // 2):
            temp = temp.next
        return temp

    def has_loop(self):
        slow = fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def find_kth_from_end_naive(self, k):
        if k <= 0 or k > self.length:
            return -1
      
        position_from_end = self.length - k
        temp = self.head

        for _ in range(position_from_end):
            temp = temp.next
        
        return temp

    def find_kth_from_end(self, k):
        if k < 0 or self.head is None:
            return None
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
        if self.head is None:
            return None
        
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2

        current = self.head
        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next
        
        prev1.next = prev2.next
        prev2.next = None

        return prev1.next
    
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
        decimal = 0
        temp = self.head
        while temp:
            decimal = decimal * 2 + temp.value
            temp = temp.next
        return decimal

    def reverse_between(self, start, end):
        # (1, 3) in: dummy → 1 → 2 → 3 → 4 → 5 → 6
        # (1, 3) out: dummy → 1 → 4 → 3 → 2 → 5 → 6
        if self.length <= 1:
            return None
        
        dummy_node = Node(0)
        dummy_node.next = self.head
        prev = dummy_node

        for _ in range(start):
            prev = prev.next

        current = prev.next

        for _ in range(end - start):
            node_to_move = current.next
            current.next = node_to_move.next
            node_to_move.next = current
            prev.next = node_to_move

        self.head = dummy_node.next


    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(3)
my_ll.append(4)
my_ll.print_ll()
print(my_ll.find_middle_node().value)
print(my_ll.find_middle_node_naive().value)
print(my_ll.has_loop())

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
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        if self.length == 0:
            self.head = None
            self.tail = None
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
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _  in range(self.length - 1, index, -1):
                temp = temp.prev
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
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index)

        new_node.next = temp
        new_node.prev = temp.prev
        temp.prev.next = new_node
        temp.prev = new_node

        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.lenght:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

        self.length -= 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def swap_first_last(self):
        if self.length == 0:
            return False
        self.head.value, self.tail.value = self.tail.value, self.head.value
        return True
    
    def reverse(self):
        if self.length <= 1:
            return False
        temp = self.head
        while temp:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        self.head, self.tail = self.tail, self.head
        return True

    def is_palindrome(self):
        if self.length <= 1:
            return False
        front = self.head
        back = self.tail
        for _ in range(self.length // 2):
            if front.value is not back.value:
                return False
            front = front.next
            back = back.prev
        return True
    
    def pairwise_swap_values(self):
        if self.length < 0:
            return False
        temp = self.head
        while temp and temp.next:
            temp.value, temp.next.value = temp.next.value, temp.value
            temp = temp.next
        return True
    
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

def Stack(self, value):
    new_node = Node(value)
    self.top = new_node
    self.height = 1

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    
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
