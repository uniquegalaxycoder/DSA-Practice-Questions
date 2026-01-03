""" Sort an array in wave form """

def SortArrayWave(arr:list):
  n = len(arr)
  for i in range(0, n-1, 2) :      # ( Start, End, Step) 
        arr[i], arr[i+1] = arr[i+1], arr[i]

  return arr 

arr = [1,2,3,4,5,6]
x = SortArrayWave(arr)
print(x)

"""
  => Output 
    [2, 1, 4, 3, 6, 5] 

"""
