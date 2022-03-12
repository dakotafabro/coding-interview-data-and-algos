# real-world application/visualization - classroom: assigning students their line order number based on their names and favorite color
# hash-key - __hash
# set-value
# get-value
# print
# keys

class Hash:
    def __init__(self, size):
        self.table = [None] * size;

    def print_table(self):
        for i, val in enumerate(self.table):
            print(f"{i} : {val}")
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.table)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.table[index] == None:
            self.table[index] = []
        self.table[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.table[index] is not None:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    return self.table[index][i][1]
        return None
    
    def keys(self):
        all_keys =[]
        for i in range(len(self.table)):
            if self.table[i] is not None:
                for j in range(len(self.table[i])):
                    all_keys.append(self.table[i][j][0])
        return all_keys

my_hash_table = Hash(7)

my_hash_table.set_item("apples", 50)
my_hash_table.set_item("bananas", 75)
my_hash_table.set_item("oranges", 35)

print(my_hash_table.keys())


