from typing import List

def hasDuplicateV1(nums: List[int]) -> bool:
        # Time Complexity O(nlogn)
        # Space complexity: O(1)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False  

print(hasDuplicateV1([1, 2, 3, 4, 5])) # False
print(hasDuplicateV1([1, 2, 3, 4, 2, 5])) # True

def hasDuplicateV2(nums: List[int]) -> bool:
    # Time Complexity O(n)
    # Space complexity: O(n)
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False        

print(hasDuplicateV2([1, 2, 3, 4, 5])) # False
print(hasDuplicateV2([1, 2, 3, 4, 2, 5])) # True

def hasDuplicateV3(nums: List[int]) -> bool:
    # Time Complexity O(n)
    # Space complexity: O(n)
    return len(set(nums)) < len(nums)

print(hasDuplicateV3([1, 2, 3, 4, 5])) # False
print(hasDuplicateV3([1, 2, 3, 4, 2, 5])) # True