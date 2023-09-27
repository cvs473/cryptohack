from pwn import xor

hexd = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
message = bytes.fromhex(hexd)
result = xor(message[:7], "crypto{")
part_key = "myXORke" + 'y'
complete_key = (part_key * (len(message) // len(part_key)))[:len(message)]
flag = xor(message, complete_key)
print(flag)
