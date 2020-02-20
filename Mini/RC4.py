import base64


def init_box() -> list:
    """Generate a s box"""
    key = input('Input your key:')
    if key == '':
        key = bytes('pjx_tql', encoding='utf-8')
        print('Default key("pjx_tql") will be used')
    else:
        key = bytes(key, encoding='utf-8')

    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def en_decrypt(box:list, data:bytes) -> bytes:
    res = []
    i = j = 0
    for b in data:
        i = (i + 1) % 256
        j = (j + box[i]) % 256
        box[i], box[j] = box[j], box[i]
        t = (box[i] + box[j]) % 256
        k = box[t]
        res.append(b ^ k)
    
    return base64.b64encode(bytes(res))

def main():
    s_box = init_box()
    msg = bytes(input("Enter the message:"), encoding='utf-8')
    print(en_decrypt(s_box, msg))
if __name__ == '__main__':
    main()