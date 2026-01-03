# move zeros to end 

"""
this is the best solution for move zeros end without changing prereserved order of other element
Time Complexity : O(n)
Space Complexity : O(1)
"""

# Better Approach

def MoveZerosEnd(arr:list)-> list :
      n = len(arr)                            # O(1) -> Space Complexity
      j = 0                                   # O(1) -> Time Complexity
      for i in range(n):                      # O(n) -> Space Complexity
          if arr[i] != 0 :                    # O(1) -> Time Complexity
              arr[i],arr[j] = arr[j],arr[i]   # O(1) -> Time Complexity
              j += 1
      return arr
  
arr = [0,0,2,0,1,0,4,3]
x = MoveZerosEnd(arr)
print(x)

# -> [2,1,4,3,0,0,0,0]

# Brute force Solution 
"""
Time Complextiy : O(n^2)
Space COmplexity : O(1)
"""

def moveZeroEnds(arr:list) :
      n = len(arr)
      for i in range(n):
            for j in range(i, n) :
                  if arr[i] == 0 :
                        arr[i], arr[j] = arr[j], arr[i]
      return arr 

arr = [0,0,2,0,1,0,4,3]
y = moveZeroEnd(arr)
print(y)
