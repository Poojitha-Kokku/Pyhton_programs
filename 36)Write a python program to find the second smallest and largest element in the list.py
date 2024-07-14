def find(list):
    length=len(list)
    list.sort()
    print('second largest element is:',list[length-2])
    print('second smallest elemnt is:',list[1])
list=[12,45,16,17,19,20]
large=find(list)
