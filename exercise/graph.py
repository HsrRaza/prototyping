from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self ,vertex):

        if vertex not in self.graph:
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


            # graph travsersal using dfs

    def dfs(self, vertex , visited):
        visited.add(vertex)
        print(vertex)

        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs(neighbour ,visited)


    #  dfs using traverse def

    def dfss(self, vertex):
        visited = set()

        def traverse(vertex):

            visited.add(vertex)
            print(vertex)

            for neighbour in self.graph[vertex]:

                if neighbour not in visited:
                    traverse(neighbour)
            
        traverse(vertex)
#  bfs traversal
    
    def bfs(self):
        visited =set()
        queue =deque()
        ans =[]

        visited.add("A")
        queue.append("A")

        while queue:
            node  =queue.popleft()
            ans.append(node)


            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return ans
    
    # graph cyle check
    

    def has_cycle(self):

        visited = set()

        for vertex in self.graph:
            if vertex not in visited:
                if self.dfs(vertex, visited, None):
                    return True

        return False


    def dfs(self, node, visited, parent):

        visited.add(node)

        for neighbour in self.graph[node]:

            if neighbour not in visited:

                if self.dfs(neighbour, visited, node):
                    return True

            elif neighbour != parent:
                return True

        return False







g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")


g.add_edge("A", "B")
g.add_edge("A","C")
g.add_edge("B" , "D")



g.display()

# visited = set()

# g.dfs("A" ,visited)

g.dfss("A")

adj = [
    [1,2],
    [0,3,4],
    [0,5,6],
    [1],
    [1],
    [2],
    [2]
]

print(g.bfs())