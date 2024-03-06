def f(n):
    s=''
    while n>0:
        s+=str(n%5)
        n=n//5
    return s
s=5 ** 2004 - 5 ** 1016 - 25 ** 508 - 5 ** 400 + 25 ** 250 - 27
s=f(s)
print(s.count('4'))