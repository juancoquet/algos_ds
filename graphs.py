from queue import Queue


class Vertex:

    def __init__(self, key):
        self.key = key
        self.connected_to = {}
        self.distance = 0
        self.visited = False
        self.fully_searched = False
        self.predecessor = None

    def add_connection(self, to_vertex, weight=0):
        self.connected_to[to_vertex] = weight

    def __str__(self):
        return str(self.id) + 'connected to: ' + str([vertex.key for vertex in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_key(self):
        return self.key

    def get_weight(self, to_vertex):
        return self.connected_to[to_vertex]


class Graph:

    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        self.num_vertices += 1
        return new_vertex

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None
    
    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, from_vertex, to_vertex, weight=0):
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)
        self.vertices[from_vertex].add_connection(self.vertices[to_vertex], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def bfs(self, start_vertex):
        start_vertex.distance = 0
        to_search = Queue()
        to_search.enqueue(start_vertex)
        while to_search.size > 0:
            current_vx = to_search.dequeue()
            for neighbour in current_vx.get_connections():
                if not neighbour.visited:
                    neighbour.visited = True
                    neighbour.distance = current_vx.distance + 1
                    neighbour.predecessor = current_vx
                    to_search.enqueue(neighbour)
            current_vx.fully_searched = True

    def traverse(self, vertex):
        while vertex.predecessor is not None:
            print(vertex.key)
            vertex = vertex.predecessor
        print(vertex.key)