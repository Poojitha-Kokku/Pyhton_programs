def perfect_no(a):
    sum=0
    for i in range(1,a):
        if(a%i==0):
            sum=sum+i
            sum==a
            return "perfect no"
        else:
            return "not a perfect no"
print(perfect_no(6))
