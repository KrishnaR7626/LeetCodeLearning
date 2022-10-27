class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        current = nums[0]
        for i in range(len(nums)):
            if nums[i] != current:
                nums[index] = current
                current = nums[i]
                index+=1
        nums[index] = current
        index+=1
        return index
