class calculator:
    def add(x,y):
        return x+y
    def subtract(x,y):
        return x-y
    def multiply(x,y):
        return x*y
    def divide(x,y):
        if y!=0:
            return x/y
        else:
            return("cant divide by 0")
result=calculator.add(7,5)
print("7+5=",result)
result=calculator.subtract(34,21)
print("34-21=",result)
result=calculator.multiply(54,2)
print("54*2=",result)
result=calculator.divide(18,9)
print("18/9=",result)

