"""
    Q.Third largest element in an array of distinct elements
"""

def Third_Large(arr:list)->int :
    n = len(arr)
    Large = float('-inf')
    SecondLarge = float('-inf')
    ThirdLarge = float('-inf')
    
    for i in range (n):
        if arr[i] > Large :
            ThirdLarge = SecondLarge
            SecondLarge = Large
            Large = arr[i]
        elif arr[i]> SecondLarge :
            ThirdLarge = SecondLarge
            SecondLarge = arr[i]
        elif arr[i] > ThirdLarge :
            ThirdLarge = arr[i]
    return f"First Element: {Large}\nSecond large element: {SecondLarge}\nThird Large Element: {ThirdLarge}"


arr = [1,2,4,21,5,6,7,8,20,12,22]
output = Third_Large(arr)
print(output)
