def cap(str):
 return ' '.join(map(lambda s: s[:-1]+s[-1].upper(),
                        s.title().split()))
s = "first on compus drive"
print("String before:", s)
print("String after:",cap(str))
