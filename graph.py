# graphs as an adjacency matrix
# better for space and time complexity because it doesn’t store zeros
# add vertex
# add edge (or connection)
# remove edge
# remove vertex

class Graph:
    def __init__(self):
        self.matrix = {}
	
    def add_vertex(self, v1):
        if v1 not in self.matrix.keys():
            self.matrix[v1] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.matrix.keys() and v2 in self.matrix.keys():
            try:
                self.matrix[v1].append(v2)
                self.matrix[v2].append(v1)
            except ValueError:
                pass
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.matrix.keys() and v2 in self.matrix.keys():
            try:
                self.matrix[v1].remove(v2)
                self.matrix[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
	
    def remove_vertex(self, v1):
        if v1 in self.matrix.keys():
            for other_vertex in self.matrix[v1]:
                self.matrix[other_vertex].remove(v1)
            del self.matrix[v1]
            return True
        return False
