class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        y = 0
        for i, num in enumerate(nums):
            if num == val:
                c+=1
                num = None
            else:
                nums[y] = nums[i]
                y+=1
        return len(nums)-c
