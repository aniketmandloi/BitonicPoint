def findMaximumUtil(arr, low, high) :
    if low == high :  
        return arr[low]

    if high == low + 1 and arr[low] >= arr[high] : 
        return arr[low]

    if high == low + 1  and  arr[low] < arr[high] :
        return arr[high]
    mid = (low + high) // 2;
    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1] :
        return arr[mid] 
    if arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1] :
        return findMaximumUtil(arr, low, mid - 1) 
    else :
        return findMaximumUtil(arr, mid + 1, high)    

class Solution:
    def findMaximum(self,Arr,N):
        return findMaximumUtil(Arr, 0, N - 1)
