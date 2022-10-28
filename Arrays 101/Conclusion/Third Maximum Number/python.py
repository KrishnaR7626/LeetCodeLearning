class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxs = {max(nums)}
        mi = min(nums)
        for i in range(2):
            m = mi
            for y in nums:
                if y > m and y < min(maxs):
                    m = y
            maxs.add(m)
            print(maxs)
        if len(maxs) < 3:
            return max(maxs)
        else:
            return min(maxs)
