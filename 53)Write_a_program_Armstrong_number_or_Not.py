n=int(input())
sum=0
temp=n
while n>0:
    rem=n%10
    sum=sum+rem**3
    n=n//10
if(temp==sum):
    print("Armstrong")
else:
    print("not Armstrong")
