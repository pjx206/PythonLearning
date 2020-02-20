std_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def encode_str(s: str, tab=std_table) -> str:
    bits = ''
    for c in s:
        bin8 = bin(ord(c))[2:]
        bin8 = '0' * (8 - len(bin8)) + bin8
        bits += bin8

    remain = len(s) % 3
    bits += '0' * (6 - len(bits) % 6)
    code = ''
    for i in range(len(bits) // 6):
        code += tab[int(bits[i*6:(i+1)*6], 2)]

    return code + '=' * (3 - remain)


def decode_str(s: str, tab=std_table):
    bits = ''
    equals = 0
    for c in s[-2:]:
        if c == '=':
            equals += 1
    for c in s[:-equals]:
        bin6 = bin(tab.find(c))[2:]
        bin6 = '0' * (6 - len(bin6)) + bin6
        bits += bin6
    real_len = (len(s) - equals) * 6 // 8 
    decode = ''
    for i in range(real_len):
        decode += chr(int(bits[i*8: (i+1) * 8], 2))
    return decode


def main():
    table = std_table
    table = input('input customized table:')
    if len(table) != 64:
        print('using default table')
        table = std_table
    else:
        print('using"', table, '" as table')

    s = 'abcd'
    encoded = encode_str(s, tab=table)

    print(encoded)
    print(decode_str(encoded, tab=table))


if __name__ == '__main__':
    main()
