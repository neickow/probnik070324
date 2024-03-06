import itertools
k=0
alf=itertools.product('ГЕКЭ023', repeat=4)
for i in alf:
    k+=1
    s=''.join(i)
    if s[0] in ('0', '2', '3') and ('ГГ' not in s and 'ЕЕ' not in s and 'КК' not in s and 'ЭЭ' not in s and '00' not in s and '22' not in s and '33' not in s):
        print(k, s)