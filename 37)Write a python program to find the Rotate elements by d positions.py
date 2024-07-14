def rotate(l,d,n):
    list=[]
    list=l[d:]+l[0:d]
    return list
l=[1,2,3,5,6,7]
d=2
n=len(l)
l=rotate(l,d,n)
for i in l:
    print(i,end=" ")
