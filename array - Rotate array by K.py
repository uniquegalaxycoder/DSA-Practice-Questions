"""
  Q. Rotate a array by k = 3
"""
    
def reversePart(arr:list, start:int, end:int):
    while start <= end :
        arr[start], arr[end] = arr[end], arr[start]
        start += 1 
        end -= 1 
            
def RotateByk(arr:list, k:int ):
    n = len(arr)
    k = k % n 
        
    # first rotate first to last
    reversePart(arr, 0, n-1)
        
    # second rotate till given k value
    reversePart(arr, 0, k-1)
        
    # third, rotate an array from k to n-1
    reversePart(arr, k, n-1)
    
    return arr 
    
arr = [1,2,3,4,5,6,7,8]
k = 3 
print(RotateByk(arr, k))
    
    
