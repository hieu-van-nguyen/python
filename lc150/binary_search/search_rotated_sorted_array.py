def search(nums, target):
    minIndex = findMinIndex(nums)
    leftSearch = binary_search(nums, 0, minIndex - 1, target)
    if leftSearch != -1:
        return leftSearch
    else:
        return binary_search(nums, minIndex, len(nums) - 1, target)

def findMinIndex(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    return l

def binary_search(nums, lowerBound, upperBound, target):
    l, r = lowerBound, upperBound
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(search([3,4,5,6,1,2], 1)) #4
print(search([3,5,6,0,1,2], 4)) #-1