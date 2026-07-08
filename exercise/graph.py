class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self ,vertex):

        if vertex is not self.graph:
            self.graph[vertex] = set()   

    def add_edge(self, v1 ,v2):

        if v1 not in self.graph:
            self.add_vertex(v1)

        if v2 not in self.graph:
            self.add_vertex(v2)


        self.graph[v1].add(v2)
        self.graph[v2].add(v1)

    def display(self):

        for vertex in self.graph:
            print(vertex, "->" ,self.graph[vertex])


    def remove(self , v1, v2):
        if v1 not in self.graph or v2 not in self.graph:
            return
        
        if v2 in self.graph[v1]:
            self.graph[v1].remove(v2)

        if v1 in self.graph[v2]:
            self.graph[v2].remove(v1)



g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")


g.add_edge("A", "B")
g.add_edge("A","C")
g.add_edge("B","D")
g.add_edge("C","D")


g.remove("A","B")

g.display()