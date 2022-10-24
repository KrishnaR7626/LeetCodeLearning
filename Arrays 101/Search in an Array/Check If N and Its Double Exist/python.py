class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        z = arr.count(0)
        if z >=2:
            s = {num for num in arr}
        else:
            s = {num for num in arr if num != 0} 
        for num in arr:
            if num*2 in s:
                return True    
        return False
