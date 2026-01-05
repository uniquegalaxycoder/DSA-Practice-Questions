""" Find the max consicutive one's  """


def maxOnes(arr:list):
    n = len(arr)                                      # O(1)
                                                      
    count = 0                                         # O(1)
    max_count = 0                                     # O(1)
    
    for i in range(n):                                # O(n)
        if arr[i] == 1 :                              # O(1)
            count += 1                                # O(1)
            max_count = max(max_count, count)         # O(1)
        else :
            count = 0                                 # O(1)
            max_count = max(max_count, count)         # O(1)
    return max(count, max_count)                      
    
arr = [1,1,0,1,1,1,1,0,1]
print(maxOnes(arr))

# Time Complexity : O(n)
# Space Complexity : O(1)


    
