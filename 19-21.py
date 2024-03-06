print('19 ЗАДАНИЕ')
def f1(a,b, p):
    if (a+b>=57) and (p==3): # petya
        return True
    if (a+b>=57) and (p==2): # ivan
        return False
    if (a+b<57) and (p==3):  # petro
        return False
    if p%2==1:  # petr
        return f1(a+b , b , p+1) or f1(a , b+a , p+1)
    if p%2==0:  # vanya
        return f1(a+b , b , p+1) or f1(a , b+a , p+1)
for s in range(1, 48):
    if f1(10, s,1)==True:
        print(s)
print('20 ЗАДАНИЕ')
def f1(a,b, p):
    if (a+b>=57) and (p==4): # petya
        return True
    if (a+b>=57) and (p==3): # ivan
        return False
    if (a+b<57) and (p==4):  # petro
        return False
    if p%2==0:  # petr
        return f1(a+b , b , p+1) and f1(a , b+a , p+1)
    if p%2==1:  # vanya
        return f1(a+b , b , p+1) or f1(a , b+a , p+1)
for s in range(1, 48):
    if f1(9, s,1)==True:
        print(s)
print('21 ЗАДАНИЕ')
def f1(a,b, p):
    if (a+b>=57) and (p==3 or p==5): # petya
        return True
    if (a+b>=57) and (p==2 or p==4): # ivan
        return False
    if (a+b<57) and (p==5):  # petro
        return False
    if p%2==0:  # petr
        return f1(a+b , b , p+1) or f1(a , b+a , p+1)
    if p%2==1:  # vanya
        return f1(a+b , b , p+1) and f1(a , b+a , p+1)
for s in range(1, 48):
    if f1(9, s,1)==True:
        print(s)