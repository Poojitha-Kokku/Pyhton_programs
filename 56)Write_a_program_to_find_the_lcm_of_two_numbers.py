n1=int(input(''))
n2=int(input(''))
for i in range(max(n1,n2),1+(n1*n2)):
    if(i%n1==i%n2==0):
        lcm=i
        break
print('The LCM of two numbers',lcm)
