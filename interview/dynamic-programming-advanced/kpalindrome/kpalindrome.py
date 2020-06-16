def kpalindrome(s, k):
    return helper(s, 0, len(s) - 1, k)

def helper(s, l, r, k):
    if r <= l:
        return True
    if s[l] == s[r]:
        return helper(s, l+1, r-1, k)
    if k == 0:
        return False
    sol = helper(s, l+1, r, k-1)
    if sol:
        return True
    return helper(s, l, r-1, k-1)
