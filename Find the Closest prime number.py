# Only return the closest prime number

def closestPrimeNum(num):
    
    for i in range(1,num):
        flag = False    
        n = num + i
        for j in range(2,n):
            if (n % j) == 0:
                flag = True
                break
        
        if flag ==  False:
            return f"{n} is prime number."
            
        flag = False
        n = num - i
        if n>1:
            for j in range(2,n):
                if (n % j) == 0:
                    flag = True
                    break
            if flag ==  False:
                return f"{n} is prime number."

print(closestPrimeNum(10))




# Print all the closest prime numbers

num = 1001

for i in range(1,num):
    flag = False    
    n = num + i
    for j in range(2,n):
        if (n % j) == 0:
            flag = True
            break
        
    if flag ==  False:
        print(n, "is prime number")
        
    flag = False
    n = num - i
    if n>1:
        for j in range(2,n):
            if (n % j) == 0:
                flag = True
                break
        if flag ==  False:
            print(n, "is prime number")
 

 
