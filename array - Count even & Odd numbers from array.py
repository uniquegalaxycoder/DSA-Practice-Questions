# Count even & Odd numbers 

def even_odd_count(arr:list):
    n = len(arr)               # O(1)
    even_ele = 0               # O(1)     
    odd_ele = 0                # O(1)
    
    if n > 0 :                  # O(1)
        
        for i in range(n):       # O(n) runs multiple time
            if arr[i]%2 == 0:     # O(1)
                even_ele += 1     # O(1)
                
            elif arr[i]%2 != 0 :    # O(1)
                odd_ele += 1        # O(1)
    else :
        return None
    
    return f"even count {even_ele}, odd count {odd_ele}"

arr = [1,2,3,4,5,6,7,8,9]
print(even_odd_count(arr))

# Time Complexity : O(n) array traverse all element
# Space Complexity : O(1) only took static veriable

    


