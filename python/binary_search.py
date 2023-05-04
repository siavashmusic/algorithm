# A sorted array and an item
def binary_search_ver_one(thelist, item):
    low = 0
    high = len(thelist) - 1

    while low <= high:
        mid = (low + high) // 2
        guess_item = thelist[mid]
        if guess_item == item:
            return mid
        if guess_item < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


def binary_search_ver_two(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_ver_two(data, target, mid - 1)
        else:
            return binary_search_ver_two(data, target, mid + 1, high)


def binary_search_ver_three(haystack, needle) -> int:
    lo = 0
    hi = len(haystack)

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        guess = haystack[mid]
        if guess == needle:
            return mid
        elif guess > needle:
            hi = mid
        else:
            lo = mid + 1
    return False


mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(binary_search_ver_three(mylist, 7))
