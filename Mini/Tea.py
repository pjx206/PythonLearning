from struct import unpack

def encrypt(msg: str, key: str) -> str:
    """
    encrypt msg using TEA with key
    """
    def cut(thing, length):
        return [bytes(thing[i*length:(i+1)*length], encoding='utf-8') for i in range(len(thing) // length)]

    # formatting msg and key to make there lengths valid
    msg += '\x00' * (8 - len(msg) % 8)

    #TODO: get every 4 bytes in msg, get 4 part of key
    msg = cut(msg, 4)
    key = cut(key, 4)

    cipher = []
    for i in range(len(msg) // 2):
        sum = 0
        left = msg[i*2]
        right = msg[i*2+1]
        delta = 0x9E3779B9
        for i in range(32):
            sum += delta
            left += ((right << 4) + key[0]) ^ (right + sum) ^ ((right >> 5) + key[1]) & 0xffff
            right += ((left << 4) + key[2]) ^ (left + sum) ^ ((left >> 5) + key[3]) & 0xffff
        cipher.append(left, right)
    ciphertext = ''.join(map(chr, cipher))
    return ciphertext



def decrypt(cipher: str, key: str) -> str:
    """
    decrypt ciphertext using TEA with key
    """
    pass


if __name__ == '__main__':
    while True:
        mode = input(
            'Enter mode (1 for encryption, 2 for decryption, 0 to quit):')

        if int(mode) == 1:
            msg = input('Enter message to be encrypted using TEA:')
            key = input('Key:')
            print('cipher:' + encrypt(msg, key))
        elif int(mode) == 2:
            cipher = input("Enter ciphertext:")
            key = input('Key:')
            print('After decryption:')
        else:
            exit(0)
