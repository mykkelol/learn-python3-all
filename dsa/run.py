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

        for _ in range(start):
            prev = prev.next
        current = prev

        for _ in range(end):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

        self.head = dummy_node.next

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
print('-----------------')
my_ll.remove_duplicates()
my_ll.print_linked_list()
print('-----------------')
my_ll.reverse_between(1,4)
print('-----------------')
my_ll.print_linked_list()