p = 29
arr = [14, 6, 11]
for i in range(p):
    if i * i % p in arr: 
        print(i, i * i % p)
