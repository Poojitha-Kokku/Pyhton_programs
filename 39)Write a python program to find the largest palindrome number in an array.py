def palindrome(arr):
    length=len(arr)
    arr.sort()
    print(" ",arr[length-2])
arr=[1,232,54545,999991]
large=palindrome(arr)
