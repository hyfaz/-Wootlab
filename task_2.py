#n is any number from 1 to whatsoever  
#The function should return true if it is a prime number or false if it isn’t
def prime(n):
    if (n==1):
        return False    
    elif (n==2):
        return True;
    else:
        for x in range(2, n):
            if(n % x==0):
                return False
        return True             
print(prime(3))
#enter any prime number in print(fx prime)