import json
import os
import string
from Query.edge import EdgeTypeEnum
from Query.graph import Graph
from Query.graphFromQuery import GraphFromQuery
from Query.utils.json_functions import graphToJson
from Query.vertex import VertexTypeEnum


files_path = './Files'

def save_json_to_file(json_object, file_name):
    with open(file_name+'.json', 'w', encoding='utf-8') as f:
        json.dump(json_object, f, ensure_ascii=False, indent=4)

def buildQuery(query :string):
    q = QueryBuilder(query)
    json = graphToJson(q.graph)
    return json

def foo(query :string, i: int):
    init_folders()
    json = buildQuery(query)
    save_json_to_file(json, files_path+'/query'+str(i))

def init_folders():
    isExist = os.path.exists(files_path)
    if not isExist:
        os.makedirs(files_path)


special_words = ["extends", "implements", "method", "class", "contains","interface"]

class QueryBuilder:

    def __init__(self, query :string):
        self.content = query
        self.graph = self.build_graph()

    def __str__(self):
        return str(self.content)

    # for GreedySearch:
    def build_graph(self)->Graph:
        g = GraphFromQuery()
        content = self.content.split(',')
        for sentence in content:
            words = list(sentence.split(' '))
            for i, word in enumerate(words):
                if word in special_words:
                    if word=='class':
                        name = words[i + 1]
                        v = g.add_vertex(name, VertexTypeEnum.CLASS)

                    elif word =='method':
                        g.add_vertex(words[i + 1], VertexTypeEnum.METHOD)

                    elif word=='extends':
                        vertex1 = g.add_vertex(words[i - 1], VertexTypeEnum.CLASS)
                        vertex2 = g.add_vertex(words[i + 2], VertexTypeEnum.CLASS)
                        g.add_edge(EdgeTypeEnum.EXTENDS, vertex1.key, vertex2.key)

                    elif word=='implements':
                        vertex1 = g.add_vertex(words[i - 1], VertexTypeEnum.CLASS)
                        vertex2 = g.add_vertex(words[i + 1], VertexTypeEnum.INTERFACE)
                        g.add_edge(EdgeTypeEnum.IMPLEMENTS, vertex1.key, vertex2.key)

                    elif word == 'interface':
                        name = words[i + 1]
                        g.add_vertex(name, VertexTypeEnum.INTERFACE)

                    elif word=='contains':
                        if words[i-2] == 'class':
                            vertex1 = g.add_vertex(words[i - 1], VertexTypeEnum.CLASS)
                        else:
                            vertex1 = g.add_vertex(words[i - 1], VertexTypeEnum.CLASS)

                        if words[i+1]== 'method':
                            vertex2 = g.add_vertex(words[i + 2], VertexTypeEnum.METHOD)
                            g.add_edge(EdgeTypeEnum.METHOD, vertex1.key, vertex2.key)

                        elif words[i+1]== 'class':
                            vertex2 = g.add_vertex(words[i + 2], VertexTypeEnum.CLASS)
                            g.add_edge(EdgeTypeEnum.CONTAINS, vertex1.key, vertex2.key)
        return g


