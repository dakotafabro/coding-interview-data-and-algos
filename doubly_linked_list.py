# bidirectional relationship between nodes
# methods
# insert
# prepend
# append
# remove
# pop
# pop_first
# find

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            while temp.next is not None:
                temp = temp.next
            
            temp.prev.next = None
            temp.prev = None
            self.length -= 1
            return temp

    def pop_first(self):
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
            self.length -= 1
            return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            return False
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True

    def insert(self, position, value):
        new_node = Node(value)
        temp = self.head
        if position == 1:
            self.prepend(new_node)
        if position > self.length or position < 0:
            print("Position out of bounds")
            return False

        for _ in range(position-1):
            temp = temp.next

        new_node.prev = temp.prev
        new_node.next = temp
        temp.prev.next = new_node
        temp.prev = new_node
        self.length += 1
        return True

    def find(self, value):
        temp = self.head
        valuesList = []

        for _ in range(self.length):
            valuesList.append(temp.value)
            temp = temp.next
        
        if value in valuesList:
            return True
        else:
            print("Value not found")
            return False

    def remove_value(self, value):
        valuePresent = self.find(value)
        temp = self.head
        if valuePresent == False:
            return False
        elif value == self.head.value:
            self.pop_first()
        elif value == self.tail.value:
            self.pop()
        else:
            while temp.value != value:
                temp = temp.next

            temp.next.prev = temp.prev
            temp.prev.next = temp.next
            temp.prev = None
            temp.next = None

            self.length -= 1
            return temp



my_double_list = DoublyLinkedList(5)
my_double_list.append(26)
my_double_list.append(22)
my_double_list.append(14)
my_double_list.append(9)
my_double_list.append(6)

my_double_list.print_list()
print("---")
#put new methods below to test
my_double_list.remove_value(11)
my_double_list.print_list()