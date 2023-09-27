cipher_text = "CKVWYX NSCR VKGCESD REXNBON"
sentence = cipher_text.split()
for i in range(1, 26):
    new_sent = ""
    for word in sentence:
        new_word = "" 
        for char in word:
            new_char = chr((ord(char) - 65 - i) % 26 + 65)
            new_word += new_char
        new_sent += ' ' 
        new_sent += new_word
    print(new_sent)
    
    
