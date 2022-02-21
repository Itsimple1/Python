def fp(a,d):
    if d==1:
        return a
    elif d%2==0:
        return fp(a*a, d//2)
    else:
        return a*fp(a*a, (d-1)//2)
    
def TestMilleraRabina(n):
    global a, b, c
    s = 0
    d = n-1
    while True:
        if d%2==0:
            s+=1
            d//=2
        else:
            break
    for i in range(1, n):
        T = 1
        x = fustpower(i,d,n,1)
        if x==1:
            a+=1
        else:
            for j in range(s):
                x = fustpower(i, 2**j*d, n, 1)
                if x==-1%n:
                    T = 0
                    break
            if T==1:
                c+=1
            else:
                b+=1
def TestFerma(n):
    global c, a
    for i in range(1,n):
        if fustpower(i,n-1,n,1)==1:
            a+=1
        else:
            c+=1
    

a = 0
b = 0
c = 0
TestMilleraRabina(n)
if c==0:
    print('Miller-Rabin test: True', c, a, b)
else:
    print('Miller-Rabin test: False', c, a, b)
a = 0
c = 0
TestFerma(n)
if c==0:
    print('Fermat test: True',c, a)
else:
    print('Fermat test: False', c, a)
