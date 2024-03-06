f=open('24.txt')
s=f.readline()
mxk=0
k=0
for i in range(1, len(s)-1):
    if s[i]!=s[i+1] and s[i-1]!=s[i]:
        k+=1
    else:
        mxk=max(mxk, k)
        k=0
print(mxk)