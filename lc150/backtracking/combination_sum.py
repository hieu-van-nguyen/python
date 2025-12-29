from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)
        dfs(0, [], 0)    
        return res
    
    def combinationSumV2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                curr.append(nums[j])
                dfs(j, curr, total + nums[j])
                curr.pop()
                
        dfs(0, [], 0)    
        return res