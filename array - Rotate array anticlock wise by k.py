"""
  Q. Reverse an array by K but anticlock wise
"""


def Reverse(arr:list, start:int, end:int):
    while start < end : 
        arr[start], arr[end] = arr[end], arr[start]
        start += 1 
        end -= 1 
    
    
def Rotate_Anticlockwise(arr, d):
    n = len(arr)
    d = d % n 
    
    Reverse(arr, 0, d-1)
    
    Reverse(arr, d, n-1)
    
    Reverse(arr, 0 , n-1)
    
    return arr 
    
arr = [1,2,3,4,5,6]
print(Rotate_Anticlockwise(arr, 2))
