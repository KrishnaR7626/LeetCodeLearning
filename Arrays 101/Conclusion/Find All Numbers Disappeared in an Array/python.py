class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = {i for i in nums}
        return [i for i in range(1, len(nums)+1) if i not in s]
