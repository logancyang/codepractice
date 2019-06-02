"""
DFS: O(V+E) time, O(V) space
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self, array):
        """
        # Start at empty array
        # No Base case for this one, since no None node will be reached
        if not self.name:
            return array
        """
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array