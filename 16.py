def f(n):
    if n<5:
        return n+f(n+1) + f(n+2)
    else:
        return n
print(f(2))