import string
import enum

class VertexTypeEnum(enum.Enum):
   CLASS = "class"
   METHOD = "method"
   INTERFACE = "interface"


class Vertex:
    def __init__(self,key:int, name, type: VertexTypeEnum, attributes=None):
        self.key :int = key
        self.type :VertexTypeEnum = type
        self.name :string = name

        self.neighbors = set()
        self.attributes = set()
        if attributes:
            for att in attributes: self.attributes.add(att)

    def __str__(self):
        neighbors = []
        if self.neighbors:
            for neighbor in self.neighbors:
                neighbors.append(neighbor.name)
        return "[{},{},{}]".format(self.key, self.type.value, self.name)

    def toJson(self):
        json = {}
        json["key"] = self.key
        json["type"] = self.type.value
        json["name"] = self.name
        # json["modifiers"] = self.modifiers
        json["attributes"] = list(self.attributes)
        return json