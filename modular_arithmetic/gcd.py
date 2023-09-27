def gcd(a, b):
    q = a // b    
    r = a % b
    while r != 0:
        a = b
        b = r
        q = a // b
        r = a % b
    print(b)


a = 66528
b = 52920

if a > b:
    gcd(a, b)
else:
    gcd(b, a)
