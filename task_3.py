# Function check whether a number is prime or not
def Prime(i, n):
#use of OR any number may be 0 or 1   
    if (n == 0 or n == 1):
        return False
    if (n == i):
        return True
    if (n % i == 0):
        return False
    i += 1
    return Prime(i, n)
#change value here and insert only prime numbers for i and n
if (Prime(1, 5)):
  print("true")
else:
  print("false")