def main():
    n = int(input('How many lines do you want to generate:'))
    for l in triangle(n):
        print(l)

def triangle(n):
    i = 1
    l = [1]
    yield(l)
    nl = []
    i += 1
    while i <= n:
        l.insert(0, 0)
        l.append(0)
        for j in range(len(l) - 1):
           nl.append(l[j] + l[j+1])
        i += 1
        yield(nl)
        l, nl = nl, []
        

if __name__ == '__main__':
    main()