"""
    Selection Sort
        - O(n*n) or O(n^2)
        - sort the list from ascending to descending order and vice versa
        - check each item in the list and then store the item into new list
        depending on asc or desc
"""

def findSmallest(arr):
    """find the smallest value inside the array"""
    # This is where we will store the smallest value and this is what we will compare to the other items
    smallest = arr[0] 

    # initialize the variable for the smallest index
    smallest_index = 0 

    # since we store the smallest into arr[0] we need to start with the index
    # 1 and get the length of the array to know when to stop
    for i in range(1, len(arr)): 

    # if the current index is the smallest with the arr[0] then reassigned the smallest
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    # at the end of the loop we will determine what index is the smallest inside the array
    return smallest_index

def selectionSort(arr):
    """create a new array then put the smallest number first the highest last"""
    newArr = []
    for i in range(len(arr)): 
        # this code will append the value to newArr then pop the value to arr
        # and to find the value of arr to be pop, we need to use the function 
        # the we create which is the findSmallest
        newArr.append(arr.pop(findSmallest(arr)))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
