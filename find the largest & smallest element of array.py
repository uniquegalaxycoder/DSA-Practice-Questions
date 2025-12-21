# find the largest & smallest element of array

arr = [4,5,1,3,2]

n = len(arr)

sml_ele = arr[0]
max_ele = arr[0]

for i in range(1,n):
    if arr[i] < sml_ele :
        sml_ele = arr[i]
        
    elif arr[i] > max_ele :
        max_ele = arr[i]
        
print(sml_ele)
print(max_ele)

# Space complexity O(1) -> only using extra two veriables  
# time complexity O(n) -> traverse the array once
