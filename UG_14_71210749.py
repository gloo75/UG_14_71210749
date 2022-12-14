class Node: 
    def __init__(self,name, value):
        self._name = name 
        self._value = value

class Graph:
    def __init__(self):
        #constructor
        self._data = {}

    #menambah vertex (Node) baru ke dalam Graph
    def addVertex(self, key, value):
        if key not in self._data:
            self._data[key] = set()        
        node = Node(key, value)
        # jika node belum ada di self._data, maka tambahkan node tersebut ke self._data (graph)
        if key not in self._data.keys():
                setEdge = set()
                listData = [setEdge, node]
                self._data[key] = listData

    def vertex(self):
        print("\nSeluruh Node = ",end = ' ')
        for key, value in self._data.items():
            print(key,end = ' ')
        print()

    def addEdge(self, x,y):
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x)

    def edge(self):
        print("Seluruh Edge =", end= ' ')
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key + item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)
        for item in listEdge :
            print(item, end= ' ')
        print()
    
    # untuk pembacaan traversing bfs graph
    def bfs(self, node):
        visited = []
        queue = []
        visited.append(node)
        queue.append(node)
        print('Traversing BFS =',end=' ')
        while queue:
            q = queue.pop(0) 
            print (q, end = " ") 
            for neighbour in self._data[q]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        print("\n")

graph = Graph()
graph.addVertex("a", 2)
graph.addVertex("b", 2)
graph.addVertex("c", 4)
graph.addVertex("d", 3)
graph.addVertex("e", 4)
graph.addVertex("f",3)
graph.addVertex("g", 3)
graph.addVertex("h", 3)

graph.addEdge('a', 'b')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('c', 'g')
graph.addEdge('d', 'e')
graph.addEdge('f', 'h')
graph.addEdge('g', 'f')

graph.vertex()
graph.edge()
graph.bfs('a')