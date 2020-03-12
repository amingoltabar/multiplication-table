for i in range(1,11,1):
    for j in range(1,11,1):
        if j!=10:
            print(i*j,end=',')
        elif j==10:
            print(i*j,end='')
    print('')
        
