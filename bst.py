# real-world application/visualization - classroom: You organize the teachers on your staff by age,
# with your own age being the age of reference (root)
# insert
# contains
# find min-value (youngest teacher)
# search - breadth first search, dfs-preorder, dfs-inorder, dfs-postorder


class Teacher:
    def __init__(self, age):
        self.age = age
        self.younger = None
        self.older = None

class TeacherOrg:
    def __init__(self):
        self.root = None

    def insert(self, age):
        new_teacher = Teacher(age)
        if self.root is None:
            self.root = new_teacher
            return True
        
        temp = self.root
        while(True):
            if new_teacher.age == temp.age:
                return False

            if new_teacher.age < temp.age:
                if temp.younger is None:
                    temp.younger = new_teacher
                    return True
                temp = temp.younger
            else:
                if temp.older is None:
                    temp.older = new_teacher
                    return True
                temp = temp.older

    def contains(self, age):
        temp = self.root
        while temp is not None:
            if age < temp.age:
                temp = temp.younger
            elif age > temp.age:
                temp = temp.older
            else:
                return True
        return False

    def youngest_teacher(self, current_teacher):
        while current_teacher.younger is not None:
            current_teacher = current_teacher.younger
        return current_teacher.age

# methods below all access the tree itself and do not need parameters passed
# methods print out tree in a specific order

    def breadth_first_search(self):
        current_teacher = self.root
        queue = []
        results = []
        queue.append(current_teacher)

        while len(queue) > 0:
            current_teacher = queue.pop(0)
            results.append(current_teacher.age)
            if current_teacher.younger is not None:
                queue.append(current_teacher.younger)
            if current_teacher.older is not None:
                queue.append(current_teacher.older)
        return results

    def dfs_preorder(self):
        results = []

        def traverse(current_teacher):
            results.append(current_teacher.age)
            if current_teacher.younger is not None:
                traverse(current_teacher.younger)
            if current_teacher.older is not None:
                traverse(current_teacher.older)
            
        traverse(self.root)
        return results

    def dfs_inorder(self):
        results = []

        def traverse(current_teacher):
            if current_teacher.younger is not None:
                traverse(current_teacher.younger)
            results.append(current_teacher.age)
            if current_teacher.older is not None:
                traverse(current_teacher.older)
            
        traverse(self.root)
        return results

    def dfs_postorder(self):
        results = []

        def traverse(current_teacher):
            if current_teacher.younger is not None:
                traverse(current_teacher.younger)

            if current_teacher.older is not None:
                traverse(current_teacher.older)
            results.append(current_teacher.age)
            
        traverse(self.root)
        return results

    
my_tree = TeacherOrg() ## creates the empty tree
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.breadth_first_search())
print(my_tree.dfs_preorder())
print(my_tree.dfs_inorder())
print(my_tree.dfs_postorder())