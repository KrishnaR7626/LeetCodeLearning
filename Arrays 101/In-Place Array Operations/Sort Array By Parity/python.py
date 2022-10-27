class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = [0 for i in nums]
        end = len(arr)-1
        start = 0
        for i in nums:
            if i % 2 == 0:
                arr[start] = i
                start+=1
            else:
                arr[end] = i
                end-=1
        return arr
