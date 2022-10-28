class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for x in range(len(nums)):
            nums[x] = nums[x]*nums[x]
        nums.sort() 
        return nums
