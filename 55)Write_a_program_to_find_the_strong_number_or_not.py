import math
a=int(input(''))
sum=0
temp=a
while(temp>0):
    digit=temp%10
    sum+=math.factorial(digit)
    temp//=10
if(sum==a):
    print('Strong Number')
else:
    print('not Strong Number')
