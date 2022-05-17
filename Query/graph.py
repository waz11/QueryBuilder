from Query.edge import Edge
from Query.vertex import Vertex


class Graph:
    def __init__(self, directed=False):
        self.vertices :dict = {}    # key:vertex
        self.edges_dict :dict = {}  # source_key:[edges]
        self.edges :list = []
        self.directed :bool = directed
##################################################################################3
    def num_of_vertices(self):
        return len(self.vertices)
    def num_of_edges(self):
        return len(self.edges_dict)
##################################################################################3
    def add_vertex(self, vertex: Vertex) -> None:
        self.vertices[vertex.key] = vertex
        self.edges_dict[vertex.key] = []

    def add_edge(self, edge :Edge):
        self.add_edge_aux(edge)

    def add_edge_aux(self, edge: Edge, directed :bool = False):
        if(edge.source not in self.edges_dict):
            self.edges_dict[edge.source] = []
        self.edges_dict[edge.source].append(edge)
        self.edges.append(edge)
        if not directed:
            edge2 = Edge(edge.to, edge.source, edge.type)
            self.add_edge_aux(edge2, True)
##################################################################################3
    def get_vertices(self) ->list:
        return list(self.vertices.values())

    def get_edges(self) ->list:
        return list(self.edges)

    def get_vertex(self, key :int) ->Vertex:
        return self.vertices[key]

    def get_edge(self,source_key :int, dest_key :int) ->Edge:
        return self.edges_dict[source_key, dest_key]
##################################################################################3
    def __len__(self):
        return len(self.vertices)

    def __str__(self):
        s = ''
        for vertex in self.get_vertices():
            s += str(vertex) + ' '
        for edge in self.get_edges():
            s += str(edge) + ' '
        return s

