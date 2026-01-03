""" Max product of triplate """

""" Solved Type-I 
( 
    By Using Gready Approach  
    - [product of Max 3 element]
    or 
    - [Product of max 2 elelemt & last 1 element ]
  )  """

def maxProduct(arr:list):
    n = len(arr)            # O(1)
    
    max1 = float('-inf')    # O(1)
    max2 = float('-inf')    # O(1)
    max3 = float('-inf')    # O(1)
    
    min1 = float('inf')     # O(1)
    min2 = float('inf')     # O(1)
    
    for i in range(n):          # O(n)
        if arr[i] > max1 :      # O(1)
            max3 = max2         # O(1)
            max2 = max1         # O(1)
            max1 = arr[i]       # O(1)
        elif arr[i] > max2 :    # O(1)
            max3 = max2         # O(1)
            max2 = arr[i]       # O(1)
        elif arr[i] > max3 :    # O(1)
            max3 = arr[i]       # O(1)
            
        if arr[i] < min1 :      # O(1)
            min2 = min1         # O(1)    
            min1 = arr[i]       # O(1)
        elif arr[i] < min2 :    # O(1)
            min2 = arr[i]       # O(1)
            
    return (min1 * min2*max1, max1*max2*max3)

  
  
arr = [-10, -3, 5, 6, -20]
print(maxiProduct(arr))

"""-----------------------------------------------------------------------------------------------------------"""

 """ By using Sorting - TimeO(n*Log(n) & sapce Complexity O(1) """ 

def maxiProduct(arr:list):
    n = len(arr)    # O(1)
  
    arr.sort()    #O( n*log(n) )
  # After sorting array will be [-20, -10, -3, 5, 6]
  
    return max( arr[0] *  arr[1] * arr[-1] ,  arr[-1] * arr[-2] * arr[-3])  
              #LastMin, #2lastMin, #1Max,     #1Max,    #2Max,   #3Maz

    
arr = [-10, -3, 5, 6, -20]
print(maxiProduct(arr))


