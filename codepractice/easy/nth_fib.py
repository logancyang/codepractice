"""
Get the Nth fibonacci number

0, 1, 1, 2, 3, 5, 8, 13
"""

# Optimal, O(n) time O(1) space
def getNthFib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    first = 0
    second = 1
    for i in range(3, n+1):
        new = first + second
        first = second
        second = new
    return new

# O(2^n) time, O(n) space
# Because e.g. 10 -> 9, 8
# 9 -> 8, 7; 8 -> 7, 6
# 7 -> 6, 5; 6 -> 5, 4...
# A lot of redundant steps for overlapping numbers
def getNthFibRecursive(n):
    # base
    if n == 1:
        return 0
    if n == 2:
        return 1

    return getNthFibRecursive(n-1) + getNthFibRecursive(n-2)


print(getNthFib(3)) #1
print(getNthFib(4)) #2
print(getNthFib(5)) #3

print(getNthFibRecursive(3)) #1
print(getNthFibRecursive(4)) #2
print(getNthFibRecursive(5)) #3
