# https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST

"""
Find the closest value to a given target value in a BST

Recursion

Key idea:

Extra param `closest` to track the previous closest value. This extra param should be initalized
as +Inf and updated every time there is a closer value.

The outer function does not have this extra param as input, so,
**We need RECURSIVE HELPER which takes this extra param initialized at +Inf**

- base case: None! Finished traversing the correct branch **tree is None**, return the current closest
- if equal, return current node value
- elif value is smaller than target, recurse and get result from right subtree
- elif value is larger than target, recurse and get result from left tree

"""

# Average O(log n) time ,O(1) space (only one node is in memory each time)

def findClosestValueInBst(tree, target):
    return helper(tree, target, closest=float("inf"))

def helper(tree, target, closest):
    # base cases
    if not tree:
        return closest
    if tree.value == target:
        return tree.value

    if abs(tree.value - target) < abs(closest - target):
        closest = tree.value
    if tree.value < target:
        return helper(tree.right, target, closest)
    else:
        return helper(tree.left, target, closest)


arr = [3,2,1,0]
print(arr[-3:])
