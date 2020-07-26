
def binary_search(array: list, key):
    lower = 0
    upper = len(array) - 1
    
    while lower < upper:
        mid = int(lower + (upper - lower) / 2)
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            lower = ""
        else:
            upper = mid

