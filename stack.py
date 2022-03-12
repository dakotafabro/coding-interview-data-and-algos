# real-world application/visualization - classroom: grading a stack of papers
# initialize
# push (add to stack)
# pop (take from top of stack)
# edge cases: nothing in the stack

class Homework:
    def __init__(self,value):
        self.value = value
        self.next = None

class PaperStack:
    def __init__(self, value):
        new_homework = Homework(value)
        self.top = new_homework
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        if self.height == 0:
            self.__init__(value)
        else:
            new_homework = Homework(value)
            new_homework.next = self.top
            self.top = new_homework
            self.height += 1

    def pop(self):
        if self.height == 0:
            print("Grading finished!")
            return None
        else:
            temp = self.top
            self.top = self.top.next if self.height > 0 else None
            temp.next = None
            self.height -= 1
            return temp

papers_to_grade = PaperStack("Math")
papers_to_grade.push("Science")
papers_to_grade.push("History")
papers_to_grade.push("ELA")


papers_to_grade.print_stack()

