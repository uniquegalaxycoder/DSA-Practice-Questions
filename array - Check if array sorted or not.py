# check if array is sorted


def array_sort_check(arr:list):
    n = len(arr)     # O(1)

    for i in range (n-1):      # O(n)
        
        if arr[i] > arr[i+1] :  # O(1)
          
            return "not Sorted"
        
    else :
        return "sorted"
        
arr = [1,2,3,4,5,6,7]
print(array_sort_check(arr))

# Time complexity : O(n)
# Time Complexity : O(1)  n, i
