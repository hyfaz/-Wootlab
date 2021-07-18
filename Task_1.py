#Write a fx that takes an array of positive integers. 
#defined fx as that f all positive intergers
def arrayofpositivenumbers(a, n):
#defines values to add to sum of either even or odd    
    even=0
    odd=0
#for value i in whole numbers n    
    for i in range(n):
#any sum of value from a(0-5) divide by 2 would indicate even or odd       
        if a[i]%2==0:
            even+=a[i] #evensum in array
        else:
            odd+=a[i] #oddsum in array
    return {'even':even, 'odd':odd}

a=[1, 2, 3, 4, 5, 6] 
n=len(a) 

print(arrayofpositivenumbers(a, n))
#any number divisable by 2 is Even while not divisable is Odd
#print(fx array+ve)