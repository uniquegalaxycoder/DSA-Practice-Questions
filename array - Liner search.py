# Liner search
def linerSearch(arr:list, value:int):
    n = len(arr)                                    # O(1)
    
    for i in range(n):                              # O(n)
        if arr[i] == value :                        # O(1)
            return f"Index: {i} \nValue: {arr[i]}"  # O(1)
    return "Value out of range!"
        
arr = [1,2,3,4,5]
print(linerSearch(arr, 10))        

# Time Complexity : O(n)
# Space Complexity  O(1)
