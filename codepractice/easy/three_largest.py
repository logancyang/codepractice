"""
Find 3 largest numbers in array with dupes in one pass, return in increasing order
"""

def findThreeLargestNumbers(array):
    # Write your code here.
    largest, second, third = float("-inf"), float("-inf"), float("-inf")
    for num in array:
        if num >= largest:
            third = second
            second = largest
            largest = num
        elif num >= second:
            third = second
            second = num
        elif num >= third:
            third = num
    return [third, second, largest]

tc1 = [141, 1, 17, -4]
print(findThreeLargestNumbers(tc1))
