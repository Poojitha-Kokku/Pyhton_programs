def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
n=int(input())
r=int(input())
m=int(input())
perm=fact(n)//(fact(r)*fact(n-r))
print(perm)
output=perm%m
print(output)
