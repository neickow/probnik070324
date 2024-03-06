f=open('17.txt')
s=[int(x) for x in f.readlines()]
mx17=-10**20
for i in range(len(s)):
    if s[i]%17==0:
        mx17=max(mx17, s[i])
mxs=0
ans=0
for i in range(len(s)-1):
    if s[i]+s[i+1]>mx17:
        ans+=1
        mxs=max(mxs, s[i]+s[i+1])
print(ans, mxs)