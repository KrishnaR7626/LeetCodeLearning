class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        for i in range(len(arr)-1, -1, -1):
            if max < arr[i]:
                temp = max
                max = arr[i]
                arr[i] = temp
            else:
                arr[i] = max
        arr[len(arr)-1] = -1
        return arr
