def countFrequency(arr:list)->dict :
  n = len(arr)                         # O(1)
  frequency = {}                       # O(n)
  for i in range (n) :                 # O(n)
    if arr[i] not in frequency :       # O(1)  
      frequency[arr[i]] = 1            # O(1)
    else :
      frequency[arr[i]] += 1           # O(1)
  return frequency 
  
arr1 = [1,1,2,3,4,3,2,1,2,3,4,3,2,1]  
print(countFrequency(arr1))

# Time Complexity : O(n)
# Space Complexity : O(n) -> Because every time key will be append if not exists value will get updated n time. 
