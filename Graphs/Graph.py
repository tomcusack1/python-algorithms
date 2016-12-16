from collections import OrderedDict
from enum import Enum


class State(Enum):
    unvisited = 1  # White
    visited = 2    # Black
    visiting = 3   # Gray


class Node:
    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # Key = Node, Value = Weight

    def __str__(self):
        return str(self.num)


class Graph:
    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, destination, weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if destination not in self.nodes:
            self.add_node(destination)
        self.nodes[source].adjacent[self.nodes[destination]] = weight
