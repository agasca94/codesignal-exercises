def firstDuplicate(a):
    for x in a:
        if a[abs(x)-1] < 0: return abs(x)
        a[abs(x)-1] *= -1
    return -1
