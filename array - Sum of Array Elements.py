# Sum of Array Elements 

def sum_array_ele(arr:list):
    arr= [1,2,3,4,5,5]
    n = len(arr)
    sums = 0
    
    for i in range(n):
        sums += arr[i]
        
    return sums
    
arr = [1,3,5,7,8]
print(sum_array_ele(arr))

# Time Complexity : O(n) array traversing one liner
# Space Complexity : O(1)  used one veriable Sums for finding total


# by recursive methode :

def sum_of_ele(arr) :
    if len(arr) == 0 :
        return 0
        
    return arr[0] + sum_of_ele(arr[1:])
    
arr=[1,2,3,4,5]
print(sum_of_ele(arr))

# Time Complexity : O(n^2) [ O(n)+O(n-1)+O(n-2)..O(1) = O(n^2)]
# Space Complexity : O(n^2) Each recursive call creates a new list
    
    
