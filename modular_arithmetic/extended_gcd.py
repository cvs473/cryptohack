def ext_gcd(a,b):
    if a == 0:
        return b, 0, 1

    gcd, s1, t1 = ext_gcd(b%a, a)
    s,t = upd_coef(a,b,s1,t1) 
    return gcd, s, t

def upd_coef(a,b,s,t):
    return(t - (b // a) * s, s) 


print(ext_gcd(32321, 26513))
