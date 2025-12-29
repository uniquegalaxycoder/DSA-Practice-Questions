# Binary search 

def BinarSearch(arr:list):    
    n = len(arr)
    low = 0 
    high = n-1 
    digi = 23
    
    while low <= high :
    
        mid = low+((high-low)//2)
        
        if arr[mid] == digi :
            return mid, arr[mid]
       
        elif arr[mid] < digi :
            low = mid + 1 
            
        else :
            high = mid - 1
    return -1 
        
arr = [11,22,23,45,67,77]

print(BinarSearch(arr))

"""
Time Complexity -> in worst case O(log n)
Time Complexity -> in Best case O(1)
Space Complexity -> O(1)
"""
