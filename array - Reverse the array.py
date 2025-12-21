# Reverse the array 

# ------- using the naive approch ( using temp array)

def reverse_array_type_one(arr:list):
    arr1= []
    
    n = len(arr)
    for i in range(n-1 ,-1, -1):
        arr1.append(arr[i])
        
    return arr1
    
arr = [4,5,1,3,2]
print(reverse_array(arr))

# time Complexity -> O(n) 
# space Complexity -> O(n) each time new element is appending in arr1 


# ------- using then left & right pointer ( Two Pointers approch)

def reverse_array_type_two(arr:list):
    n = len(arr)
    left = 0
    right = n-1
    
    while left <= right :
        arr[left], arr[right] = arr[right], arr[left]
        left +=1 
        right -= 1
        
    return arr
    
arr1 = [4,5,1,3,2]
print(reverse_array_type_two(arr1))

# Time Complexity -> O(n) traversing each element
# Space Complexity -> O(1) reversing inplace not took any extra veriable


# ------- using swapping Element methode by n//2 
def reverse_array_type_three(arr:list)
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        
    return arr
    
arr2 = [4,5,1,3,2]    
print(reverse_array_type_three(arr2))

# Time Complexity -> O(n) ( we did n//2 but array iterate element till n//2 so, O(n))
# Space Complexity -> O(1) not took any extra veriable, did inplace


# -------- using Recursion methode 

def reverse_array(arr, start, end):
    if start >= end :
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start+1, end-1)

arr = [1, 2, 3, 4, 5]
reverse_array(arr, 0, len(n)-1)
print(arr)



