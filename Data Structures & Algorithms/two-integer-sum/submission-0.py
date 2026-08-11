class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        brute force implemenataion match every i + j tp target 
        """
        pairs = {} # nums = [3,4,5,6], target = 7, nums = [5,5], target = 10
        for i,num in enumerate(nums): 
            if num in pairs: 
                return [pairs[num], i]
            else: 
                pairs[target - num] = i
                    