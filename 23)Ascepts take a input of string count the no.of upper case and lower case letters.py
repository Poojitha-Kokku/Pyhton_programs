a=str(input())
upper=0
lower=0
for i in a:
    if i.isupper():
        upper+=1
    else:
        lower+=1
print('upper case letters are:',upper)
print('lower case letters are:',lower)
