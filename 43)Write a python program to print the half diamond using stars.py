def half_diamond(n):
    for i in range(1,n+1):
        print('*'*i)
    for i in range(n-1,0,-1):
        print('*'*i)
n=5
half_diamond(n)
