def first_occur(arr,x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if x > arr[mid]:
            low = mid +1
        elif x < arr[mid]:
            high = mid-1
        else:
            if mid == 0 or arr[mid-1] !=  arr[mid]:
                return mid
            else:
                return -1
    return -1

def last_occur(arr,x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if x > arr[mid]:
            low = mid +1
        elif x < arr[mid]:
            high = mid-1
        else:
            if mid == len(arr)-1 or arr[mid] !=  arr[mid+1]:
                return mid
            else:
                low = mid +1
    return -1

def max_occur(arr,x):
    first = first_occur(arr,x)
    if first == -1:
        return 0
    else:
        return last_occur(arr,x) - first + 1

arr = [5,10,10,20,20,20,10]
x = 10
p = max_occur(arr,x)
print(p)