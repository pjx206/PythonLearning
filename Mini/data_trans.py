from functools import reduce


def char2num(c) -> int:
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[c]


def str2int(s) -> int:
    return reduce(lambda x, y: x * 10 + y, map(char2int, s))


def str2float(s) -> float:
    dot_pos = s.find('.')
    r = 0.0

    def f1(a, b):
        return a * 10 + b

    def f2(a, b):
        return a / 10 + b
    # get the digits before the dot
    r += reduce(f1, map(char2num, s[0:dot_pos]))
    # get the digits after the dot
    r += reduce(f2, map(char2num, s[len(s): dot_pos - len(s): -1])) / 10
    return r
