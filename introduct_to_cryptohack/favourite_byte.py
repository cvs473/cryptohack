hexd = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
code = bytes.fromhex(hexd)
for i in range(256):
    flag = ""
    res = [chr(n^i) for n in code]
    flag = "".join(res)
    print(flag)
