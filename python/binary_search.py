# A sorted array and an item


from typing import List


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




##Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17]
obj = Solution()
print(obj.search(mylist, 7))

