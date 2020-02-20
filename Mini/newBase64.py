import base64

stdtable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def decode_str(s, table):
    global stdtable
    transtab = str.maketrans(table, stdtable)
    s = s.translate(transtab)
    return base64.b64decode(bytes(s, encoding='ascii'))


def main():
    
    print(decode_str('ywjJza==', table=))

if __name__ == '__main__':
    main()
