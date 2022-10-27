class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        g = [i for i in heights]
        c=0
        heights.sort()
        for i in range(len(heights)):
            if heights[i] != g[i]: 
                c+=1
        return c
