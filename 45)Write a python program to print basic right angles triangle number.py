def inverted_triangle(): 
    current_number=10 
    for i in range(1,5):
        for j in range(1,6-i):
            print(current_number,end='')
            current_number-=1 
            if current_number<1:
                break 
        print()
        if current_number<1:
            break
inverted_triangle()
