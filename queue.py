# real-world application/visualization - classroom: lining students up as they enter classroom
# enqueue (adding people to line)
# dequeue (removing people from line)
# insert (cutting in line)
# edge cases: 1 person in line & no people in line

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.front = new_node
        self.end = new_node
        self.length = 1

    def print_queue(self):
        temp = self.front
        if self.length == 0:
            print("Queue empty")
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        temp = self.end
        if self.length == 1:
            temp.next = new_node
            self.end = new_node
            return True
        temp.next = new_node
        self.end = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 1:
            temp = self.front
            self.front == None
            self.end == None
            self.length -= 1
            return temp

        prev = self.front
        temp = self.front.next
        self.front.next = None
        self.front = temp
        self.length -= 1
        return prev

    
class_line = Queue("Auggie")
class_line.enqueue("Paige")
class_line.enqueue("Koda")

class_line.print_queue()
print("---")

class_line.dequeue()
class_line.dequeue()
class_line.dequeue()
class_line.dequeue()
print("---")

class_line.print_queue()