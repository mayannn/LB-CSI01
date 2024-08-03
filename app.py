
#Exercise 1: Search for an element in an array
#Problem: Given a sorted array, search for an element in that array.
#Solution: Use the Binary Search algorithm to search quickly.
#Example: arr = [1, 3, 5, 7, 9, 11, 13]
#target = 5

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right :
        mid = (left + right)//2
        if arr[mid] == target :
            return mid
        elif arr[mid] < target :
            left = mid + 1
        else :
            right = mid - 1
    return -1

arr = [1,3,5,7,9,11,13]
target = 5
print(binary_search(arr,target))


# Exercise 2: Search for all occurrences of an element in an array
# Problem: Given an array, find all occurrences of an element in the array.
# Solution: Use Linear Search to traverse the entire array and record the occurrences.
# Example: arr = [1, 3, 7, 8, 7, 5, 6, 7, 2]
# target = 5

def linear_search(arr,target) :
    indices = []
    for i in range(len(arr)):
        if arr[i] == target :
            indices.append(i)
    return indices if indices else -1

arr = [1,3,7,8,5,6,7,2]
target = 7
print(linear_search(arr,target))

# Exercise 3: Search for the largest element in an array
# Problem: Given an array, find the largest element in the array.
# Solution: Use Linear Search to find the largest element.
# Example: arr = [1, 3, 7, 8, 5, 6, 2]

def linear_search_large(arr) :
    largest = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[largest]  :
            largest = i 
    return largest

arr = [1,3,7,8,5,6,2]
print(linear_search_large(arr))

# Exercise 4: Find the smallest element in an array
# Problem: Given an array, find the smallest element in the array.
# Solution: Use Linear Search to find the smallest element.
# Example: arr = [1, 3, 7, 8, 5, 6, 2]


def linear_search_small(arr) :
    smallest = 0
    for i in range(1, len(arr)):
        if arr[smallest] > arr[i]  :
            smallest = i 
    return smallest

arr = [1,3,7,8,5,6,2]
print(linear_search_small(arr))