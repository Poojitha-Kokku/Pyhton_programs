def print_triangle(): 
    current_number=1 
    for i in range(1,5):
        for j in range(1,i+1):
            print(current_number,end='')
            current_number+=1 
            if current_number>10:
                break 
        print()
        if current_number>10:
            break
print_triangle()
