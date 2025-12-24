#Find second largest / second smallest


def get_secondLarge(arr):
    n = len(arr)                                        # O(1)
    large = float('-inf')                               # O(1)
    secondLarge = float('-inf')                         # O(1)
    for i in range(n):                                  # O(n)
        if arr[i] > large :                             # O(1)
            secondLarge = large                         # O(1)
            large = arr[i]                              # O(1)
        elif arr[i] > secondLarge and arr[i] < large :  #O(1)
            secondLarge = arr[i]                        # O(1)
            
    return secondLarge
    
def get_secondSmall(arr):                               
    n = len(arr)                                        # O(1)
    small, secondSmall = float('inf'), float('inf')     # O(1)
    for i in range(n):                                  # O(n)
        if arr[i] < small :                             # O(1)
            secondSmall = small                         # O(1)
            small = arr[i]                              # O(1)
        elif arr[i] < secondSmall and arr[i] > small :  # O(1)
            secondSmall = arr[i]                        # O(1)
        
    return secondSmall
    
arr=[1,2,3,4,5,6,7]

secondSmall = get_secondSmall(arr)

secondLarge = get_secondLarge(arr)

print(f"Second Small : {secondSmall} \nSecond Large : {secondLarge}")

# Time Complexity : O(n)
# Space Complexity : O(1)


