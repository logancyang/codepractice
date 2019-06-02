
def binarySearch(array, target):
    # Write your code here.
    if not array:
        return -1
    start, end = 0, len(array)-1
    # Note start + 1 < end
    while start + 1 < end:
        mid = (start + end)//2
        if target == array[mid]:
            # This means we discard the larger side, i.e. return the leftmost/first occurrence
            end = mid
        if target < array[mid]:
            end = mid
        else:
            start = mid

    if array[start] == target:
        return start
    if array[end] == target:
        return end
    return -1

