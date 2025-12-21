# find the largest & smallest element of array

def max_min_ele(arr:list) :
    n = len(arr)
    
    sml_ele = arr[0]
    max_ele = arr[0]
    
    for i in range(1,n):
        if arr[i] < sml_ele :
            sml_ele = arr[i]
            
        elif arr[i] > max_ele :
            max_ele = arr[i]
    return sml_ele, max_ele
        

arr = [4,5,1,3,2]
print(max_min_ele(arr))


# Space complexity O(1) -> only using extra two veriables  
# time complexity O(n) -> traverse the array once
