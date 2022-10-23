class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                c+=1
                nums[i] = 101
        nums.sort()
        return len(nums)-c
