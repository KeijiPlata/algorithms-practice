"""
Binary Search
- half the nummber of items until you get the desire item
- only works if the list is sorted
"""

def binarySearch(mylist, item):
    """get the list and item they want and return the index"""
    # initialization of varialbles
    low = 0
    high = len(mylist)-1

    # if low is less than equal to high, it will not terminate 
    while low <= high:
        # add low and high and divide it by 2 to get the mid value
        mid = (low + high)//2

        # get the number in list
        guess = mylist[mid]

        # if guess is equal to number, return the index
        if guess == item:
            return mid
        
        # if guess is greater than the item, change the value of high into
        # mid - 1
        elif guess > item:
            high = mid - 1

        # if guess is less than the item, change the value of low into
        # mid + 1
        else:
            low = mid + 1

    # return nothing if not found
    return None

mylist = [1, 3, 5, 7, 9]

# output
userinput = int(input("Find the number you want in the list: "))
print(f"index: {binarySearch(mylist, userinput)}")
