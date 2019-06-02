"""
Write a class for a Doubly Linked List. The class should have a "head" and "tail" properties,
both of which should point to either the None (null) value or to a Linked List node.
Every node will have a "value" property as well as "next" and "prev" properties,
both of which can point to either the None (null) value or another node. The class
should support setting the head and tail of the linked list, inserting nodes before
and after other nodes as well as at certain positions, removing given nodes and removing
nodes with specific values, and searching for nodes with values.

Only the searching method should return a value: specifically, a boolean.
"""

"""
Key Takeaway: For Node Equality, use `is` rather than `==`.
`is`: identity;
`==`: value equality

The custom Node class does not have equality implemented, BUT since they are the same object,
`==` is True.

Python note: `is` => True means `==` => True, almost always, with `NaN` as the only exception
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        # None <-> Head <-> HeadNext
        if not self.head:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    def setTail(self, node):
        # Write your code here.
        # TailPrev <-> Tail <-> None
        if not self.tail:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # If list only has one node and it is the node to insert
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        # If nodeToInsert already in the chain, remove it first, then place it before node
        self.remove(nodeToInsert)
        prev = node.prev
        nodeToInsert.prev = prev
        nodeToInsert.next = node
        node.prev = nodeToInsert
        # Case prev is None, node is head, None <- node <-> next
        if not prev:
            self.head = nodeToInsert
        else:
            prev.next = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # If list only has one node and it is the node to insert
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        # If nodeToInsert already in the chain, remove it first, then place it before node
        self.remove(nodeToInsert)
        nodenext = node.next
        nodeToInsert.prev = node
        nodeToInsert.next = nodenext
        node.next = nodeToInsert
        # Case prev is None, node is head, None <- node <-> next
        if not nodenext:
            self.tail = nodeToInsert
        else:
            nodenext.prev = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        curr = self.head
        # To define head is pos 1, range(position-1)
        pos = 1
        while curr and pos != position:
            curr = curr.next
            pos += 1
        # if position == 1, curr is at head, insert before head
        # pos = 2, before 2nd node
        if curr:
            self.insertBefore(curr, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        curr = self.head
        while curr:
            candidate = curr
            curr = curr.next
            if candidate.value == value:
                self.remove(candidate)

    def containsNodeWithValue(self, value):
        # Write your code here.
        curr = self.head
        while curr and curr.value != value:
            curr = curr.next
        return curr is not None

    def remove(self, node):
        # For a node either head or tail, or in the chain, cut the bindings
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def removeNodeBindings(self, node):
        # For a node not head or tail, cut the bindings
        if node and node.prev:
            node.prev.next = node.next
        if node and node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


node1 = Node(1)
node2 = Node(2)
print(node1 == node2) # False
# What does `==` do for this Node class? Since __eq__ is not implemented,
# it falls back to `object.__eq__` which compares address of instances
