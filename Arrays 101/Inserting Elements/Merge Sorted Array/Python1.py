class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        c = 0
        i = m
        while i<m+n:
            nums1[i] = nums2[c]
            i+=1
            c+=1
        nums1.sort()
