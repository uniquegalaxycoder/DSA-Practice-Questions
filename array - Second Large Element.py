

def SecondLarge(arr:list)-> int :
    n = len(arr)
    first_large = float("-inf")
    second_large = float("-inf")
    
    for i in range(n):
        if arr[i] > first_large :
            second_large = first_large
            first_large = arr[i]
        elif arr[i] > second_large and arr[i] < first_large :
            second_large = arr[i]
    return f"Second Max {second_large}"


arr = [1,2,7,4,5,6]
output = SecondLarge(arr)
print(output)
"""
Time Complexity : O(n)
Space Complexity : O(1)
        
""""
