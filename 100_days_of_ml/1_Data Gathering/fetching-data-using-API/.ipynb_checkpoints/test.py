#palindrom of a number

def pal(n):
    rev = 0
    tem = n 
    while tem !=0:
        ld = tem % 10
        rev = rev * 10 + ld
        tem = tem // 10

    return rev == n

if __name__ == '__main__':
        number = 234432
        # print(pal(number))


#factorial of a number

def fact(n):
    if n == 0:
        return 1
    else:
         return  n * fact(n-1)
         
def fact2(m):
    res = 1
    for i in range(2, m+1):
        res = res * i
    return res
    

if __name__ == '__main__':
    number = 4
    # print(fact(number))
    # print(fact2(number))
    


# find gcd or hcf of two number
def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b- a
    return a
def hcf(c,d):
    if d == 0:
        return c
    else:
         return hcf(d, c % d)
s = 12
t = 15
# print(gcd(s,t))
# print(hcf(s,t))
        


#lcm of a number 
def lcm(a,b):
    res = max(a,b)
    while True:
        if res % a == 0 and res % b == 0:
            return res 
        res +=1


if __name__ == '__main__':
    result = lcm(5,6)
    print(result)

#formula method
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return a * b // gcd(a,b)


if __name__ == '__main__':
    a = 4
    b = 6
    print(lcm(a,b))

    # **********************************************

#all divisor of a number
def allDivisor(n):
    i = 1
    while(i*i < n):
        if(n%i==0):
            print(i)
        i +=1
    while(i>=1):     
        if(n%i==0):
                print(n/i)
        i -=1
        
allDivisor(10)



# prime no series till n 
def primeseries(n):
    if n <= 1:
        return
    isPrime = [True] * (n+1)
    i = 2
    while i <= n:
        if isPrime[i]:
            print(i)
            for j in range(i*i, n+1, i):
                isPrime[j] = False
        i += 1

# primeseries(10)
        

#computing power of (x,n)
def computePower(a, b):
    p = a ** b
    print(p)

# computePower(10,3)