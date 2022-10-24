class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        increasing = True
        endpeak = True
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1] or ((endpeak or arr[i] < arr[i+1]) and not increasing):
                return False
            elif increasing and arr[i] > arr[i+1]:
                increasing = False
                endpeak = True
            if i == 0 or (increasing and i == len(arr)-2):
                endpeak = True
            else:
                endpeak = False
        return not endpeak
