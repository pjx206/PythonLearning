def permute(nums):
    """return all possible permutation of a list"""
    all_permutation = []
    return all_permutation


def get_(l):
    if len(l) == 1:
        return l
    elif len(l) == 2:
        return l[::-1]
    else:
        nl = l[:-2]
        nl.append(l[:-1])
        nl.append(l[:-2])
        return nl


def main():
    nums = [1, 2, 3]
    print(permute(nums))


if __name__ == '__main__':
    main()
