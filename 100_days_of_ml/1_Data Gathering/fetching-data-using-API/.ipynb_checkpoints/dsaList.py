# task - find the average of list 
def listAverage(li):
    t = 0
    for i in li:
        t = t +i
        n = len(l1)
    return t/n
    


def listAvg(li):

    return sum(l1)/len(l1)


l1 = [10,20,30,40]
print(listAvg(l1))
print(listAverage(l1))



#seperate even and odd list from a main list

def sepEvenorOdd(li):
    even = []
    odd = []
    for i in li:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even , odd
            
l1 = [2,3,4,5,6,7,8,9]            
res = sepEvenorOdd(l1)
print(res)


# get smaller elements from list 
def smlList(li,a):
    small_list = []
    for i in li:
        if i < a:
            small_list.append(i)
    return small_list

l1 = [30,53,3,87,17,26,77]
a =  40
print(smlList(l1,a))


#list  comprehension
def graterthanX(li,n):
    lst = [x for x in li if x < n]
    return lst

def seperate_even_odd(li):
    even = [x for x in li if x%2 == 0]
    odd = [x for x in li if x % 2 != 0]
    return even, odd

    
li = [6,23,4,7,90,13,24,54,34,77]
n = 30
# print(graterthanX(li,n))
# print(seperate_even_odd(li))







#dictnory comprehension
li = [1,3,4,2,5]
di = {x:x**3 for x in li}
print(di)

d2 = {x:f"ID{x}" for x in range(5)}
print(d2)


#largest element in list 
def largestElement(li):
    n = 0
    for i in li:
        if i > n:
            n = i
    return n
    
    

l1 = [54,63,13,9,65,78,99,103,45,32,200]    
# print(largestElement(l1))



#second largest element in list
def SecondLargestElement(li):   
    if len(li)<2:
        return None
    largest = secondLargest = float('-inf')

    for i in li:
        if i > largest:
            secondLargest = largest
            largest = i
        elif i > secondLargest and i != largest:
            secondLargest = i
        
    return secondLargest
    
    
l1 = [20,10,40,20,40]
print(SecondLargestElement(l1))



#check if a lst is sorted or not
def checkSorted(li):
    e = 0
    for i in range(1,len(li)):
        if li[i] < li[i-1]:
            return False
            i += 1
    return True
l1 = [2,3,4,1]
# print(checkSorted(l1))


#reverse a list 
def revList(li):
    s = 0
    e = len(li) -1
    while s < e:
        li[s],li[e] = li[e],li[s]
        s += 1
        e -= 1
    return li
    
l1 = [34,44,54,64,74,84,94]
l2 = ['sumed', 'ajit', 'rohan','shailesh']
# print(revList(l1))



#remove duplicate elements from list
def remove_Duplicates(arr):
    re = 1
    for i in range(1,len(arr)-1):
        if arr[re-1] != arr[i]:
            arr[re] = arr[i]
            re += 1
    return re
li = [10,20,20,10]

# print(remove_Duplicates(li))

#rotate list by one 
def leftRotate(li):
    li = li[1:] + li[0:1]
    print(li)

def leftR(li):
    li.append(li.pop(0))
    print(li)
l1 = [50,60,70,80]
# leftRotate(l1)
# leftR(l1)

















