a=6
sum=0
for i in range(1,a):
    if(a%i==0):
        sum=sum+i
if(sum==a):
    print("perfecf",a)
else:
    print("not perfect",a)
