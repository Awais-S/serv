import random

ugen = []
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['5','6','7','8','9','10','11','12'])
    if b in ['5', '6', '7', '8', '9']:
        z=random.choice(['0', '1'])
        bv=b+'.'+z+'.'+z
    else:
        bv=b
    B=['GT-', 'SM-']
    c=random.choice(B)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    application_version = str(random.randint(111,396))+'.0.0.'+str(random.randrange(10,49))+'.'+str(random.randint(111,396))
    V=str(random.randrange(11,99))
    uas=f'{aa} {bv}; {c}{d}{e}{f} Build/{d}{f}{V}{f}; wv) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uas)
