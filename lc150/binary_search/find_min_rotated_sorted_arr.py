from typing import List

def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while (l < r):
        m = l + (r - l) // 2
        if nums[m] < nums[r]:
            r = m
        else:
            l = m + 1
    return nums[l]

print(findMin([3,4,5,6,1,2])) #1
print(findMin([4,5,0,1,2,3])) #0
print(findMin([4,5,6,7])) #4