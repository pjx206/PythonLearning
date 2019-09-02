#decrypt caesar cipher
ct = input('Input cipher:')

#lower case or upper case
is_lower = True
for i in ct:
    if i.isupper():
        is_lower = False
        break

print('decrypting...')
print('Possible original text:')
ct =  ct.upper()
for i in range(1, 26):
    msg = ''
    for c in ct:
        if c.isalpha():
            msg += chr((ord(c) - i - 65) % 26 + 65)
        else:
            msg += c
    if is_lower:
        print(msg.lower())
    else:
        print(msg)