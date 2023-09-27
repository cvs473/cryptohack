new_string = ""
for char in "label":
    new_string += chr(ord(char) ^ 13)
print(new_string)
