def checkPal(i, base=2):

    if base == 2:
        i = bin(i)[2:]
    else:
        i = str(i)
    lo = 0
    hi = len(i) - 1

    while(i[lo] == i[hi]):
        lo += 1;
        hi -= 1;

        if lo > hi:
            return True

    return False


def pal(limit):
    ans = []
    for i in range(1, limit, 2):
        if checkPal(i):
            if checkPal(i, 10):
                ans.append(int(i))

    return sum(ans)


print(pal(1000000))
