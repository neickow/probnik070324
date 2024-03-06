for A in range(100):
    i=0
    for x in range(100):
        for y in range(100):
            if (2*x+3*y != 150) or (x<A) and (y<A):
                i+=1
    if i==100**2:
        print(A)
        break