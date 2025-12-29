"""
        Q.Count even & Odd numbers 
"""

"""
1st approach
"""

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

"""
 # Time Complexity : O(n) array traverse all element
 # Space Complexity : O(1) only took static veriable
"""



"""
2nd Apporach : by integer methode [ ( n // 2) * 2 == n then even ] 
"""

def EvenOdd(arr:list)-> int:
    n = len(arr)
    even_count = 0
    odd_count = 0

    for i in range (n) :
        if (arr[i]//2)*2 == arr[i]:
            even_count += 1
        else :
            odd_count += 1 
    return f"Odd Element Count : {odd_count} & Even Element Count : {even_count} "

arr = [1,2,3,4,5,6,7,8,9,13,15]
x = EvenOdd(arr)
print(x)

""" 
--> Odd Element Count : 7 & Even Element Count : 4 
Time Complexity : O(n)
Space Complexity : O(1)
"""

"""
3rd Approach : by '&' bitwise operatore n & 1 == 0  
"""
def odd_even(arr:list) :
    n = len(arr)
    evens = 0
    odds = 0
    for i in range(n):
        if arr[i] & 1 == 0 :
            evens+= 1 
        else :
            odds +=1 
    return evens, odds 
    
arr = [1,2,3,4,5,6,7,8,9]
y = odd_even(arr)
print(y)

"""
Time Complexity : O(n)
Space Complexity : O(1)
"""


