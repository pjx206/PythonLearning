class Node():
    def __init__(self, number):
        self._number = number
        self._linked = []
    
    def __repr__(self):
        return "Node({})".format(self._number)

    def add_linked_node(self, node):
        self._linked.append(node)

    def __iter__(self):
        return iter(self._linked)

class Graph():
    """Manage graphs which has edges with weight"""
    pass

def dijkstra(Graph, origin:Node, dest:Node):
    pass

def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.add_linked_node(node2)
    node1.add_linked_node(node3)
    for node in node1:
        print(node)

if __name__ == '__main__':
    main()