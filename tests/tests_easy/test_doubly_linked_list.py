import unittest
from codepractice.easy.doubly_linked_list import DoublyLinkedList


class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

def expectEmpty(self, linkedList):
  self.assertEqual(linkedList.head, None)
  self.assertEqual(linkedList.tail, None)

def expectHeadTail(self, linkedList, head, tail):
  self.assertEqual(linkedList.head, head)
  self.assertEqual(linkedList.tail, tail)

def expectSingleNode(self, linkedList, node):
  self.assertEqual(linkedList.head, node)
  self.assertEqual(linkedList.tail, node)

def getNodeValuesHeadToTail(linkedList):
  values = []
  node = linkedList.head
  while node is not None:
    values.append(node.value)
    node = node.next
  return values

def getNodeValuesTailToHead(linkedList):
  values = []
  node = linkedList.tail
  while node is not None:
    values.append(node.value)
    node = node.prev
  return values

def removeNodes(linkedList, nodes):
  for node in nodes:
    linkedList.remove(node)


class TestProgram(unittest.TestCase):

  def test_case1(self):
    linkedList = DoublyLinkedList()
    node = Node(1)

    linkedList.setHead(node)
    expectSingleNode(self, linkedList, node)
    linkedList.remove(node)
    expectEmpty(self, linkedList)
    linkedList.setTail(node)
    expectSingleNode(self, linkedList, node)
    linkedList.removeNodesWithValue(1)
    expectEmpty(self, linkedList)
    linkedList.insertAtPosition(1, node)
    expectSingleNode(self, linkedList, node)

  def test_case2(self):
    linkedList = DoublyLinkedList()
    first = Node(1)
    second = Node(2)
    nodes = [first, second]

    linkedList.setHead(first)
    linkedList.setTail(second)
    expectHeadTail(self, linkedList, first, second)
    removeNodes(linkedList, nodes)
    expectEmpty(self, linkedList)
    linkedList.setHead(first)
    linkedList.insertAfter(first, second)
    expectHeadTail(self, linkedList, first, second)
    removeNodes(linkedList, nodes)
    linkedList.setHead(first)
    linkedList.insertBefore(first, second)
    expectHeadTail(self, linkedList, second, first)
    removeNodes(linkedList, nodes)
    linkedList.insertAtPosition(1, first)
    linkedList.insertAtPosition(2, second)
    expectHeadTail(self, linkedList, first, second)
    removeNodes(linkedList, nodes)
    linkedList.insertAtPosition(2, first)
    linkedList.insertAtPosition(1, second)
    expectHeadTail(self, linkedList, second, first)

  def test_case3(self):
    linkedList = DoublyLinkedList()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    linkedList.setHead(first)
    self.assertEqual(linkedList.containsNodeWithValue(1), True)
    linkedList.insertAfter(first, second)
    self.assertEqual(linkedList.containsNodeWithValue(2), True)
    linkedList.insertAfter(second, third)
    self.assertEqual(linkedList.containsNodeWithValue(3), True)
    linkedList.insertAfter(third, fourth)
    self.assertEqual(linkedList.containsNodeWithValue(4), True)
    linkedList.removeNodesWithValue(3)
    self.assertEqual(linkedList.containsNodeWithValue(3), False)
    linkedList.remove(first)
    self.assertEqual(linkedList.containsNodeWithValue(1), False)
    linkedList.removeNodesWithValue(4)
    self.assertEqual(linkedList.containsNodeWithValue(4), False)
    linkedList.remove(second)
    self.assertEqual(linkedList.containsNodeWithValue(2), False)

  def test_case4(self):
    linkedList = DoublyLinkedList()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(3)
    fifth = Node(3)
    sixth = Node(6)
    seventh = Node(7)

    linkedList.setHead(first)
    linkedList.insertAfter(first, second)
    linkedList.insertAfter(second, third)
    linkedList.insertAfter(third, fourth)
    linkedList.insertAfter(fourth, fifth)
    linkedList.insertAfter(fifth, sixth)
    linkedList.insertAfter(sixth, seventh)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [1, 2, 3, 3, 3, 6, 7])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [7, 6, 3, 3, 3, 2, 1])
    expectHeadTail(self, linkedList, first, seventh)
    linkedList.remove(second)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [1, 3, 3, 3, 6, 7])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [7, 6, 3, 3, 3, 1])
    expectHeadTail(self, linkedList, first, seventh)
    linkedList.removeNodesWithValue(1)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [3, 3, 3, 6, 7])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [7, 6, 3, 3, 3])
    expectHeadTail(self, linkedList, third, seventh)
    linkedList.removeNodesWithValue(3)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [6, 7])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [7, 6])
    expectHeadTail(self, linkedList, sixth, seventh)
    linkedList.removeNodesWithValue(7)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [6])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [6])
    expectHeadTail(self, linkedList, sixth, sixth)

  def test_case5(self):
    linkedList = DoublyLinkedList()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)

    linkedList.setHead(first)
    linkedList.insertAfter(first, second)
    linkedList.insertAfter(second, third)
    linkedList.insertAfter(third, fourth)
    linkedList.insertAfter(fourth, fifth)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [1, 2, 3, 4, 5])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [5, 4, 3, 2, 1])
    expectHeadTail(self, linkedList, first, fifth)
    linkedList.insertAfter(third, fifth)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [1, 2, 3, 5, 4])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [4, 5, 3, 2, 1])
    expectHeadTail(self, linkedList, first, fourth)
    linkedList.insertAfter(third, first)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [2, 3, 1, 5, 4])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [4, 5, 1, 3, 2])
    expectHeadTail(self, linkedList, second, fourth)
    linkedList.insertAfter(fifth, second)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [3, 1, 5, 2, 4])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [4, 2, 5, 1, 3])
    expectHeadTail(self, linkedList, third, fourth)
    linkedList.insertAfter(second, first)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [3, 5, 2, 1, 4])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [4, 1, 2, 5, 3])
    expectHeadTail(self, linkedList, third, fourth)
    linkedList.insertAfter(fourth, sixth)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [3, 5, 2, 1, 4, 6])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 4, 1, 2, 5, 3])
    expectHeadTail(self, linkedList, third, sixth)
    linkedList.insertAfter(second, seventh)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [3, 5, 2, 7, 1, 4, 6])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 4, 1, 7, 2, 5, 3])
    expectHeadTail(self, linkedList, third, sixth)

  def test_case6(self):
    linkedList = DoublyLinkedList()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)

    linkedList.setHead(first)
    linkedList.insertBefore(first, second)
    linkedList.insertBefore(second, third)
    linkedList.insertBefore(third, fourth)
    linkedList.insertBefore(fourth, fifth)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [5, 4, 3, 2, 1])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [1, 2, 3, 4, 5])
    expectHeadTail(self, linkedList, fifth, first)
    linkedList.insertBefore(third, first)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [5, 4, 1, 3, 2])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [2, 3, 1, 4, 5])
    expectHeadTail(self, linkedList, fifth, second)
    linkedList.insertBefore(fifth, second)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [2, 5, 4, 1, 3])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 1, 4, 5, 2])
    expectHeadTail(self, linkedList, second, third)
    linkedList.insertBefore(fifth, fourth)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [2, 4, 5, 1, 3])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 1, 5, 4, 2])
    expectHeadTail(self, linkedList, second, third)
    linkedList.insertBefore(second, sixth)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [6, 2, 4, 5, 1, 3])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 1, 5, 4, 2, 6])
    expectHeadTail(self, linkedList, sixth, third)
    linkedList.insertBefore(first, seventh)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [6, 2, 4, 5, 7, 1, 3])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 1, 7, 5, 4, 2, 6])
    expectHeadTail(self, linkedList, sixth, third)

  def test_case7(self):
    linkedList = DoublyLinkedList()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)

    linkedList.setHead(first)
    linkedList.insertAtPosition(1, second)
    linkedList.insertAtPosition(1, third)
    linkedList.insertAtPosition(1, fourth)
    linkedList.insertAtPosition(1, fifth)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [5, 4, 3, 2, 1])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [1, 2, 3, 4, 5])
    expectHeadTail(self, linkedList, fifth, first)
    linkedList.insertAtPosition(2, first)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [5, 1, 4, 3, 2])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [2, 3, 4, 1, 5])
    expectHeadTail(self, linkedList, fifth, second)
    linkedList.insertAtPosition(1, second)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [2, 5, 1, 4, 3])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 4, 1, 5, 2])
    expectHeadTail(self, linkedList, second, third)
    linkedList.insertAtPosition(2, fourth)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [2, 4, 5, 1, 3])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 1, 5, 4, 2])
    expectHeadTail(self, linkedList, second, third)
    linkedList.insertAtPosition(1, sixth)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [6, 2, 4, 5, 1, 3])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 1, 5, 4, 2, 6])
    expectHeadTail(self, linkedList, sixth, third)
    linkedList.insertAtPosition(5, seventh)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [6, 2, 4, 5, 7, 1, 3])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 1, 7, 5, 4, 2, 6])
    expectHeadTail(self, linkedList, sixth, third)
    linkedList.insertAtPosition(8, fourth)
    self.assertEqual(getNodeValuesHeadToTail(linkedList), [6, 2, 5, 7, 1, 3, 4])
    self.assertEqual(getNodeValuesTailToHead(linkedList), [4, 3, 1, 7, 5, 2, 6])
    expectHeadTail(self, linkedList, sixth, fourth)
