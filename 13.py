from ipaddress import *
m=ip_address('255.255.252.0')
ans=2**(f'{m:b}'.count('0')-1)-2
print(ans)