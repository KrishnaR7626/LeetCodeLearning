class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=0
        for i in nums:
            if i == 0:
                z+=1
        p = 0
        for i in nums:
            if i != 0:
                nums[p] = i
                p+=1
        for i in range(p, len(nums)):
            nums[i] = 0
