# unidirectional relationship between nodes
# methods:
# insert
# prepend
# append
# pop
# find

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.next = None
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 1:
            self.head.next = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        temp = None
        temp = new_node
        temp.next = self.head
        self.head = new_node
        self.length += 1
        return True

    def insert(self, position, value):
        new_node = Node(value)
        if position > self.length:
            print("Position out of bounds")
            return False
        if position <= self.length:
            positionCount = 0
            prev = self.head
            temp = self.head.next
            while positionCount != position-2:
                prev = temp
                temp = temp.next
                positionCount += 1
            
            if temp == None:
                self.append(value)

            prev.next = new_node
            new_node.next = temp
        self.length += 1
        return True

    def pop(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            prev = temp
            temp = temp.next

        prev.next = None
        self.length -= 1
        return temp.value

    def find(self, value):
        temp = self.head
        linked_list_array = []
        while temp is not None:
            linked_list_array.append(temp.value)
            temp = temp.next

        if value in linked_list_array:
            return True
        else:
            return False

my_list = LinkedList(5)
my_list.append(4)
my_list.append(7)
my_list.append(9)
my_list.insert(3, 11)
print("-----")
my_list.print_list()
