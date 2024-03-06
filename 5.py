for N in range(1, 100):
    R = bin(N)[2:]
    sm = sum([int(x) for x in R])
    if sm % 2 == 1:
        R = R + '11'
    else:
        R = '11' + R
    R = int(R, 2)
    if R > 102:
        print(N)
        break