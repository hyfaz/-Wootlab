#palindrome
def Palindrome(b):
    return b == b[::-1]
b = "salamimalas"
ans = Palindrome(b) 
if ans:
    print("Yes")
else:
    print("No")