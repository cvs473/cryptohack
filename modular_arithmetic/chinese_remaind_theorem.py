# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17

def find_q(a, b):
    if b > a:
        return 0
    else:
        q = 1
        while (q + 1) * b <= a:
            q += 1
        return q

def alg(a, c, b):
    modul = b
    print(f"{a}u + {c}v = {b}")
    q = find_q(a, b)
    r = a - b * q
    u_0 = 1
    u_1 = 0
    u_2 = u_0 - u_1 * q 
    print("a\t|b\t|r\t|q\t|u_0\t|u_1") 
    print(f"{a}\t|{b}\t|{r}\t|{q}\t|{u_0}\t|{u_1}") 
    while r != 0:
        a = b
        b = r
        q = find_q(a, b)
        r = a - b * q
        u_0 = u_1
        u_1 = u_2 
        u_2 = u_0 - u_1 * q 
        print(f"{a}\t|{b}\t|{r}\t|{q}\t|{u_0}\t|{u_1}") 
        if r == 0:
            if u_1 > 0:
                print(f"{u_1} is the mod inverse")
                return u_1
            else:
                print(f"{u_1 % modul} is the mod inverse")
                return u_1 % modul


b1 = 2
b2 = 3
b3 = 5

n1 = 5
n2 = 11
n3 = 17

N1 = n2 * n3
N2 = n1 * n3
N3 = n2 * n1

M1 = alg(N1, 1, n1)
M2 = alg(N2, 1, n2)
M3 = alg(N3, 1, n3)

x = (b1 * N1 * M1 + b2 * N2 * M2 + b3 * N3 * M3) % (n1 * n2 * n3)
print(x)
