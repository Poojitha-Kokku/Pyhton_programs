n=int(input('n:'))
rev=0
temp=n
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(temp==rev):
    print('Palindrome')
else:
    print('Not Palindrome')
