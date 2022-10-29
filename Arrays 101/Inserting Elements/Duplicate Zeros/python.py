class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        res = [0 for i in arr]
        i = 0
        b = 0
        while i < len(arr):
            if arr[i-b]!=0:
                res[i] = arr[i-b]
            else:
                res[i] = 0
                if i+1 < len(arr):
                    res[i+1] = 0
                    i+=1
                    b+=1
            i+=1
        for i in range(len(arr)):
            arr[i] = res[i]
