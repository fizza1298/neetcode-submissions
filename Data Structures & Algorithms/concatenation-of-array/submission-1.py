class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_ = [0] *2*len(nums)
        for i, num in enumerate(nums_): 
            j = i % len(nums) 
            nums_[i] = nums[j]
        return nums_

        