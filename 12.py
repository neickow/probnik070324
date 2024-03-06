mnc=10000
ind=0
for i in range(100, 500):
    s='3'*i
    while '333' in s or '111' in s:
        if '111' in s:
            s=s.replace('111', '3', 1)
        else:
            s=s.replace('333', '1', 1)
    if int(s)<mnc:
        mnc=int(s)
        ind=i
print(ind)

