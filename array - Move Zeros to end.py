# move zeros to end 

"""
this is the best solution for move zeros end without changing prereserved order of other element
Time Complexity : O(n)
Space Complexity : O(1)
"""

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

