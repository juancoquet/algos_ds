class Vertex:

    def __init__(self, key):
        self.key = key
        self.connected_to = {}

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


