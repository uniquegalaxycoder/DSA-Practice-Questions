#Find second largest / second smallest


def get_SecondLargets(arr:list):
    n = len(arr)
    largest, secondLargest = float('-inf'), float('-inf')
    for i in range(n):
        if arr[i] > largest :
            secondLargest = largest
            largest = arr[i]
        elif arr[i] > secondLargest and arr[i] < largest :
            secondLargest = arr[i]
    return secondLargest
    
def get_SecondSmallest(arr:list):
    n = len(arr)
    small, secondSmall = float('inf'), float('inf')
    for i in range(n):
        if arr[i] < small :
            secondSmall = small 
            small = arr[i]
        elif arr[i] < secondSmall and arr[i] > small :
            secondSmall = arr[i]
    return secondSmall
            
arr = [1,2,3,4,5,6]

secondLargets = get_SecondLargets(arr)
secondSmall = get_SecondSmallest(arr)

print(f"Second Smallest : {secondSmall} \nsecond Large :{secondLargets}")

#Time Complexity  : O(n)
#Space Complexity : O(1)

